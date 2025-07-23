def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

factorial(1000)
# This will producce an error