# Level 1: Greet the user and take their order

# Greet the user
print("Welcome to Tom's Restaurant! Let's take your order.")

# Print a list of starters
starters = ["Bacon", "Dates", "Grapes"]
print("Starters Menu:", starters)

# Take input for the starter
starter_choice = input("Please choose a starter from the menu: ")

# Print a list of mains
mains = ["Pizza", "Masala Curry", "Roast"]
print("Main Course Menu:", mains)

# Take input for the main course
main_choice = input("Please choose a main course from the menu: ")

# Print a list of desserts
desserts = ["Ice Cream", "Brownie", "Cake"]
print("Desserts Menu:", desserts)

# Take input for the dessert
dessert_choice = input("Please choose a dessert from the menu: ")

# Print the user's choices
print("\nYour Order:")
print(f"Starter: {starter_choice}")
print(f"Main Course: {main_choice}")
print(f"Dessert: {dessert_choice}")



