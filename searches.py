from abc import abstractmethod
from types import FunctionType
from grafo_knn import *
from auxiliary_structures import *
import numpy as np

"""
This file defines some types of searches used to find a path
in a knn graph. The objective is to be able to compare several 
different types of them in regards to processing time and memory
usage. So each one of the algorithms has it's own time keeping 
variables for time analysis purposes 

"""



class GenericSearch():
    """
    This class defines a general Framework
    for search algorithms
    """

    def __init__(self, destination : Point):
        """
        Parameters
        ----------

        destination: Point
            The destination point for the search algorithm
        """

        #Start priority queue of points to visit
        self._queue =  PriorityQueue()

        #Initiate list of points in the order in which they where visited
        self._visitedList = []

        #Store the destination for the search
        self._destination =  destination

    @abstractmethod
    def heuristic():
        pass

    def visited(self, point: Point):
        if point in self._visitedList :
            return True
        return False

    def step(self,actual: Point,  graph : Knn_Graph):
       
        """
        Expand current node

        Parameters
        ----------
        actual: Point
            The current point in the graph.
        graph: Knn_Graph
            The current graph

        Returns
        -------
        True
            if the search is completed
        False
            if the search continues

        """

        # Check if the point has not yet been visited
        if self.visited(actual):
            return False

        # The point has not yet been visited, insert it into the visited list
        print("Inserting " +str(actual)+"into visited list")
        self._visitedList.append(actual)

        ## Expand the node        
        # For each node neighbouring the current node
        for node in graph.neighbours(actual):
            # Did we find the goal node ?
            if node == self._destination:
                #EUREKA
                print("SEARCH COMPLETED")
                return True
            # It's not the goal node
            # has it been already visited ?
            if node in self._visitedList:
                # do nothing
                pass
            # is it on the queue ? (has it already been planned for visitting ?)
            # Don't forget we have to strip x and y dimension to check
            elif [node.x, node.y, self.heuristic(node, graph)] in self._queue.array.tolist():
                # also do nothing
                pass
            else:
                # Insert the value into the open list:
                self._queue.insert([node.x, node.y, self.heuristic(node, graph)])

        # Went trough all direct neighbours, found no destinatino
        # returns false
        return False
            
    def search(self, start: Point, graph: Knn_Graph):
        """
        Do the search

        Parameters
        ----------
        start: Point
            Where to start the search
        graph: Knn_Graph
            The graph in which to do the search
        """

        finish = False

        # Insert the starting node into the queue
        self._queue.insert([start.x, start.y, self.heuristic(start, graph)])

        print("Starting search !!")

        print("from node: "+str(start))


        while(finish == False):

            if self._queue.size == 0:
                return False

            current_node_values = self._queue.remove()

            # Discards the heuristic value and create an auxiliary
            # node with x and y values
            current_node = Point(current_node_values[0], current_node_values[1])

            # Step
            finish = self.step(current_node, graph)

        return True


# As this fuction inherits from the generic search function, we only need to 
# Define it's heuristic and the rest is python's problem ;)
class BestFirst(GenericSearch):

    def __init__(self, destination: Point):
        super().__init__(destination)

    def heuristic(self, origin: Point, graph: Knn_Graph):
        """
        Returns the heuristic for the
        best first search, given a sef of two points.
        the goal is: the heuristic is smaller the closest 
        the origin point is to the destination one.


        Parameters
        ----------
            origin: Point
                The origin point from which to calculate the heuristic

        Returns
        -------
            Float
                The result of the formula:  h =  distance

        """

        return graph.distance(origin, self._destination)

    def search(self, origin: Point, graph: Knn_Graph):
        super().search(origin, graph)
