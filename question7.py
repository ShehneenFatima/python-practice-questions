#7. Print table of 24, 50 and 29 using loop.
numbers = [24, 50, 29]

for num in numbers:
    print(f"Multiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print()  # Prints a blank line for better readability

