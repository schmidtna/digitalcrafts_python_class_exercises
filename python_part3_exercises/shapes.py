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

def turthexa():
    for i in range(6):
        forward(100)
        right(60)

    plot.show()

if __name__ == "__main__":
    turthexa()

def turtocta():
    for i in range(8):
        forward(100)
        right(45)

    plot.show()

if __name__ == "__main__":
    turtocta()

def turtpenta():
    for i in range(5):
        forward(100)
        right(72)

    plot.show()

if __name__ == "__main__":
    turtpenta()

def turtsqr():
    for i in range(4):
        forward(100)
        right(90)

    plot.show()

if __name__ == "__main__":
    turtsqr()

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

def turttri():
    for i in range(3):
        forward(100)
        right(120)

    plot.show()

if __name__ == "__main__":
    turttri()