import math
'''

The k-nearest neighbor graph (k-NNG) is a graph in which
 two vertices p and q are connected by an edge, if the 
 distance between p and q is among the k-th smallest 
 distances from p to other objects from P. The NNG is a 
 special case of the k-NNG, namely it is the 1-NNG. 
 k-NNGs obey a separator theorem: they can be partitioned
 into two subgraphs of at most n(d + 1)/(d + 2) vertices
 each by the removal of O(k1/dn1 − 1/d) points.[3]


'''


class Point:
    """
    This class defines a point in an euclidean space

    ...

    Attributes
    ----------
    x : int
        The x coordinate of the point
    y : int
        The y coordinate of the point

    Methods
    -------

    """

    def __init__(self, x: int = 0, y: int = 0):
        """
        Initializes a point in an euclidean space

        Parameters
        ----------
        x : int, optional
            The x coordinate of the point, defaults to 0
        y : int, optional
            The y coordinate of the point, defaults to 0

        """

        self.x = x;
        self.y = y;


class Edge:
    """ 
    An edge is a line connecting two points in an Euclidean space

    Attributes
    ----------
    p1: Point
        One end of the edge
    p2: Point
        The other end of the edge  

    """ 

    def __init__(self,p1: Point, p2: Point):
        """ 
        Constructor for the edge

        Parameters
        ----------
        p1: Point
            One end of the edge 
        p2: Point
            The other end of the edge 
        """
        self.p1 = p1
        self.p2 = p2 


class EuclideanSpace:
    """
    This class defines an euclidean space
    
    ...

    Attributes
    ----------
    xSize : int
        The maximum x coordinate of the space 
    ySize : int
        The maximum y coordinate of the space 

    
    Methods
    -------

    """

    def __init__(self,xSize: int,ySize: int):
        """
        Initializes the euclidean space and it's boundaries
        
        Parameters
        ----------
        xSize : int
            The maximum x coordinate of the space
        ySize : int
            The maximum y coordinate of the space
        
        """

        self.xSize = xSize
        self.ySize = ySize


    def in_space(self, p: Point):
        """"
        Verifies if a given point belongs to this Euclidean space 

        Parameters
        ----------
        p: Point
            The point to check for ownership

        Returns
        -------
        bool
            Wether or not p is inside this space
        
        """
        if p.x <= self.xSize:
            if p.y <= self.ySize:
                return True
            return False


    def distance(self, point1: Point, point2: Point):
        """
        Calculates the euclidean distance between two points on this space

        ...

        Parameters
        ----------
        point1 : Point
            The first point 
        point2 : Point
            The second point 

        Returns
        -------
        int 
            The distance between the two points
        
        Raises
        ------
        ValueError:
            Raises ValueError if one of the points is outside of this euclidean space
        
        """

        # Calculates the distance only if both points belong to the current space
        if self.in_space(point1) and self.in_space(point2):
            
            return math.sqrt(math.pow(point1.x - point2.x, 2) + math.pow(point1.y - point2.y, 2))

        raise ValueError

