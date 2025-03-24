#Write a Python program which accepts the user&#39;s first and last name and print them in
#reverse order with a space between them
rows = 5  # Number of rows in the upper half

# Upper half of the diamond
for i in range(1, rows + 1, 2):
    print(" " * ((rows - i) // 2) + "*" * i)

# Lower half of the diamond
for i in range(rows - 2, 0, -2):
    print(" " * ((rows - i) // 2) + "*" * i)

# Accept user's first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Print in reverse order
print(last_name + " " + first_name)
