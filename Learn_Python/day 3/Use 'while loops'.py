# Initialize x with the value of 0
x = 0

# Create a while loop that continues as long as x is less than 10
while x < 10:
    # Print the value of x using an f-string
    print(f"x -> {x}")

    # Increment x by 1 I needed to research to find this
    x += 1

# 4.     while x < 10:
#           ^
# NameError: name 'x' is not defined, when you do not increment x the code will not run

while x < 10:
    print(f"x -> {x}")

    x += 1

