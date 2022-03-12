fib_cache = {}
def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fib_cache[n] = value
    return value

repeat = int(input("How many numbers would you like to see?"))
for n in range(1,repeat+1):
    print(n, ':', fibonacci(n))
print("Try not to overload!")