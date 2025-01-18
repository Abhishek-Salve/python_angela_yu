# # Python program to find GCD of two numbers
#
#
# # Function to find gcd of two numbers
# def gcd(a, b):
#
#     # Find minimum of a and b
#     result = min(a, b)
#
#     while result:
#         if a % result == 0 and b % result == 0:
#             break
#         result -= 1
#
#     # Return the gcd of a and b
#     return result
#
#
# # Driver Code
# if __name__ == '__main__':
#     a = 98
#     b = 56
#     print(f"GCD of {a} and {b} is {gcd(a, b)}")

import random

for i in range(50):
    print(f'{random.randint(1, 100)},', end=' ')

print('')

list_1 = [18, 72, 50, 5, 52, 1, 96, 48, 82, 83, 96, 85, 54, 8, 99, 37, 16, 72, 65, 98, 10, 98, 3, 97, 72, 59, 17, 61, 74, 62, 60, 60, 24, 35, 17, 35, 27, 44, 1, 47, 98, 33, 35, 75, 10, 13, 98, 62, 52, 41]
list_1.sort()
print(list_1)

list_2 = [1, 2, 3, 5, 8, 10, 11, 13, 16, 17, 18, 19, 24, 27, 33, 35, 36, 37, 41, 44, 47, 48, 50, 52, 53, 54, 59, 60, 61, 62, 64, 65, 72, 73, 74, 75, 82, 83, 85, 96, 97, 98, 99]
print(list_2.index(36))


# Define the size of the array and the range of numbers
array_size = 20
number_range = 100  # Range from 1 to 100

# Generate an array of non-repeating elements
non_repeating_array = random.sample(range(1, number_range + 1), array_size)

# Print the result
print(non_repeating_array)
print(len(non_repeating_array))