import numpy as np

"""

This file defines some auxiliary structures needed for this program to function correctly


"""


class PriorityQueue():
    """
    This class implements a priority queue to be used specifically with this program
    it stores the X and Y coordinates of a node and it's associated heuristic, thus
    it consists of an n-dimensional nx3 matrix, as shown:
    [x0][x1][x2]....n
    [y0][y1][y2]....n
    [h0][h1][h2]....n

    Attributes
    ----------
    array: np.ndarray
        An array which is used as the backbone for our priority queue
    """

    def __init__(self):
        """
        Initializes the Queue with a n dimensional 3xn array

        Parameters
        ----------
        n: int
            the n dimension of the queue
        """
        self._array = np.zeros((1, 3))

    @property
    def array(self):
        return self._array
    @array.setter
    def array(self, array):
        self._array = array

    def insert(self, list):
        """
        Inserts a tuple x of 3 values into the Queue, from highest to lowest priority
        on tuples with the same priority, store new values first

        list[3] = [x, y, h]  where x is x coordinate, y is y coordinate and h is heuristic

        """
        # Strip values from argument list
        x = list[0]
        y = list[1]
        h = list[2]
      


        # Search for the priority value on the sorted matrix, return it's index
        index = np.searchsorted(self._array[:,2], h, side = "left",  )
        # Adds to the leftmost part of given index the specified values
        self._array = np.insert(self._array, index, [x, y, h], axis=0)


    def remove(self):
        """
        Removes the first item from our queue (it is already ordered ;))
        
        Returns
        -------
        float[3]
            The first tuple from the queue
        """
        elements = self._array[0,:] # get first set of tuples from array
        self._array = np.delete(self._array, 0, axis=0)
        return elements