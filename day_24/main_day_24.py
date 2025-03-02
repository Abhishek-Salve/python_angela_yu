# # How to read a file
# file = open(file="my_file.txt")
# file_contents = file.read()
# print(file_contents)
# file.close()

# # # How to read a file - using "with" keyword
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # How to write  to file
# with open("my_file.txt", "a") as file:
#     file.write("New text 2")
#     # contents = file.read()
#     # print(contents)

# Absolute path
FILE_PATH = r'C:/Users/salve/Desktop/my_file.txt'
with open(FILE_PATH) as file:
    contents = file.read()
    print(contents)

