from turtle import *
import matplotlib
import matplotlib.pyplot as plot

def turtpenta():
    for i in range(5):
        forward(100)
        right(72)

    plot.show()

if __name__ == "__main__":
    turtpenta()