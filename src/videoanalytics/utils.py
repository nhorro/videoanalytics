# -*- coding: utf-8 -*-

"""
This module contains miscelaneous functions for conversion of types and adapting format
of data shared by more than one component.
"""

def read_class_names(filename):
    '''Reads a textfile containing classes names in DarkNet format.
        
        Args:
            filename (str): text file. See examples.

        Returns:
            names (dict): A dictionary that maps each class name with an id.
        '''
    names = {}
    with open(filename, 'r') as data:
        for ID, name in enumerate(data):
            names[ID] = name.strip('\n')
    return names

def format_boxes(bboxes, image_height, image_width):
    '''Helper function to convert bounding boxes from normalized ymin, xmin, ymax, xmax to frame coordinates: xmin, ymin, xmax, ymax
        
        Args:
            bboxes (np.array): Array containing multiple bounding boxes.
            image_height (int): height of the image in pixels.
            image_width (int): width of the image in pixels.

        Returns:
            bboxes (np.array): converted bounding boxes.
        '''    
    for box in bboxes:
        ymin = int(box[0] * image_height)
        xmin = int(box[1] * image_width)
        ymax = int(box[2] * image_height)
        xmax = int(box[3] * image_width)
        width = xmax - xmin
        height = ymax - ymin
        box[0], box[1], box[2], box[3] = xmin, ymin, width, height
    return bboxes