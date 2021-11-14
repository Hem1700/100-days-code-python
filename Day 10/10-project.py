import art


def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

def square(n1,n2):
    return n1 ** n2

def calculator():
    print(art.logo)
    operations = {"+": add, "-": sub, "*": multiply, "/": divide, "**": square}
    continue_calculating = 'y'
    num1 = float(input("What's the first number?: "))
    for key in operations:
            print(key)

    while continue_calculating != 'n':
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a nenw calculation: ")
        if continue_calculating == 'y':
            num1 = answer
        else:
            calculator()    


calculator()