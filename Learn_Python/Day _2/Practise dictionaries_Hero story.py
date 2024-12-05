# Define the story1 dictionary
story1 = {
    "start": "Once upon a time, a keyboard warrior named Thomas set out on a journey to learn Python.",
    "middle": "After braving treacherous mountains and cunning traps, Thomas discovered a program hidden in Pycharm.",
    "end": "With courage and wit, Thomas learned the ancient skill and returned home as a hero."
}

# Print the entire dictionary
print("The entire dictionary:")
print(story1)

# Print the type of the dictionary
print("\nThe type of the dictionary:")
print(type(story1))

# Print only the keys
print("\nThe keys in the dictionary:")
print(story1.keys())

# Print only the values
print("\nThe values in the dictionary:")
print(story1.values())

# Print individual values using the keys
print("\nAccessing values using keys:")
print("Start:", story1["start"])
print("Middle:", story1["middle"])
print("End:", story1["end"])

# Add a new key:value pair for the character
story1["character"] = "Tom"

# Print the end of the story with the character's name
print("\nThe end of the story:")
print(f"The end. I hope you enjoyed the story about {story1['character']}!")