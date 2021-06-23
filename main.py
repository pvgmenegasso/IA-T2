from grafo_knn import *
from matplotlib import pyplot as plt


def main():

    print("Hello World!")

    p0 = Point(10, 20)
    p1 = Point(20, 30)

    e1 = EuclideanSpace(500, 500)

    print("Distance bewteen the two points is: " + str(e1.distance(p0, p1)))

    plt.plot([p0.x, p0.y], [p1.x, p1.y], color="black")
    plt.show()

    input("Falows")

main()