num = int(input("size of square?"))
y = int(input("size of square?"))

# def square(num, y):
for i in range(num):
    if i == 0 or i == (num - 1):
        print("*" * y)
    else:
        print("*" + (" " * (y - 2 )) + "*")

# square(num, y)