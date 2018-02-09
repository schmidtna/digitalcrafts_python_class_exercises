# plot ex. 1

# def hello(name):
#     return "Hello {}".format(name)

# print(hello('Nick'))


# import matplotlib
# import matplotlib.pyplot as plot
# from matplotlib.ticker import MaxNLocator
# from collections import namedtuple
# import math
# from math import sin
# import numpy as np
# from numpy import arange


# plot ex. 2

# def f(x):
#     return x + 1

# def run():
#     xs = list(range(-3, 16))
#     ys = []
#     for x in xs:
#         ys.append(f(x))

#     plot.plot(xs, ys)
#     plot.show()

# if __name__ == "__main__":
#     run()

# Plot ex. 3
# def f(x):
#     return x * x

# def run():
#     xs = list(range(-100, 100))
#     ys = []
#     for x in xs:
#         ys.append(f(x))

#     plot.plot(xs, ys)
#     plot.show()

# if __name__ == "__main__":
#     run()

#plot ex. 4
# def f(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return -1

# def run():
#     xs = list(range(-5, 5, 1))
#     ys = []
#     for x in xs:
#         ys.append(f(x))

#     plot.bar(xs, ys)
#     plot.show()

# if __name__ == "__main__":
#     run()

# plot ex. 5 and 6

# def f(x):
#     return sin(x)

# def run():
#     xs = arange(-5, 5, .1)
#     ys = []
#     for x in xs:
#         ys.append(f(x))

#     plot.plot(xs, ys)
#     plot.show()

# if __name__ == "__main__":
#     run()

# Funct ex. 7

# def faren(x):
#     return (x * 1.8) + 32

# def celc(x):
#     return x

# def run():
#     faren_out = []
#     celc_out = []
#     x_list = list(range(-3, 5))    
#     for x in x_list:
#         faren_out.append(faren(x))
#         celc_out.append(celc(x))

#     plot.plot(x_list, faren_out, x_list, celc_out)
#     plot.show()

# if __name__ == "__main__":
#     run()

# funct ex. 8

def run():
    play = input("Play again? Type Y or N: ").upper()

    while play != "Y" and play != "N":
        print("Try again with Y or N")
        play = input("Play again? Type Y or N: ").upper()
    if play == "Y":
        return True  
    elif play == "N":
        return False
    # elif play.upper() != "Y" or "N":
    #     print("Try again with Y or N")
    
    print("kay")

if __name__ == "__main__":
    print(run())