# -*- coding: utf-8 -*-

"""
Association of events related to tracked objects entering/leaving ROIs.
"""

import shapely
from shapely.geometry import Point, Polygon, LineString, GeometryCollection
import numpy as np
import matplotlib.pyplot as plt

from videoanalytics.pipeline import Sink
import json
import csv


class ROIEventsGenerator:
  def __init__(self,screen_width,screen_height,user_callback=None):
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

    if user_callback == None:
      self.user_callback = self.__default_user_callback 
    else:
      self.user_callback = user_callback 

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
    # FIXME
    
    # Plot tracked obj
    for x,v in self.tracked_objs.items():
      axes.scatter(*v.xy,color="r") 

    axes.grid(which="Both")
    return axes



class ROIEvents(Sink):
    '''
    Registers ROI events in the shared context.

    This component **READS** the following entries:

    +-------------------+-----------------------------------------------------+
    | Variable name     | Description                                         |
    +===================+============+==========+=============================+
    | START_FRAME       | Initial frame.                                      |
    +-------------------+-----------------------------------------------------+
    | TRACKED_OBJS      | Positions of identified objects.                    |
    +-------------------+-----------------------------------------------------+
    | INPUT_WIDTH       | Image width (regions are defined in absolute pixel  |
    |                   | coordinates).                                       |
    +-------------------+-----------------------------------------------------+
    | INPUT_HEIGHT      | Image width (regions are defined in absolute pixel  |
    |                   | coordinates).                                       |
    +-------------------+-----------------------------------------------------+
        
    This component **WRITES** the following entries:
    
    +-----------------------+-----------------------------------------------------+
    | Variable name         | Description                                         |
    +=======================+============+==========+=============================+
    | EVENTS_ENTERED_SCREEN | Object IDs that entered the screen region.          |
    +-----------------------+-----------------------------------------------------+
    | EVENTS_LEFT_SCREEN    | Object IDs that left the screen region.             |
    +-----------------------+-----------------------------------------------------+
    | EVENTS_ENTERED_ROI    | Object IDs that entered ROIs.                       |
    +-----------------------+-----------------------------------------------------+
    | EVENTS_LEFT_ROI       | Object IDs that left ROIs.                          |
    +-----------------------+-----------------------------------------------------+
    
    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        filename(str): CSV filename.
    '''
    def __init__(self, name, context,filename):
        super().__init__(name, context)
        self.verbose = False
        with open(filename) as f:
            self.rois = json.load(f)
            
        self.rois = self.rois["regions"]
            
        for i,v in enumerate(self.rois):
            self.rois[i]["polygon"] = Polygon(self.rois[i]["polygon"])

    def setup(self):                
        self.frame_counter = self.context["START_FRAME"]
        self.roi_eventgen = ROIEventsGenerator(
            screen_width = self.context["INPUT_WIDTH"],
            screen_height = self.context["INPUT_HEIGHT"],
            user_callback=self.__update)
        
        for r in self.rois:
            self.roi_eventgen.add_roi(r["name"],r["polygon"])
            
    def __update(self, entered_screen,left_screen, entered_roi, left_roi):
        
        self.context["EVENTS_ENTERED_SCREEN"] = entered_screen
        self.context["EVENTS_LEFT_SCREEN"] = left_screen
        self.context["EVENTS_ENTERED_ROI"] = entered_roi
        self.context["EVENTS_LEFT_ROI"] = left_roi
        
        if self.verbose:
            if len(entered_screen)>0:
                for x in entered_screen:
                    print("{} entered the screen".format(x))

            if len(left_screen)>0:
                for x in left_screen:
                    print("{} left the screen".format(x))

            for k_roi in entered_roi:
                if len(entered_roi[k_roi])>0:
                    print("Entered {} ".format(k_roi), entered_roi[k_roi])

            for k_roi in left_roi:
                if len(left_roi[k_roi])>0:
                    print("Left {} ".format(k_roi), left_roi[k_roi])            

    def process(self):                
        tracked_objs = {x[0]:[x[1]+x[3]/2,x[2]+x[3]/2] for x in self.context["TRACKED_OBJS"] }
        self.roi_eventgen.update_obj_positions(tracked_objs)
        self.frame_counter+=1

    def shutdown(self):               
        pass
    
    

class ROIEventsCSVWriter(Sink):
    '''
    Writes ROI events to CSV.

    This component **READS** the following entries:

    +-----------------------+-----------------------------------------------------+
    | Variable name         | Description                                         |
    +=======================+============+==========+=============================+
    | START_FRAME           | Initial frame.                                      |
    +-----------------------+-----------------------------------------------------+
    | TRACKED_OBJS          | Positions of identified objects.                    |
    +-----------------------+-----------------------------------------------------+
    | EVENTS_ENTERED_SCREEN | Object IDs that entered the screen region.          |
    +-----------------------+-----------------------------------------------------+
    | EVENTS_LEFT_SCREEN    | Object IDs that left the screen region.             |
    +-----------------------+-----------------------------------------------------+
    | EVENTS_ENTERED_ROI    | Object IDs that entered ROIs.                       |
    +-----------------------+-----------------------------------------------------+
    | EVENTS_LEFT_ROI       | Object IDs that left ROIs.                          |
    +-----------------------+-----------------------------------------------------+
    
    Args:        
        name(str): the component unique name.
        context (dict): The global context. 
        filename(str): CSV filename.
    '''
    def __init__(self, name, context,filename):
        super().__init__(name, context)
        self.verbose = False
        self.csv_file = open(filename, mode='w')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',', quotechar='"', 
                                     quoting=csv.QUOTE_MINIMAL)
        self.csv_writer.writerow(["frame_num","event","obj_id","roi"])

    def setup(self):                
        self.frame_counter = self.context["START_FRAME"]
            
    def process(self):                
        entered_screen = self.context["EVENTS_ENTERED_SCREEN"]
        left_screen = self.context["EVENTS_LEFT_SCREEN"]
        entered_roi = self.context["EVENTS_ENTERED_ROI"]
        left_roi = self.context["EVENTS_LEFT_ROI"]
        
        if len(entered_screen)>0:
            for obj_id in entered_screen:
                self.csv_writer.writerow([self.frame_counter,"ENTERED",obj_id,"SCREEN"])

        if len(left_screen)>0:
            for obj_id in left_screen:
                self.csv_writer.writerow([self.frame_counter,"LEFT",obj_id,"SCREEN"])

        for k_roi in entered_roi:
            if len(entered_roi[k_roi])>0:
                for obj_id in entered_roi[k_roi]:
                    self.csv_writer.writerow([self.frame_counter,"ENTERED",obj_id,k_roi])
                
        for k_roi in left_roi:
            if len(left_roi[k_roi])>0:
                for obj_id in left_roi[k_roi]:
                    self.csv_writer.writerow([self.frame_counter,"LEFT",obj_id,k_roi])        
        self.frame_counter+=1

    def shutdown(self):        
        self.csv_file.close()        
        pass    