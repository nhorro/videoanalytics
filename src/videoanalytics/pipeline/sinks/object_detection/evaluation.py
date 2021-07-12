import numpy as np
import pandas as pd
from mean_average_precision import MetricBuilder

"""
This module contains utilities for evaluation of object detection models using mAP.
"""

def evaluate_object_detection_predictions(df_gt_dets, df_pred_dets, classes,model_name):
    """ Evaluate the predictions returned by an object detection model.
  
    Args:        
        df_gt_dets(pandas.DataFrame): ground truth detections as returned by 
            :meth:`videoanalytics.pipeline.sinks.object_detection.utils.load_detections_from_file_list`.
        df_pred_dets(pandas.DataFrame): predictions.
        classes(list): list of class indexes to evaluate.
        model_name(str): model name to use in the returned dataframe.

    Returns:
        - A dataframe containing the results.
    """
    metric_fn = MetricBuilder.build_evaluation_metric("map_2d", async_mode=True, num_classes=len(classes))

    # add samples to evaluation
    for filename in df_gt_dets.filename.unique():
        for class_idx in classes:
            # [xmin, ymin, xmax, ymax, class_id, difficult, crowd]
            gt = df_gt_dets[(df_gt_dets.filename==filename) & 
                        (df_gt_dets.class_idx==class_idx)][['x0','y0','x1','y1','class_idx','difficult','crowd']].values

            # [xmin, ymin, xmax, ymax, class_id, confidence]
            preds = df_pred_dets[(df_pred_dets.filename==filename) & 
                             (df_pred_dets.class_idx==class_idx)][['x0','y0','x1','y1','class_idx','score']].values
            metric_fn.add(preds, gt)

        df_od_metrics = pd.DataFrame ({
            "VOC PASCAL": [
                metric_fn.value(iou_thresholds=0.5, 
                recall_thresholds=np.arange(0., 1.1, 0.1))['mAP'] ], 
            "VOC PASCAL (all points)": [metric_fn.value(iou_thresholds=0.5)['mAP']],
            "COCO": [
                metric_fn.value(
                    iou_thresholds=np.arange(0.5, 1.0, 0.05), 
                    recall_thresholds=np.arange(0., 1.01, 0.01), 
                    mpolicy='soft')['mAP']]
        },index=[model_name])
        
        return df_od_metrics