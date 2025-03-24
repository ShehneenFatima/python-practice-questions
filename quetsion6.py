#Write a Python program to count the number 4 in a given list.
def count_fours(numbers):
    return numbers.count(4)

# Example list
num_list = [1, 4, 6, 4, 7, 4, 9, 4]

# Counting the number of 4s
print("Number of 4s in the list:", count_fours(num_list))
