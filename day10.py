#Calculator

def add(num1, num2):
    """Adds n1 and n2 and returns the sum"""
    return num1 + num2


def subtract(num1, num2):
    """Subtracts n2 from n1 and returns the difference"""
    return num1 - num2


def multiply(num1, num2):
    """Multiplies n1 by n2 and returns the product"""
    return num1 * num2


def divide(num1, num2):
    """Divides n1 by n2 and returns the quotient"""
    return num1 / num2

def intChecker(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


cont: bool = True
first: bool = True
check1: bool = False
checkOp: bool = False
check2: bool = False

while cont:
    ops = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if first:
            while check1 == False:
                n1: int = input("What's the first number? ")
                if len(n1) > 0:
                    check1 = intChecker(n1)
                    if check1 == True:
                        n1: int = int(n1)
                    else:
                        print("Re-enter a valid integer")
                else:
                    print("Re-enter a valid integer")

    for symbol in ops:
        print(symbol)

    while checkOp == False:
        operation: str = input("Pick an operation: ")
        if len(operation) == 1:
            if operation in ops:
                checkOp = True
            else:
                print("Re-enter a valid operation symbol")
        else:
            print("Re-enter a valid operation symbol")


    while check2 == False:
        n2: int = input("What's the second number? ")
        if len(n2) > 0:
            check2 = intChecker(n2)
            if check2 == True:
                n2: int = int(n2)
            else:
                print("Re-enter a valid integer")
        else:
            print("Re-enter a valid integer")



    function = ops[operation]
    total: int = function(n1, n2)
    print(f"The total is {total}")

    prompt: str = input("Would you like to continue? y/n\n")

    if prompt != "y":
        cont: bool = False
        print("Thank you for using the calculator")
    else:
        first: bool = False
        tot: bool = True
        n1: int = total
        print(f"The continuing number is {n1}")
