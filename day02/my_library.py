import numbers

def cube(num: numbers) -> numbers:
    return num * num * num

def square(num: numbers) -> numbers:
    return  num * num

def addition(num1: numbers, num2: numbers, num3: numbers = 0, num4: numbers = 0) -> numbers:
    return num1 + num2 + num3 + int(num4)