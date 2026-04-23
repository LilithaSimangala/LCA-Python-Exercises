#Lliitha Simangala Python Operators Code
# Question 1: Arithmetic and Assignment Operators

x = 10
y = 5


x += 3

y *= 2

result = x / y

print("Question 1 Result:", result)

# Question 2: Comparison and Logical Operators

a = 12
b = 8
c = 10

condition1 = a > b
condition2 = b % 2 == 0
condition3 = c <= a

final_condition = condition1 or (condition2 and condition3)

print("Question 2 Result:", final_condition)


# Question 3: Conditional Statements

score = int(input("Enter test score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Question 3 Grade:", grade)



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    answer = num1 + num2
elif operation == "-":
    answer = num1 - num2
elif operation == "*":
    answer = num1 * num2
elif operation == "/":
    if num2 == 0:
        answer = "Cannot divide by zero"
    else:
        answer = num1 / num2
else:
    answer = "Invalid operation"

print("Question 4 Result:", answer)