from turtle import *
import matplotlib
import matplotlib.pyplot as plot

def turtstar():
    f = 90
    r = 144
    l = 72

    for i in range(5):
        forward(f)
        right(r)
        forward(f)
        left(l)
    fillcolor("blue")

    plot.show()

if __name__ == "__main__":
    turtstar()