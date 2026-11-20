def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


count = int(input("Enter fibonnaci sequence numbers to be printed:  "))

for int in range(count):
    print(fibonacci(int))