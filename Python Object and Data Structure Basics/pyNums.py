# basic operations
def add(x, y):
    print("Addition:", x + y)
add(2, 3)

def subtract(x, y):
    print("Subtraction:", x - y)
subtract(10, 3)

def multiply(x, y):
    print("Multiplication:", x * y)
multiply(2, 5)

def divide(x, y):
    print("Division:", x / y)
divide(10, 2)

# Modulo or "Mod" Operator (returns the remainder)
def mod(x, y):
    print("Modulo:", x % y)
mod(7, 4)

# function to check if a x is even or odd
def evenOrOdd(x):
    z = x % 2
    if z == 0:
        print("Even")
    else:
        print("Odd")
evenOrOdd(20)
evenOrOdd(21)

# power function
def power(x, y):
    z = x ** y
    print(x, "to the", y, "is", z)
power(2, 3)