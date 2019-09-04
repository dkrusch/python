# 1. write a function called add that accepts two arguments and returns their sum
# 2. write a function called subtract that accepts two arguments and returns the difference
# 3. write a function called calculate that accepts a function as an argument. In calculate's body, it should execute that function and pass it the numbers 3 and 5
# 4. print an execution of calculate and pass it a reference to add
# 5. print an execution of calculate and pass it a reference to subtract

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def calculate(functional):
    return functional(3, 5)

print(calculate(add))
print(calculate(subtract)