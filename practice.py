def addition(*args):
    return sum(args)

num1 = int(input("Enter numbers separated by spaces: "))
num2 = int(input("Enter numbers separated by spaces: "))

add = addition(num1, num2)
print("Addition of numbers:",add)

def substraction(a,b):
    return a-b

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

sub = substraction(number1,number2)
print(f' Substraction of {number1} and {number2} =', sub)