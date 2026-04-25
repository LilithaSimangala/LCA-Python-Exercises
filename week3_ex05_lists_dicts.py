#Lilitha Simangala Lists and Dictionary Exercise
# Question 1: Creating and Modifying Lists

# Creating a list of fruits
fruits = ["Grape", "Kiwi", "Peach"]

# Adding a fruit to the end of the list
fruits.append("Watermelon")

# Inserting a fruit at the beginning of the list
fruits.insert(0, "Orange")

# Removing a fruit from the list
fruits.remove("Kiwi")

# Print the modified list
print("Modified Fruits List:", fruits)


# Question 2: List Operations

# Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]

# Create a new list with each number squared
squared_numbers = []

for num in numbers:
    squared_numbers.append(num ** 2)

# Find the sum and average of the original numbers
total = sum(numbers)
average = total / len(numbers)

# Print the results
print("Original Numbers:", numbers)
print("Squared Numbers:", squared_numbers)
print("Sum:", total)
print("Average:", average)


# Question 3: Creating and Modifying Dictionaries

# Dictionary for a country and its capital
countries = {
    "South Africa": "Pretoria",
    "France": "Paris",
    "China": "Honk-Kong"
}

# Adding a new country-capital pair
countries["Zimbabwe"] = "Harare"

# Updating the capital of an existing country
countries["South Africa"] = "Cape Town"

# Removing a country-capital pair
del countries["France"]

# Print the modified dictionary
print("Modified Dictionary:", countries)

# Question 4: Dictionary Operations

# Creating a dictionary of fruit colors
fruit_colors = {
    "Peach": "Orange",
    "Banana": "Yellow",
    "Watermelon": "Green",
    "Grapes": "Purple"
}

# Printing all the fruits (keys)
print("Fruits:", fruit_colors.keys())

# Printing all the colors (values)
print("Colors:", fruit_colors.values())

# Printing each fruit and its color
for fruit, color in fruit_colors.items():
    print(fruit, "-", color)

# Checking if a fruit is in the dictionary and print its color
search_fruit = "Apple"

if search_fruit in fruit_colors:
    print(search_fruit, "is", fruit_colors[search_fruit])
else:
    print(search_fruit, "not found")