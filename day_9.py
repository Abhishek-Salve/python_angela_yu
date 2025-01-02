# Dictionaries and Nesting

# empty_dict = {}
# empty_dict["key_1"] = "w"
# print(empty_dict)
# print(empty_dict["key_1"])
# empty_dict["key_1"] = "a"
# empty_dict["key_2"] = "b"
# empty_dict["key_3"] = "c"
# print(empty_dict)
#
# for item in empty_dict:
#     print(item, empty_dict[item])

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades = {}
#
# for student in student_scores:
#     score = student_scores[student]
#     if 91 < score < 100:
#         student_grades[student] = "Outstanding"
#     elif 81 < score < 90:
#         student_grades[student] = "Exceeds Expectations"
#     elif 71 < score < 80:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)


# capitals = {
#     "France" : "Paris",
#     "Germany" : "Berlin",
# }
#
# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany" : ["Stuttgart", "Berlin"],
# }
#
# print(travel_log["France"][1])
#
# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

auction_dict = {}
auction_done = False

while not auction_done:
    bidder_name = input("What is your name?: ")
    bid_value = int(input("What is your bid value: "))
    auction_dict[bidder_name] = bid_value

    continue_bid = input("Do you want to continue? (y/n): ")
    if continue_bid == 'n':
        auction_done =True
    else:
        print("\n" * 100)
        # continue


auction_winner_bid = 0
auction_winner_name = ''
for auctioner in auction_dict:
    if auction_dict[auctioner] > auction_winner_bid:
        auction_winner_name = auctioner
        auction_winner_bid = auction_dict[auctioner]
    else:
        continue

print(f"*** {auction_winner_name} has won the bid with value {auction_winner_bid} ***")
