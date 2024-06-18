# Develop a Python script that calculates the square and cube of a given number.
num = int(input("enter a number:"))
square = num ** 2
cube = num ** 3
print("square of num is", square)
print("cube of num is", cube)

#Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))

if num1>num2:
    print("num1 is greater than num2")
elif num1<num2:
    print("num1 is less than num2")
else:
    print("num1 is equals to num2")

