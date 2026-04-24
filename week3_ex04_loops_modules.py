#LILITHA SIMANGALA Python LOOPS 

# Question 1: Using a for loop with a list

fruits = ["Apple", "Banana", "Orange", "Mango"]

for fruit in fruits:
    print(fruit)

# Question 2: Using a while loop for countdown

count = 5

while count >= 1:
    print(count)
    count -= 1

# Question 3: Using a for loop with range()

for number in range(1, 11):
    print(number * number)

# Question 4: Using the random module

import random

colors = ["Red", "Blue", "Green", "Yellow", "Black"]

for i in range(3):
    random_color = random.choice(colors)
    print(random_color)

# Question 5: Using a custom module

import math_operations

running = True

while running:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Choose (+, -, *, /): ")

    if operator == "+":
        print(math_operations.add(num1, num2))

    elif operator == "-":
        print(math_operations.subtract(num1, num2))

    elif operator == "*":
        print(math_operations.multiply(num1, num2))

    elif operator == "/":
        print(math_operations.divide(num1, num2))

    else:
        print("Invalid operator")

    again = input("Do another calculation? yes/no: ")

    if again.lower() != "yes":
        running = False