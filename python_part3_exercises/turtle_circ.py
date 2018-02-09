from turtle import *
import matplotlib
import matplotlib.pyplot as plot

def turtcirc():

    up()
    right(90)
    forward(50)
    left(90)
    down()
    
    for i in range(2):
        
        width(4)
        circle(180)

    plot.show()

if __name__ == "__main__":
    turtcirc()