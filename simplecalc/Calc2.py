import sys

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def main():
    operation = input("What do you want to do (a,-,*,/): ")
    print(sys.version)
    if operation != 'a' and operation != '-' and operation != '*' and operation != '/':
        # invalid operation
        print("You must enter a valid operation")
    else:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
    if operation == "a":
        print(add(num1, num2))
    elif operation == '/':
        print(divide(num1, num2))
    elif "-" == operation:
        print(subtract(num1, num2))
    else:
        print(multiply(num1, num2))


main()
