# -*- coding: utf-8 -*-

"""
videoanalytics.utils
~~~~~~~~~~~~~~~~~~~~

Miscelaneous functions for conversion of types and adapting format
of data shared by more than one component.
"""

def read_class_names(filename):
    names = {}
    with open(filename, 'r') as data:
        for ID, name in enumerate(data):
            names[ID] = name.strip('\n')
    return names

def format_boxes(bboxes, image_height, image_width):
    """# helper function to convert bounding boxes from normalized ymin, xmin, ymax, xmax ---> xmin, ymin, xmax, ymax
    """
    for box in bboxes:
        ymin = int(box[0] * image_height)
        xmin = int(box[1] * image_width)
        ymax = int(box[2] * image_height)
        xmax = int(box[3] * image_width)
        width = xmax - xmin
        height = ymax - ymin
        box[0], box[1], box[2], box[3] = xmin, ymin, width, height
    return bboxes