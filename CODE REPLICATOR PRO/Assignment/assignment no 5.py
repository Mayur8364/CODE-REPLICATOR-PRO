'''
Title: - Create a model for the following functions using Python
1. Factorial
2. Even or Odd
3. Reverse a string
Name : Ganesh Wagh
Roll No : 133
Batch: AiDs-B3
'''

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

def even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

def rev(s):
    return s[::-1]

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
