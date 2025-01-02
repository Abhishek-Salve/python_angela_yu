import random

# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit_name in fruits:
#     print(fruit_name)

# marks = []

# for i in range(100):
#     marks.append(random.randint(50, 100))
# print(marks)


# marks = [85, 92, 50, 79, 54, 61, 90, 77, 71, 95, 73, 66, 59, 51, 68, 80, 88, 57, 63, 90, 63, 51, 94, 55, 61, 87, 92, 55, 96, 91, 74, 67, 52, 80, 53, 51, 73, 58, 82, 98, 55, 90, 55, 94, 53, 82, 66, 50, 94, 62, 95, 92, 91, 84, 87, 68, 70, 76, 83, 92, 73, 55, 94, 53, 93, 94, 52, 94, 82, 79, 62, 93, 66, 56, 62, 62, 94, 69, 56, 53, 77, 94, 67, 73, 96, 94, 52, 79, 55, 56, 69, 91, 82, 76, 71, 64, 78, 96, 90]
# total_marks = 0
# max_score = 0
#
# for score in marks:
#     total_marks += score
#     if max_score < score:
#         max_score = score
#
# print(total_marks)
# print(max_score)

# for number in range(11):
#     print(number)

# total = 0
#
# for num in range(1, 101):
#     total += num
#
# print(total)

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

my_list = []

for num in range(10):
    # my_list.append(num)
    my_list += str(num)

print(my_list) 
