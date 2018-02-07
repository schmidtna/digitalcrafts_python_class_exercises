num = int(input("size of square?"))

for i in range(num):
    print("*" * num)
    print("*" + " " * (num - 2) + "*")
    print("*" * num)   
