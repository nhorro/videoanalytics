# -*- coding: utf-8 -*-

"""
Association of events related to tracked objects entering/leaving ROIs.
"""

import shapely
from shapely.geometry import Point, Polygon, LineString, GeometryCollection
import numpy as np
import matplotlib.pyplot as plt



class ROIEvents:
  def __init__(self,screen_width,screen_height):
    self.screen_width = screen_width
    self.screen_height = screen_height

    # Regions

    # The screen is a special region
    self.screen_region = Polygon([
      (0,0),(screen_width,0),
      (screen_width,screen_height),(0,screen_height)
    ])

    # User defined regions and segments
    self.regions = {}
    self.segments = {}

    # Objects being tracked
    self.tracked_objs = {}

    # Set containing objects inside the screen
    self.objs_inside_screen = set()

    # Dictionary of sets containing objects inside each ROI
    self.objs_inside_rois = {}

    self.user_callback = self.__default_user_callback

  def add_roi(self,name,r):
    """ Add a ROI.
    """
    if name not in self.regions:
      self.regions[name] = r
      self.objs_inside_rois[name] = set()
    else:
      raise ValueError("ROI already exists")

  def add_segment(self,name,x0,y0,x1,y1):
    self.segment[name] = (x0,y0,x1,y1)

  def __default_user_callback(self, entered_screen,left_screen,
                              entered_roi, left_roi):
    
    """ Default user callback. Prints events to STDOUT.
    """
    for x in entered_screen:
      print("{} entered the screen".format(x))
    
    for x in left_screen:
      print("{} left the screen".format(x))

    for k_roi in entered_roi:
      print("Entered {} ".format(k_roi), entered_roi[k_roi])

    for k_roi in left_roi:
      print("Left {} ".format(k_roi), left_roi[k_roi])

  def __generate_events(self,objs_inside_screen_before,objs_inside_screen_after, 
          objs_inside_rois_before, objs_inside_rois_after):
    """ Test changes in object positions.
    """
    
    # Objects that entered the screen
    entered_screen = objs_inside_screen_after.difference(objs_inside_screen_before)

    # Objects that left the screen
    left_screen = objs_inside_screen_before.difference(objs_inside_screen_after)

    # Objects that entered a ROI
    entered_roi = { k_roi: objs_inside_rois_after[k_roi].difference(objs_inside_rois_before[k_roi]) for k_roi in self.regions }

    # Objects that left a ROI
    left_roi = { k_roi: objs_inside_rois_before[k_roi].difference(objs_inside_rois_after[k_roi]) for k_roi in self.regions }


    self.user_callback(entered_screen,left_screen,entered_roi,left_roi)
    
  def update_obj_positions(self,new_positions):
    # Store positions before update
    objs_inside_screen_before = self.objs_inside_screen.copy()
    objs_inside_rois_before = self.objs_inside_rois.copy()

    for k,v in new_positions.items():
      self.tracked_objs[k] = Point(v[0], v[1])

    # objects inside screen?
    self.objs_inside_screen = set()
    for k,v in self.tracked_objs.items():      
      if self.screen_region.contains(v):
        self.objs_inside_screen.add(k)

    # objects inside ROI?
    for k_roi,v_roi in self.regions.items():
      self.objs_inside_rois[k_roi] = set()
      for k_obj,v_obj in self.tracked_objs.items():              
        if v_roi.contains(v_obj):
          self.objs_inside_rois[k_roi].add(k_obj)
   
    self.__generate_events(objs_inside_screen_before,self.objs_inside_screen, 
                           objs_inside_rois_before, self.objs_inside_rois)

  def debug_render(self):
    fig,axes = plt.subplots(1,1,figsize=(18,6))

    # Plot screen region
    axes.plot(*self.screen_region.exterior.xy)

    # Plot other regions
    for x,v in self.regions.items():
      axes.plot(*v.exterior.xy,color="g") 

    # Plot line segments
    for x in self.segments:
      axes.plot(x[0], y[0], 'bo', linestyle="--")
      #axes.text(point1[0]-0.015, point1[1]+0.25, "Point1")
      #axes.text(point2[0]-0.050, point2[1]-0.25, "Point2")

    # Plot tracked obj
    for x,v in self.tracked_objs.items():
      axes.scatter(*v.xy,color="r") 

    axes.grid(which="Both")
    return axes