def addition(*args):
    return sum(args)

num1 = int(input("Enter numbers separated by spaces: "))
num2 = int(input("Enter numbers separated by spaces: "))

add = addition(num1, num2)
print("Addition of numbers:",add)
