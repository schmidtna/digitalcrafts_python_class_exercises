from turtle import *
import matplotlib
import matplotlib.pyplot as plot

def turthexa():
    for i in range(6):
        forward(100)
        right(60)

    plot.show()

if __name__ == "__main__":
    turthexa()