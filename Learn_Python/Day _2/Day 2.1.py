#Working with a list

### "collections" Python topic

# Step 1: Create a list called 'shopping_list'
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

# Step 2: Print the list to the screen
print("Shopping List:", shopping_list)

# Step 3: Print the data type of 'shopping_list'
print("Data Type:", type(shopping_list))

# Step 4: Print the first item in the list
print("First Item:", shopping_list[0])

# Step 5: Print the last item in the list
print("Last Item:", shopping_list[-1])

# Step 6: Change the second item ('bread') to 'rice' and print it
shopping_list[1] = "rice"
print("Updated Second Item:", shopping_list[1])

# Step 7: Add the item 'carrots' using a list method and check the length
shopping_list.append("carrots")
print("List After Adding 'carrots':", shopping_list)
print("Length of List:", len(shopping_list))

# Step 8: Add another list ['toffee', 'coffee'] to 'shopping_list' in one go
shopping_list.extend(["toffee", "coffee"])
print("List After Adding 'toffee' and 'coffee':", shopping_list)

# Step 9: Remove 'bananas' from the list and check
shopping_list.remove("bananas")
print("List After Removing 'bananas':", shopping_list)

# Step 10: Remove the last item ('coffee') using the pop method and check
shopping_list.pop()
print("List After Removing the Last Item:", shopping_list)

#Task 2 Mix all the data about a user into a list

# Step 1: Ask the user for their name, age, and DOB
name = "Thomas"
age = "21"
dob = "24.01.2003"

# Step 2: Mix the name, age, and DOB into one list 'user_details_list'   when you make the list, convert the strings to interger
user_details_list = [name, int(age), dob]
#age = 21 jacks way

# Step 3: Print the user's name, age, and DOB from the list
print("User Details:")
print("Name:", user_details_list[0])
print("Age:", user_details_list[1])
print("Date of Birth:", user_details_list[2])

# Step 4: Check if age is an integer; convert if necessary
print("Data Type:", type(user_details_list[1]))

#this command will show the data type of the second item in the list

    # Convert age to integer
print("Age after ensuring it is an integer:", user_details_list[1])

# Step 5: Ask the user for their height in cm and save it to the variable 'height'
height = float(input("Enter your height in cm: "))

# Step 6: Save 'height' as a float in the list and print the height from the list
user_details_list.append(height)
print("Height added to the list:", user_details_list[-1])




# test you can slice lists

# Starting code
mixture = [1, 2, 3, "one", "two", "three"]
print("Original list:", mixture)

# 1. Returns the 2nd and 3rd items in the list
second_and_third = mixture[1:3]
print("2nd and 3rd items:", second_and_third)  # Output: [2, 3]

# 2. Returns every second item in the list
every_second_item = mixture[::2]
print("Every second item:", every_second_item)  # Output: [1, 3, 'two']

# 3. Start at the last item, stop at the 3rd last item, and step in reverse order
reverse_slice = mixture[-1:-4:-1]
print("Reverse slice from last to 3rd last:", reverse_slice)  # Output: ['three', 'two']

#learn tuples - finish the "Stranded on desert island" game

# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You can take only THREE items.")

# User input for essential items
essential_item1 = input("What essential item would you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")

outfit = input("what outfit would you take?")

# Save the items as a tuple
essentials_tuple = (essential_item1, essential_item2, essential_item3, outfit)


# Print the tuple
print('Here are your items as a tuple:', essentials_tuple)
print('')

# User input for the 4th item
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")

# Adding the 4th item to the tuple (since tuples are immutable, we create a new tuple)
essentials_tuple = essentials_tuple + (essential_item4,)

# Print the updated tuple
print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)















