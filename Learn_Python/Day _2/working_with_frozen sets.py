# 1. Create a frozen set named frozen_set containing elements "hello", "world"
frozen_set = frozenset(["hello", "world"])

# 2. add "!" to frozen_set. What happens? ("!")

print( "Error" )
print("Explanation: Frozen sets are immutable, so you cannot add elements to them.")

# 3. Create a normal set named normal_set containing elements "let's", "learn".
normal_set = {"let's", "learn"}

# 4. Try to add frozen_set to normal_set.
try:
    normal_set.add(frozen_set)
    print("Frozen set successfully added to normal set.")
except TypeError as e:
    print("Error:", e)

# 5. Print normal_set.
print("normal_set:", normal_set)

# 6. Run the script multiple times to observe the order of items in normal_set.
# The order may change because sets in Python are unordered collections.
# Run this script multiple times to notice the behavior.

# 7. Explanation of differences between frozen sets and normal sets.
print("""
Differences Between Frozen Sets and Normal Sets:
1. Frozen sets are immutable, meaning their elements cannot be changed after creation.
   Normal sets are mutable, allowing elements to be added or removed.
2. Frozen sets can be used as keys in dictionaries or elements in other sets because they are hashable.
   Normal sets are not hashable, so they cannot be used in these contexts.
""")