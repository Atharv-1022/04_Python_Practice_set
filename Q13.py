#Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.

def fib(n):
    if n==0 or n==1:
        return 1
    return fib(n-2)+(n-1)
print(fib(5))