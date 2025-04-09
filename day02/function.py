import numbers;


def return_value():
    # print("test")
    return 1000


print(return_value())


def return_integer() -> int:
    print("This is int function")


print(return_integer())


def cube(num: int) -> int:
    return num * num * num


print(cube(2))


def addition(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


print(addition(100, 200))


def addition(num1: numbers, num2: numbers, num3: numbers = 0, num4: numbers = 0) -> numbers:
    return num1 + num2 + num3 + int(num4)


print(addition(2, 3))
print(addition(100, 200, 300,"200"))

def funtion():
    pass
