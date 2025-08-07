# Problem 2: Print the first 'a' odd numbers


# Get dynamic input from the user
a = int(input("Enter how many odd numbers to print: "))

# Print the first 'a' odd numbers
count = 0
num = 1

while count < a:
    print(num, end=", ")
    num += 2
    count += 1
