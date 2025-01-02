import random
from resources.higher_or_lower_game_data import data

# Print art

celeb_list = data

# Count score of player
player_score_curr = 0
player_highest_score = 0
game_iter = 0

# Choose 2 celebs to compare
# Remove celeb from list after compare ? --> yes
def choose_celeb():
    choice = random.choice(celeb_list)
    celeb_list.remove(choice)
    return choice


# Loop until player loses
def play_game(celeb=None):
    if celeb is None:
        celeb_1 = choose_celeb()
    else:
        celeb_1 = celeb

    celeb_2 = choose_celeb()

    print("******************************************")
    print('Compare follower count between')
    print(f"A is : {celeb_1['name']},who/which is {celeb_1["description"]}, from {celeb_1['country']}.")
    print('______ VS. ______ ')
    print(f"B is : {celeb_2['name']},who/which is {celeb_2["description"]}, from {celeb_2['country']}.")
    user_selection = input("Who has more followers? Type 'A' or 'B': ").upper()

    celeb_1_follows = celeb_1["follower_count"]
    celeb_2_follows = celeb_2["follower_count"]

    if user_selection == 'A':
        if celeb_2_follows > celeb_1_follows:
            print(f"Wrong ! {celeb_2['name']} has more follows")
            return 0, {}
        else:
            print(f"Right ! {celeb_1['name']} has more follows")
            return 1, celeb_2
    elif user_selection == 'B':
        if celeb_1_follows > celeb_2_follows:
            print(f"Wrong ! {celeb_1['name']} has more follows")
            return 0, {}
        else:
            print(f"Right ! {celeb_2['name']} has more follows")
            return 1, celeb_2


game_over = False
celeb_pass = None
while not game_over:
    result = play_game(celeb=celeb_pass)
    # print(result, type(result))
    # print(celeb_return, type(celeb_return))

    game_iter += 1

    if result[0] == 1:
        player_score_curr += 1
        print(f"Current player score is {player_score_curr}")
        if player_score_curr > player_highest_score:
            player_highest_score = player_score_curr
            celeb_pass = result[1]

    if result[0] == 0:
        print(f"Current player score was {player_score_curr}")
        game_over = True



