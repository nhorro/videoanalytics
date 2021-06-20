import tensorflow as tf
import cv2
from tensorflow.python.saved_model import tag_constants
from videoanalytics.utils import format_boxes
from videoanalytics.pipeline import Sink

import numpy as np

class YOLOv4Detector(Sink):
    def __init__(self, context,weights_filename,
                 allowed_classes = [0],
                 yolo_input_size = 416,
                 yolo_max_output_size_per_class=50,
                 yolo_max_total_size=50,
                 yolo_iou_threshold=0.45,
                 yolo_score_threshold=0.40):
        super().__init__(context)
        
        self.allowed_classes = np.array(allowed_classes)
        
        self.yolo_input_size = yolo_input_size
        self.yolo_max_output_size_per_class=yolo_max_output_size_per_class
        self.yolo_max_total_size=yolo_max_total_size
        self.yolo_iou_threshold=yolo_iou_threshold
        self.yolo_score_threshold=yolo_score_threshold
        
        self.saved_model_loaded = tf.saved_model.load(weights_filename, tags=[tag_constants.SERVING])
        self.infer = self.saved_model_loaded.signatures['serving_default']
    
    def setup(self):
        pass
            
    def process(self):
        
        # 1. Convertir la imagen a formato de entrada de YOLO
        frame_size = self.context["FRAME"].shape[:2]        
        image_data = cv2.resize(self.context["FRAME"], (self.yolo_input_size, self.yolo_input_size))
        image_data = image_data / 255.
        image_data = image_data[np.newaxis, ...].astype(np.float32)
        
        # 2. Inferencia
        batch_data = tf.constant(image_data)
        pred_bbox = self.infer(batch_data)
        for key, value in pred_bbox.items():
            boxes = value[:, :, 0:4]
            pred_conf = value[:, :, 4:]
        
        # 3. Non Max Supression
        boxes, scores, classes, valid_detections = tf.image.combined_non_max_suppression(
            boxes=tf.reshape(boxes, (tf.shape(boxes)[0], -1, 1, 4)),
            scores=tf.reshape( pred_conf, (tf.shape(pred_conf)[0], -1, tf.shape(pred_conf)[-1])),
            max_output_size_per_class=self.yolo_max_output_size_per_class,
            max_total_size=self.yolo_max_total_size,
            iou_threshold=self.yolo_iou_threshold,
            score_threshold=self.yolo_score_threshold
        )
        
        # 4. Convertir a Numpy y eliminar elementos que no se usan
        num_objects = valid_detections.numpy()[0]
        bboxes = boxes.numpy()[0]
        bboxes = bboxes[0:int(num_objects)]
        scores = scores.numpy()[0]
        scores = scores[0:int(num_objects)]
        classes = classes.numpy()[0]
        classes = classes[0:int(num_objects)]
        
        # 5. Filtrar clases que no interesan
        remove_idx = np.argwhere(~np.isin(classes,self.allowed_classes))
        bboxes = np.delete(bboxes, remove_idx, axis=0)
        scores = np.delete(scores, remove_idx, axis=0)
        classes = np.delete(classes, remove_idx, axis=0)
        num_objects = len(bboxes)
        
        # 6. Convertir BBs de normalized ymin, xmin, ymax, xmax ---> xmin, ymin, width, height
        original_h, original_w, _ = self.context["FRAME"].shape
        bboxes = format_boxes(bboxes, original_h, original_w)

        # 7. FIXME: encontrar una forma mejor de representar las detecciones
        self.context["DETECTIONS"] = [bboxes, scores, classes, num_objects]
    
    def shutdown(self):
        pass  