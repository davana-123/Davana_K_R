# Problem 4: Count how many numbers in the list are divisible by 1 to 9

# Given list of numbers
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Create an empty dictionary to store results
result = {}

# Loop from 1 to 9 
for i in range(1, 10):
    count = 0
    for num in numbers:
        if num % i == 0:
            count += 1
    result[i] = count

# Printing the final output dictionary
print(result)

