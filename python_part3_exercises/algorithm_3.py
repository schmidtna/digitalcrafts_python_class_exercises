def fibon():
    fib = [1, 2]
    fib_even = []
    while ((fib[-1]) + (fib[-2])) < 4000000:
        fib.append((fib[-1]) + (fib[-2]))
    for i in fib:
        if i % 2 == 0:
            fib_even.append(i)

    print(sum(fib_even))
print(fibon())