# -*- coding: utf-8 -*-

"""
videoanalytics.pipeline
~~~~~~~~~~~~~~~~~~~~~~~

Base classes for the pipeline paradigm.
"""

from abc import ABC, abstractmethod
import networkx as nx

class Source(ABC): 
    """
    A source.
    """ 
    def __init__(self, context):
        """ Default constructor.
        """
        self.context = context
            
    @abstractmethod
    def setup(self):
        """ This method is called after all components from the pipeline are instanced.
        """
        pass
    
    @abstractmethod
    def read(self):
        """ This method is called until it returns None or the processing is cancelled.
        """
        pass
    
    @abstractmethod
    def shutdown(self):
        """ This method is called after the process finished.
        """
        pass    
    
class Sink(ABC):
    """
    A sink.
    """ 
    def __init__(self, context):
        """ Default constructor.
        """
        self.context = context
        self.display_enabled = True
        
    @abstractmethod
    def setup(self):
        """ This method is called after all components from the pipeline are instanced.
        """
        pass
    
    @abstractmethod
    def process(self):
        """ This method is called for each active component in the pipeline.
        """
        pass
    
    @abstractmethod
    def shutdown(self):
        """ This method is called after the process finished.
        """
        pass 

    def enable_display(self,state):
        """ Set/unset display output (does not necesarily apply to all components).
        """
        self.display_enabled = state
        pass         

    def toggle_display_enable(self):
        """ Toggle display output (does not necesarily apply to all components).
        """
        self.display_enabled = not self.display_enabled
        pass            



def process_pipeline(p,context):
    """ Execute a pipeline.
    The order of traversal of the components is computed using topological sort.
    """
    seq = [p.nodes[x]['component'] for x in list(nx.topological_sort(p))]
    sources = [x for x in filter(lambda x: issubclass(type(x),Source),seq)]
    sinks = [x for x in filter(lambda x: issubclass(type(x),Sink),seq)]
    
    # Init
    print("Initializing pipeline")
    print("Sequence:", list(nx.topological_sort(p)))
    for x in seq:    
        x.setup()
    
    # Process
    print("Processing pipeline")
    eof_not_reached = False
    for x in sources:
        eof_not_reached |= x.read()
    
    while eof_not_reached:
        for x in sinks:
            x.process()    
            
        # Read next frame
        eof_not_reached = False
        for x in sources:
            eof_not_reached |= x.read()
    
    # Shutdown    
    print("Shutting down pipeline")
    for x in seq:
        x.shutdown()         