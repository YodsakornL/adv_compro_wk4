def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error"
    return x / y

x = int(input("Enter num1 ="))
y = int(input("Enter num2 ="))

def main():
    print(add(x,y))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y))


main()