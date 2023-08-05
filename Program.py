def add(a,b):
    return a+b

x = int(input("Enter the first number"))
y = int(input("Enter the second number"))

def sub(a,b):
    return a-b


def multi(a,b):
    return a*b


def div(a,b):
    return a/b
def calculator(operation,x,y):
    match operation:
        case "add":
            return x + y
        case "subtract":
            return x - y
        case "multiply":
            return x * y
        case "divide":
            return x / y

operation = input("Please pick an operation")

print(calculator(operation, x, y))

    