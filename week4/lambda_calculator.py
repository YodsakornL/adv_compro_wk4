add = lambda x,y: x+y
subtract = lambda x, y: x-y
multiply = lambda x, y:x*y
divide = lambda x, y: x/y if y != 0 else "Error"

x = int(input("Enter num1 ="))
y = int(input("Enter num2 ="))

def main():
    print(add(x,y))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y))


main()