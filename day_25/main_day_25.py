# with open("weather_data.csv") as test_file:
#     data = test_file.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)  # data is csv reader object
#     temperatures = []
#     for row in data:
#         if not row[1] == "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#
# print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()  # converts the column data into a iterable list
# print(temp_list)

# sum = 0
# for temp in temp_list:
#     sum += temp
# average = sum/len(temp_list)
# print(average)

# # Average using sum()
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# # Average using panda series mean API
# avr = data["temp"].mean()
# print(avr)
#
# # Max value in column using series max API
# max = data["temp"].max()
# print(max)


# # Find row of max temp
# row = data["temp"].idxmax()
# print(data[data.day == data["day"][row]])
# # their method
# print(data[data.temp == data.temp.max()])

# Find mondays temp
monday = data[data.day == "Monday"]
# print(monday)
print(monday.condition)
print(monday.condition[0])
print(type(monday.condition[0]))
print(monday.temp)
print(monday.temp[0])
print(type(monday.temp[0]))
# print((monday.temp[0] * 9/5)+32)

# # Create Dataframe from scratch
# data_dict = {
#     "students" : ["K", "A", "S"],
#     "scores" : [90, 45, 78]
# }
#
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_csv.csv")


# # Process the squirrel CSV
# csv_filepath = '2018_Central_Park_Squirrel_Census_Squirrel_Data.csv'
# data = pandas.read_csv(csv_filepath)
# colours = data["Primary Fur Color"]
#
# gray, black, cinnamon = 0, 0, 0
# for colour in colours:
#     if colour == 'Gray':
#         gray += 1
#     elif colour == 'Black':
#         black += 1
#     elif colour == 'Cinnamon':
#         cinnamon += 1
#     else:
#         pass
#
# print(gray, cinnamon, black)
#
# grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels, cinnamon_squirrels, black_squirrels)
#
# # create dict
# squirrel_dict = {
#     "fur color" : ["grey", "cinnamon", "black"],
#     "count" : [gray, cinnamon, black]
# }
#
# squirrel_data = pandas.DataFrame(squirrel_dict)
# print(squirrel_data)
