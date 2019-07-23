# Multiply 3 and any number
def mult(number):
    return 3 * number

# Adds two numbers together
def add(a, b):
    return a + b

# Data structure
numbers = [1, 2, 3, 6]
def sumOfListNumbers(somelist):
    temp = 0
    for item in somelist:
        temp += item
    return temp

# Program checker
# assert statement is used as a checker to see if the condition satisfied by your function
assert sumOfListNumbers(numbers) == 12
assert mult(3) == 9
assert add(1, 3) == 4
