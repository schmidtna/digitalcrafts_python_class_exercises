height = int(input("number"))

for i in range(0, height):
    stars = (i * 2) + 1
    spaces = height - i 
    print(( " " * spaces) + ("*" * stars))
