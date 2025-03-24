#Write a Python program to get the difference between a given number and 17, if the
#number is greater than 17 return double the absolute difference.
def difference_from_17(n):
    difference = abs(n - 17)
    if n > 17:
        return 2 * difference
    return difference

# Test cases
num = int(input("Enter a number: "))
print("Result:", difference_from_17(num))

