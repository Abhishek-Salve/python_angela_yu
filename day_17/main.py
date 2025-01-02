class User:
    def __init__ (self):
        print("class constructor is executed")
        

user_1 = User()
user_1.id = "001"
user_1.name = "Bill"

# print(user_1.name)

user_2 = User()
user_2.id = "001"
user_2.name = "Bill"

if user_1 == user_1:
    print('ok')
else:
    print('nok')

if user_1 == user_2:
    print('ok')
else:
    print('nok')