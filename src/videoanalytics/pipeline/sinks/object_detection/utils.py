import os
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches    

"""
This module contains utilities for format conversion, working with dataframes, and visualization.
"""




def convert_detections(df,box_format="xyxy"):
    """ Convert a dataframe in YOLO normalized format to absolute coordinates (x0,y0,x1,y1)

    Args:        
        df(pandas.DataFrame): input dataframe with columns x,y,w,h.

    Rerturns:
        A dataframe with columns x0,y0,x1,y1.
    """
    converted_df = df.copy()
    converted_df['x0'] = df.x
    converted_df['y0'] = df.y
    converted_df['x1'] = df.x+df.w
    converted_df['y1'] = df.y+df.h
    return converted_df    


def load_detections_from_file_list(det_list,box_format="xyxy"):
    """ Given a list of files, constructs a dataframe with the bounding boxes for each image.
    The list of files is typically obtained from the test directory text annotations 
    (YOLO normalized format is assumed).

    Args:        
        det_list(list): list of filenames.
        box_format (str): Currently only "xyxy" is supported. 

    Returns:
        A dataframe (see format below).

    The returned dataframe contains the following columns:
        - filename: name of the file.
        - frame_num: set to the index of the file in the list (this field is reserved for videos).
        - class_idx: class index.
        - x,y: bounding box center coordinates (normalized)
        - w,h: bounding box dimensions (normalized).
        - img_w,img_h: image width and height in pixels.

    If the box_format is 'xyxy' then the following columns will be transformed/added:
        - x,y,w,h: will be transformed to pixels
        - x0,y0,x1,y1: will be set to the bounding box top-left, bottom-right coordinates in pixels.    
    """
    df_gt_dets = pd.DataFrame()
    for frame_num, filename in enumerate(det_list):
        with open(filename,'r') as fp:
            frame = cv2.imread(os.path.splitext(filename)[0]+'.jpg')
            img_w = frame.shape[1]
            img_h = frame.shape[0]
            lines = fp.readlines()
            lines = [line.split() for line in lines]
            df_tmp = pd.DataFrame(lines,columns=["class_idx", "x","y","w","h"])
            
            # quickfix
            df_tmp.class_idx = df_tmp.class_idx.astype(int)
            df_tmp.x = df_tmp.x.astype(float)
            df_tmp.y = df_tmp.y.astype(float)
            df_tmp.w = df_tmp.w.astype(float)
            df_tmp.h = df_tmp.h.astype(float)
            
            df_tmp["frame_num"] = frame_num
            df_tmp["img_w"] = img_w
            df_tmp["img_h"] = img_h
            df_tmp["filename"] = os.path.splitext(os.path.basename(filename))[0]
            df_tmp = df_tmp.reindex(columns=["filename","frame_num","class_idx", "x","y","w","h","img_w","img_h"])
        df_gt_dets = df_gt_dets.append(df_tmp)
    
    # xmin,ymin,xmax,ymax format
    if box_format == "xyxy":
        df_gt_dets['w'] = df_gt_dets['w']*df_gt_dets['img_w']
        df_gt_dets['h'] = df_gt_dets['h']*df_gt_dets['img_h']    
        df_gt_dets['x'] = df_gt_dets['x']*df_gt_dets['img_w']
        df_gt_dets['y'] = df_gt_dets['y']*df_gt_dets['img_h']

        df_gt_dets['x0'] = df_gt_dets['x']-df_gt_dets['w']/2
        df_gt_dets['x1'] = df_gt_dets['x']+df_gt_dets['w']/2
        df_gt_dets['y0'] = df_gt_dets['y']-df_gt_dets['h']/2
        df_gt_dets['y1'] = df_gt_dets['y']+df_gt_dets['h']/2
        
    if True:
        df_gt_dets['difficult'] = 0
        df_gt_dets['crowd'] = 0
        
    return df_gt_dets  


def plot_predictions_vs_ground_truth(df_gt_dets,df_pred_dets,img_path, img_name, class_idx,ax):
    """ Given an image and class id present in two dataframes containing bounding boxes 
        for a set of images in x0,y0,x1,y1 format, plot the bounding boxes corresponding to the
        ground truth and predictions.

    Args:        
        df_gt_dets(pandas.DataFrame): ground truth detections as returned by 
            :meth:`videoanalytics.pipeline.sinks.object_detection.utils.load_detections_from_file_list`.
        df_pred_dets(pandas.DataFrame): predictions.
        img_path(str): path of the parent directory containing the input images.
        img_name(str): name of the image.
        class_idx(int): class index to plot (only one class is supported).
        ax (Axes): matplotlib axes instance.        
    """
    img = cv2.imread(os.path.splitext(img_path+img_name)[0]+'.jpg')    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    

    # Ground truth
    for r in df_gt_dets[(df_gt_dets.filename==img_name) &
                        (df_gt_dets.class_idx == class_idx)].iterrows():
        img = cv2.rectangle(img, (int(r[1].x0),int(r[1].y0)), 
                        (int(r[1].x1),int(r[1].y1)), (0,255,0), 4) 
    
    # Predictions
    for r in df_pred_dets[(df_pred_dets.filename==img_name) & 
                          (df_pred_dets.class_idx == class_idx)].iterrows():
        img = cv2.rectangle(img, (int(r[1].x0),int(r[1].y0)), 
                                 (int(r[1].x1),int(r[1].y1)), (0,0,255), 4)     

    ax.imshow(img, interpolation='bilinear', aspect='auto')
    ax.legend(handles=[mpatches.Patch(color='green', label='ground truth'),
                        mpatches.Patch(color='blue', label='predicted')])
    return ax    