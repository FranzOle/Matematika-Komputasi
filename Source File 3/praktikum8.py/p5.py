def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 9
print("Faktorial(n):", faktorial(n))
print("Fibonacci(n):", fibonacci(n))