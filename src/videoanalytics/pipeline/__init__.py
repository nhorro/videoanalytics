# -*- coding: utf-8 -*-

"""
This module contains the base classes for the pipeline paradigm.
"""

from abc import ABC, abstractmethod
import logging
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import time

# FIXME
import sys
if 'ipykernel' in sys.modules:
    from tqdm import tqdm_notebook as tqdm
else:
    from tqdm import tqdm


class Source(ABC): 
    """
    Abstract class for a source component.
    """ 

    """
    Name. Used as an unique identifier to refer to the component in the pipeline.
    """ 
    name = ""
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

    @abstractmethod
    def get_progress(self):
        """ This method is called for components that read from a source of known length.
        """
        pass    

class Sink(ABC):
    """
    Abstract class for a sink component.
    """     

    """
    Name. Used as an unique identifier to refer to the component in the pipeline.
    """ 
    name = ""

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
    """
    Class that represents a configuration of components in a pipeline.
    """     

    logger = logging.getLogger(__name__)

    def __init__(self):
        self.dag = nx.DiGraph()
        self.optimized = False
        self.metrics = {}
        self.total_iterations = 0
        self.abs_t0 = 0
        self.abs_t1 = 0
        self.total_elapsed_time = 0

    def add_component(self,component):
        self.dag.add_node( component.name, component=component )

    def set_connections(self,connections):
        self.dag.add_edges_from(connections)

    def optimize(self):
        """
        Optimizing the pipeline consistis in removing isolated blocks from the graph.
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

        # FIXME: progress only works for 1 source right now
        progress_bar = tqdm(total=100.0)
        last_progress = sources[0].get_progress()

        i = 0
        self.abs_t0 = time.perf_counter()          
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

            # FIXME: progress only works for 1 source right now
            curr_progress = sources[0].get_progress()
            progress_bar.update(curr_progress-last_progress)            
            last_progress = curr_progress
            i+=1
            
        self.abs_t1 = time.perf_counter()        
        self.total_elapsed_time = self.abs_t1 - self.abs_t0
    
        # Shutdown  
        self.logger.info("Shutting down pipeline")
        self.total_iterations = i
        for x in seq:
            x.shutdown()               
            self.metrics[x.name+"_avg_dt"] /= self.total_iterations            

    def get_metrics(self):
        """ Get the average execution time for each block in seconds.
        """
        return self.metrics

    def get_total_execution_time(self):
        """ Get the total execution time in seconds.
        """
        return self.total_elapsed_time

    def plot(self,ax):
        """ Plot the pipeline graph.

        Note: currently only matplotlib is supported.
        """
        #nx.draw_networkx(self.dag, 
        #    pos=nx.spring_layout(self.dag), with_labels=True, font_weight='bold')
        #plt.show()
        nx.draw_networkx(self.dag, 
                 pos=graphviz_layout(self.dag, prog='neato'), 
                 node_size=4000, arrowsize=20,node_shape="o",node_color="#1f78b4",
                 with_labels=True, font_weight='bold',ax=ax)        
