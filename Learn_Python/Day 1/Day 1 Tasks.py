# Tasks: types of data types
from itertools import count

One_third = 1/3

print(One_third)

#Python should show 0.33333333333333

whole = One_third * 3

print(whole)
#python rounds it to 1.0

print(type(whole))

print(type(One_third))

# Task create strings and use quotes appropriately

#Starting code:

# bad_string = 'I said 'Wow!''

#this fails because of the double single quote.
# correct code

bad_string = 'I said "Wow!"'
print(bad_string)

# the best practise when deciding what quotes to use around string in Python is to be continous, pay attention to synatax when using quotes

# Task: Slice strings

# what is string slicing?
#
# write code to do what the comments ask for, write a comment to explain the codes.
print("\n")

Hw = "Hello World!"

print(type(Hw))
print(Hw)

print("\n")

#how many characters does Hw have ?  Ans 12  print(len
print(len(Hw))

#Get the character in the first position in Hw
print(Hw[0])
#Get the last character
print(Hw[11])
# also
#Get the 2nd last character
print(Hw[-2])
#Write a comment to explain what does this do? Ans print Hw string from the 3rd character onwards 3rd character being l
print(Hw[2:])

#write a comment to explain what does this do? Ans print Hw string from the 3rd last character
print(Hw[-3:])

#write a comment to explain what does this do? [start:stop] pastes from the start 0 till 6th character
print(Hw[:5])

#Starts from the second and, stops at the fifth (doesn't include it) ans ell
print(Hw[1:4])

# Use string methods

# Trim spaces off the beginning and end of a string:
str_with_extra_spaces = " extra spaces at the start and end "
#comment
print(str_with_extra_spaces)
print(str_with_extra_spaces.strip())
#comment
print(len(str_with_extra_spaces))
print(len(str_with_extra_spaces.strip()))
#comment removes the blank spaces at the ends of the indexes
print(str_with_extra_spaces.strip(" e"))

# count how many times the substring 'text' occurs within example_text &

example_text = "here's some text with some words of text"

# Count the occurrences of "text"

count = example_text.count("text")

print("The word 'text' occurs", count, "times.")

# Convert to lowercase

lowercase_text = example_text.lower()

print(lowercase_text)

#Convert to uppercase

uppercase_text = example_text.upper()
print(uppercase_text)

#Capitalize the first letter

capitalized_text = example_text.capitalize()

print(capitalized_text)

# Replace "with" with a commar

replaced_text = example_text.replace(" with", ",")

print(replaced_text)

#concatination

# Starting code
x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

# Fixing the concatenation by converting x and y to strings
result = str(x + y) + z
print(result)  # Output: 25.4 there's now a number 25.4 unless we put a space in!

#Convert/ cast this string to an int and float

# Starting code
int_string = "6"

# Convert int_string to an integer
int_value = int(int_string)

# After converting, print its data type to the screen
print("Type after converting to integer:", type(int_value))

# Convert int_string to float
float_value = float(int_string)

# After converting, print its data type to the screen
print("Type after converting to float:", type(float_value))

int_string = "6"

# Convert to an integer and print the value
print(int(int_string))  # Output: 6
# Print the type of the converted integer
print(type(int(int_string)))  # Output: <class 'int'>

# Convert to a float and print the value
print(float(int_string))  # Output: 6.0
# Print the type of the converted float
print(type(float(int_string)))  # Output: <class 'float'>

# Print a line as an F string
name = "Lassie"
years = 7  # Replace '/' with the appropriate value
height_cm = 60.2

# Using an f-string to format and print the output
print(f"{name} is {years} years old and {height_cm} cm tall.")

# Task; finish the guessing game with string slicing

# Guess the word with 4 hints to help
# Rationale: Practice word slicing
# Type of exercise: Finish the code
original_word = "recommendation"
scrambled_word = "eoommandretnic"

# Create the hint slices...
# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]".
# Use the hints below to know what slice is needed
hint1_slice = original_word[4:6]  # The 5th and 6th letters (0-based index: 4th and 5th)
# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]".
# Use the hints below to know what slice is needed
hint2_slice = original_word[-3:]  # The last 3 letters
# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]".
# Use the hints below to know what slice is needed
hint3_slice = original_word[7:10]  # The 8th to 10th letters (0-based index: 7, 8, 9)
# TO DO: On the next line, replace "?" with a string slice in the format "original_word[x:y]".
# Use the hints below to know what slice is needed
hint4_slice = original_word[:2]  # The first two letters

# Game instructions
print("Scrambled word:", scrambled_word)
print("Guess the original word from the scrambled version.")
print("Here are some hints:")
# Hints based on list slicing
print("Hint 1: The 5th and 6th letters are '" + hint1_slice + "'")
print("Hint 2: The last 3 letters are '" + hint2_slice + "'")
print("Hint 3: The 8th to 10th letters are '" + hint3_slice + "'")
print("Hint 4: The first two letters are '" + hint4_slice + "'")
# Game ends here
print("What's your guess?")












