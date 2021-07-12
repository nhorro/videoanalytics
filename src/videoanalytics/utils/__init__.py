# -*- coding: utf-8 -*-

"""
This module contains miscelaneous functions for conversion of types and adapting format
of data shared by more than one component.
"""

def read_class_names(filename):
    '''Reads a text file containing classes names in DarkNet format.
        
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
