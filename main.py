from grafo_knn import *
from auxiliary_structures import *
from matplotlib import pyplot as plt


def main():

    print("Hello World!")

    #p0 = Point(10, 20)
    #p1 = Point(20, 30)

    #e1 = Euclidean_Space(500, 500)

    #grafo = Knn_Graph(500, 500)

    # Inicializa um grafo knn
    #grafo.grafo_knn(500, 2)

    #grafo2 = Knn_Graph(3000, 3000)
    #grafo2.grafo_knn(3000, 5)

    #for point in grafo.points:
    #    plt.scatter(point.x, point.y)
    #for i, edge in enumerate(grafo2.edges):
    #    print("plotting edge: "+str(i))
    #    plt.plot([edge.p1.x, edge.p2.x], [edge.p1.y, edge.p2.y], marker = '.', markersize = 3)


    p = PriorityQueue()

    p.insert([0, 0, 4])
    p.insert([3, 2, 0])
    p.insert([6, 1, 3])
    p.insert([4, 3, 1])
    p.insert([7, 2, 2])
    p.insert([8, 3, 8])
    p.insert([9, 3, 3])
    p.insert([12, 3, 3])

    print(p.array)

    elements = p.remove()

    print(elements)

    print(p.array)

    
    

    #print("Distance bewteen the two points is: " + str(e1.distance(p0, p1)))

    #plt.show()

    input("Falows")

main()