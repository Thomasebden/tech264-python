# 2. Create a set named 'fruits' containing "apple", "banana", and "cherry".
fruits = {"apple", "banana", "cherry"}

# 3. Print the set 'fruits'
print("Initial set:", fruits)

# 4. Add "orange" to the set using the .add() method.
fruits.add("orange")

# 5. Print the set 'fruits' to check if "orange" was added.
print("After adding 'orange':", fruits)

# 6. Remove "banana" from the set using the .remove() method.
fruits.remove("banana")

# 7. Print the set 'fruits' to check if "banana" was removed.
print("After removing 'banana':", fruits)

# 8. Attempt to add another "apple" to the set.
fruits.add("apple")

# Observation:
# Adding "apple" again does nothing because sets do not allow duplicates.

# 9. Print the final fruits set.
print("Final set:", fruits)

# 10. Attempt to print the 2nd item in the set.
# Sets are unordered, so there is no concept of a 2nd item.
try:
    print(fruits[1])  # This will raise an error
except TypeError as e:
    print("Error:", e)
    print("Explanation: Sets are unordered, and their elements cannot be accessed by index.")