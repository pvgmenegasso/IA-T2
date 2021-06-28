import math
import numpy as np
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

        self._x = x;
        self._y = y;

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, x):
        self._x = x 

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, y):
        self._y = y

    # Overload == operator
    def __eq__(self, other):
        if self._x == other.x:
            if self._y == other.y:
                return True
        return False

    # Overload + operator
    def __add__(self, other):
        return Point(self._x+other.x(), self._y+other.y())

    # Overload - operator
    def __sub__(self, other):
        return Point(self._x-other.x(), self._y-other.y())


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
        self._p1 = p1
        self._p2 = p2 

    @property
    def p1(self):
        return self._p1
    @p1.setter
    def p1(self, p1):
        self._p1 = p1

    @property
    def p2(self):
        return self._p2
    @p2.setter
    def p2(self, p2):
        self._p2 = p2

    # Overrides the == operator
    def __EQ__(self, other):
        """
        Verifies wether an edge is equal to another
        Considers that the edges are not directed, 
        I.E edges as opposed to vectors

        @Params
            e: Edge
                The edge with which we would like to compare

        """

        # Gets the two points that define the other edge
        p1e = other.p1()
        p2e = other.p2()

        # Compare them:
        # is the first point equal to any of the points in this edge ?
        if p1e == self._p1 or p1e == self._p2:
            # Now we check the other point
            if p2e == self._p1 or p2e == self._p2:
                # The edges are equal
                return True
        # The edges are different
        return False


class Euclidean_Space:
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

    def __init__(self, xSize: int, ySize: int):
        """
        Initializes the euclidean space and it's boundaries
        
        Parameters
        ----------
        xSize : int
            The maximum x coordinate of the space
        ySize : int
            The maximum y coordinate of the space
        
        """

        self._xSize = xSize
        self._ySize = ySize

    @property
    def xSize(self):
        return self._xSize
    @xSize.setter
    def xSize(self, x):
        self._xSize = x

    @property
    def ySize(self):
        return self._ySize
    @ySize.setter
    def ySize(self, y):
        self._ySize = y


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
        if p.x <= self._xSize:
            if p.y <= self._ySize:
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
        float 
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


class Knn_Graph(Euclidean_Space):
    """
    This class inherits functions from the Euclidean Space class
    and adds a vector of points and a vector of edges, to completely
    represent a knn graph

    Attributes
    ----------
        points: np.ndarray
            A list of points on this graph
        edges: np.ndarray
            A list of edges

    Methods
    -------

    """


    def __init__(self, x_size: int, y_size: int):
        # Calls super constructor
        super().__init__(x_size, y_size)

        # Declare vectors of points and edges
        self._points = []
        self._edges = []


    @property
    def points(self):
        return self._points
    @points.setter
    def points(self, points):
        self._points = points

    @property
    def edges(self):
        return self._edges
    @edges.setter
    def edges(self, edges):
        self._edges = edges


    def add_point(self, p: Point):
        """
        Adds a point to this Graph

        Parameters
        ----------
        p: Point
            The point to add

        """

        # check if the point already exists in the graph
        for point in self._points:
            # Point already exists, try to add a new random point
            if point == p:
                self.add_point(Point(np.random.randint(0, self._xSize), np.random.randint(0, self._ySize)))
        self._points.append(p)

    def add_edge(self, e: Edge):
        """
        Adds an Edge to this Graph

        Parameters
        ----------
        e: Edge
            The edge to add

        """

        # check if the graph contains the points that the edge reffers to
        if e.p1 in self._points and e.p2 in self._points:
            # append the edge to the list, if it is not there already
            if e not in self._edges:
                self._edges.append(e)
            else:
                # The edge is already present on the graph, raise error
                raise ValueError.with_traceback()
 
    def farthest_point(self, point: Point):
        """
        Finds the point that is farther away from a given point on the graph
        obs. The point given as argument must have already been removed from the list

        Parameters
        ----------
        point: Point
            The point to which the farthest point will be found

        Returns
        -------
        Float
            The distance found
        Point
            The point that is farther away from the given point
        """

        # assume the maximum distance to be 0
        max_distance = 0
        # Temporary Point
        pTemp = Point()

        # Percorre todos os pontos para checar a maior distancia
        for p in self._points:
            # Calcula a distancia entre o ponto argumento e o ponto atual
            distance = self.distance(point, p)
            # Se a distancia for maior que a máxima, atualiza a máxima e salva o ponto
            if distance > max_distance:
                max_distance = distance 
                pTemp = p
        # Retorna a distância e o ponto encontrados
        return distance, pTemp

    def nearest_neighbour(self, point: Point, minimalDistance : float = 0.0): 
        """
        Returns the nearest point to the given point

        Parameters
        ----------
        point: Point
            The point whose nearest neighbour will be found

        minimalDistance: float
            Only look for points farther than this distance, defaults to 0
        
        Returns
        -------
        Point
            The nearest neighbour
        Float
            The distance
        """

        temp = Point() # instantiates a new point at the origin
        tempMin = self.ySize*self.xSize # Defines the minimum distance as the area of the euclidean space

        # go through all the points on the graph
        for p in self._points:
            # if a point is nearer than the current minimal distance,
            # assigns it as the new nearest point
            dist = self.distance(p, point)
            if(dist < tempMin and dist > minimalDistance ):
                # the new nearest neighbour is p
                temp = p
                # the new nearest distance is the newfound one
                tempMin = dist

        return temp, tempMin

    def neighbours(self, point: Point):
        """
        Return all the direct neighbours for a given point

        Parameters
        ----------
        point: Point
            The point whose neighbours will be returned

        Returns
        -------
        neighbours: Point[]
            A list of neighbour points

        """

        neighbours = []

        # First we find all the edges spanning from point:
        for edge in self._edges:
            # Check if point is in one of the edge's ends:
            if point == edge.p1:
                # The other point is a neighbour !
                neighbours.append(edge.p2)
            elif point == edge.p2:
                # p1 is a neighbour:
                neighbours.append(edge.p1)

        return neighbours

    def grafo_knn(self, v, k):
        # Para o tamanho V faça
        for i in range(0,v):
            print("gerando ponto .."+str(i))
            # Adiciona um ponto aleatóreo na lista de pontos, o ponto não pode ser maior do que 
            # o tamanho do espaço euclidiano
            self.add_point(Point(np.random.randint(0, self._xSize), np.random.randint(0, self._ySize)))
        # Para cada vértice faça
        for edx, vertex in enumerate(self.points):
            print("Gerando hastes do ponto "+str(edx))
            min_distance = 0
            tempPoint = Point()
            # Designa k arestas
            for i in range(0,k):
                #Encontra os k vizinhos mais próximos
                tempPoint, min_distance = self.nearest_neighbour(vertex, min_distance)
                # Adiciona ao conjunto de arestas
                self.add_edge(Edge(vertex, tempPoint))
