# -*- coding: utf-8 -*-

"""
Base classes for the pipeline paradigm.
"""

from abc import ABC, abstractmethod
import logging
import networkx as nx
import time


class Source(ABC): 
    name = ""
    
    """
    A source.
    """ 
    def __init__(self, name:str, context:dict):
        """ Default constructor.
        """
        self.context = context
        self.name = name        
            
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
    name = ""

    """
    A sink.
    """ 
    def __init__(self, name:str, context:dict):
        """ Default constructor.
        """
        self.context = context
        self.name = name
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

class Pipeline:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.dag = nx.DiGraph()
        self.optimized = False
        self.metrics = {}
        self.total_iterations = 0

    def add_component(self,component):
        self.dag.add_node( component.name, component=component )

    def set_connections(self,connections):
        self.dag.add_edges_from(connections)

    def optimize(self):
        """
        Remove isolated blocks, if any
        """
        self.dag.remove_nodes_from(list(nx.isolates(self.dag)))
        self.optimized = True

    def execute(self):
        """ Execute the pipeline.
        The order of traversal of the components is computed using topological sort.
        """
        if not self.optimized:
            self.optimize()

        seq = [self.dag.nodes[x]['component'] for x in list(nx.topological_sort(self.dag))]
        sources = [x for x in filter(lambda x: issubclass(type(x),Source),seq)]
        sinks = [x for x in filter(lambda x: issubclass(type(x),Sink),seq)]

        # Init
        self.logger.info("Initializing pipeline")
        self.logger.info("Sequence:", list(nx.topological_sort(self.dag)))
        for x in seq:    
            self.logger.info("Setting up", x.name)
            x.setup()
            self.metrics[x.name+"_avg_dt"] = 0.0
    
        # Process
        self.logger.info("Processing pipeline")
        eof_not_reached = False
        for x in sources:
            eof_not_reached |= x.read()

        i = 0
        while eof_not_reached:
            for x in sinks:
                t0 = time.perf_counter()                
                x.process()                    
                t1 = time.perf_counter()
                self.metrics[x.name+"_avg_dt"] += t1-t0
            
            # Read next frame
            eof_not_reached = False
            for x in sources:
                t0 = time.perf_counter()             
                eof_not_reached |= x.read()
                t1 = time.perf_counter()
                self.metrics[x.name+"_avg_dt"] += t1-t0
            i+=1
    
        # Shutdown  
        self.logger.info("Shutting down pipeline")
        self.total_iterations = i
        for x in seq:
            x.shutdown()               
            self.metrics[x.name+"_avg_dt"] /= self.total_iterations            

    def get_metrics(self):
        return self.metrics