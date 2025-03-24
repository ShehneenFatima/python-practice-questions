#Write a Python program to calculate the sum of three given numbers, if the values are
#equal then return thrice of their sum
def sum_or_triple(a, b, c):
    total = a + b + c
    if a == b == c:
        return 3 * total
    return total

# Test cases
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("Result:", sum_or_triple(num1, num2, num3))
