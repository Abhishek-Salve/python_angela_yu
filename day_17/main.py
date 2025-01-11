class User:
    def __init__ (self, user_id, user_name):
        # print("class constructor is executed")
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.id = "001"
# user_1.name = "Bill"
user_1 = User("001", "Angela")
print(user_1.username)
print(user_1.followers)



# user_2 = User()
# user_2.id = "001"
# user_2.name = "Bill"
user_2 = User("002", "Bill")

# if user_1 == user_1:
#     print('ok')
# else:
#     print('nok')
#
# if user_1 == user_2:
#     print('ok')
# else:
#     print('nok')

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
