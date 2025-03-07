import random
import pandas

# sequences --> list, strings
# list comprehension
# 1
numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

# 2
name = "Abhishek"
new_list = [letter for letter in name]
print(new_list)

# 3
square = [x*x for x in range(1,5)]
print(square)

# 4
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
cap_names = [name.upper() for name in names if len(name) > 5]
print(cap_names)

# 5
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

# 6
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num%2==0]
print(result)

#7
file1 = open("file1.txt")
file2 = open("file2.txt")
list_1 = file1.readlines()
list_2 = file2.readlines()
file_1_list = [int(num.strip()) for num in list_1]
file_2_list = [int(num.strip()) for num in list_2]
result = [num for num in file_1_list if num in file_2_list]
print(result)


# dict comprehension
# 1
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {student : random.randint(1, 100) for student in names}
print(student_score)

# 2
student_score = {'Alex': 8, 'Beth': 87, 'Caroline': 37, 'Dave': 87, 'Eleanor': 68, 'Freddie': 81}
# print(student_score.items())
# passed students
passed_students  = {student : score for (student, score) in student_score.items() if score > 60}
print(passed_students)

# 3
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word : len(word) for word in sentence.split(" ")}
print(result)

# 4
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day : celsius * 9/5 + 32 for (day, celsius) in weather_c.items()}
print(weather_f)


student_dict = {
    "student" : ["A", "B", "C", "D"],
    "score" : [67, 34, 65, 34]
}
df = pandas.DataFrame(student_dict)
# print(df)

# loop through dataframes
for (key, value) in student_dict.items():
    print(key)  # prints only column names

for (key, value) in student_dict.items():
    print(value)  # prints values under all columns --> as lists

for (index, row) in df.iterrows():
    print(row.score)

for (index, row) in df.iterrows():
    if row.student == "A":
        print(row.score)