from grafo_knn import *
from matplotlib import pyplot as plt


def main():

    print("Hello World!")

    p0 = Point(10, 20)
    p1 = Point(20, 30)

    e1 = Euclidean_Space(500, 500)

    grafo = Knn_Graph(500, 500)

    # Inicializa um grafo knn
    grafo.grafo_knn(200, 7)

    #for point in grafo.points:
    #    plt.scatter(point.x, point.y)
    for edge in grafo.edges:
        plt.plot([edge.p1.x, edge.p2.x], [edge.p1.y, edge.p2.y], marker = '.', markersize = 10)



    print("Distance bewteen the two points is: " + str(e1.distance(p0, p1)))

    plt.show()

    input("Falows")

main()