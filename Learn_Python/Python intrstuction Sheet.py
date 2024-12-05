#1. Basic Syntax & Print Statements
# Print statement
print("Hello, World!")  # Outputs: Hello, World!

# Assigning variables
x = 10  # Integer
name = "John"  # String

# f-string for formatting strings
age = 25
print(f"Name: {name}, Age: {age}")

#2. Data Types
# Numbers
x = 10  # int
y = 3.14  # float

# Strings
greeting = "Hello"

# Lists
fruits = ["apple", "banana", "cherry"]

# Tuples (immutable)
coordinates = (10, 20)

# Sets (unique, unordered)
colors = {"red", "green", "blue"}

# Dictionaries (key-value pairs)
person = {"name": "Alice", "age": 30, "city": "New York"}

# Booleans
is_active = True
is_completed = False

#3. Working with Sets
# Creating a set
fruits = {"apple", "banana", "cherry"}

# Adding an element to a set
fruits.add("orange")

# Removing an element from a set
fruits.remove("banana")

# Iterating through a set
for fruit in fruits:
    print(fruit)

#3. Working with Lists

# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Outputs: apple

# Adding elements
fruits.append("orange")  # Adds 'orange' to the end

# Removing elements
fruits.remove("banana")  # Removes 'banana'

# Iterating over a list
for fruit in fruits:
    print(fruit)

#4. Working with Tuples
# Creating a tuple
coordinates = (10, 20)

# Accessing tuple elements
print(coordinates[0])  # Outputs: 10

#5. Working with Frozen Sets
# Creating a frozen set
frozen_set = frozenset(["apple", "banana", "cherry"])

# Attempt to add an element (will raise an error)
# frozen_set.add("orange")  # Error: 'frozenset' object has no attribute 'add'

#6. Creating a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing values
print(person["name"])  # Outputs: Alice

# Adding key-value pairs
person["gender"] = "Female"

# Removing key-value pairs
del person["age"]

# Iterating over dictionary
for key, value in person.items():
    print(f"{key}: {value}")

#7. Loops
# For loop
for i in range(5):
    print(i)  # Outputs 0, 1, 2, 3, 4

# While loop
x = 0
while x < 5:
    print(x)
    x += 1  # Increment

#8. Conditional Statements
# If-elif-else
age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are an adult.")
else:
    print("You are older than 18.")

# 9. Breaking and Continuing Loops
# Break out of loop
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

# Continue the loop
for i in range(5):
    if i == 3:
        continue  # Skip the rest of the loop when i is 3
    print(i)

