import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)
# print(df.iterrows())

# for index, value in df.iterrows():
#     print(value)

nato_dict = {row.letter : row.code for (index, row) in df.iterrows()}
# print(nato_dict)
# print(nato_dict['A'])

user_name = input("Enter a name : ")
# print(f'User has input --> {user_name}')

print('NATO phonetic is as follows :')
# name_dict = [char for char in user_name]
# # print(name_dict)
#
# user_nato_list = []
# for char in name_dict:
#     char = char.capitalize()
#     user_nato_list.append(nato_dict[char])
#
# print(user_nato_list)

output = [nato_dict[letter] for letter in user_name.upper()]
print(output)

