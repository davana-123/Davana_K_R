# Problem 3: Print odd numbers up to 'a' count


# Getting input from the user
a = int(input("Enter a number: "))

# If 'a' is even, reduce it by 1
if a % 2 == 0:
    a = a - 1

# Initialize counter and number
count = 0
num = 1

# Print 'a' odd numbers
while count < a:
    print(num, end=", ")
    num += 2
    count += 1
