
import cv2
import numpy as np
import tensorflow as tf
from videoanalytics.pipeline.sinks import Sink

class ImageClassifier(Sink):
    def __init__(self, name, context, model_path, img_size,labels,x0=None,y0=None,x1=None,y1=None):
        super().__init__(name, context)                 
        self.frame_counter = 0

        self.img_size = img_size
        self.classifier_model = tf.keras.models.load_model(model_path)
        self.labels = labels
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
                
    def predict_proba(self, frame):        
        tmp = frame[self.y0:self.y1,self.x0:self.x1]
        # Verificar si hay que convertir        
        tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2RGB)
        tmp = cv2.resize(tmp,dsize=(self.img_size,self.img_size), interpolation = cv2.INTER_CUBIC)
        tmp = np.expand_dims(tmp,axis=0)
        return tf.nn.softmax(self.classifier_model.predict(tmp))
    
    def predict(self,frame, display=False):
        y_pred = self.predict_proba(frame)        
        return np.argmax(y_pred)
    
    def predict_raw(self,frame, display=False):
        return tf.nn.softmax(self.classifier_model.predict(tmp))
    
    def get_label(self,class_idx):
        return self.labels[class_idx]
        
    def setup(self):        
        if "START_FRAME" in self.context:
            self.frame_counter= self.context["START_FRAME"]
        pass

    def process(self):           
        activity_idx = self.predict( self.context["FRAME"] )
        
        activity_description = self.get_label(activity_idx)
        self.context["ACTIVITY_IDX"] = activity_idx            
        self.context["ACTIVITY_DESCR"] = activity_description

        #activity_proba = self.model.predict_proba(data.reshape(1, -1))
        # self.context["ACTIVITY_PROBA0"] = activity_proba[0][0] # "Levado de redes 1"
        # self.context["ACTIVITY_PROBA1"] = activity_proba[0][1] # "Levado de redes 2"
        # self.context["ACTIVITY_PROBA2"] = activity_proba[0][2] # "Levado de redes 3"
        # self.context["ACTIVITY_PROBA3"] = activity_proba[0][3] # "Redes recogidas"
        # self.context["ACTIVITY_PROBA4"] = activity_proba[0][4] # "Descarga de redes"
        # self.context["ACTIVITY_PROBA5"] = activity_proba[0][5] # "Redes descargadas / clasificación"
        # self.context["ACTIVITY_PROBA6"] = activity_proba[0][6] # "Otro"
        #print(activity_idx,activity_description)            
        #print(data)
            
        self.frame_counter+=1     
        
    def shutdown(self):        
        pass
# =================================================================================================