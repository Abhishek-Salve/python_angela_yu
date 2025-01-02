# Number guessing game
import random

print("Welcome to Number Guessing Game !!")

# Choose a random number between 1-100
random_number = random.randint(1, 100)
print(f"The random number is {random_number}")

# Choose mode "easy" / "hard"
mode = input("Player can choose the modes (easy/hard) : ").lower()
if mode == "easy":
    chances = 10
elif mode == "hard":
    chances = 5
else:
    chances = 0
    print("Enter keywords either 'easy' OR 'hard' ")
    exit()

print(f"Player has {chances} chances to guess the number !\n")


while chances != 0:
    player_guess = int(input("What is your guess ? :"))
    if type(player_guess) != type(1):
        print(f"Guess a number between 1-100, you entered {player_guess} instead")
    else:
        if player_guess == random_number:
            print(f"You Win! The random number is {random_number}")
            exit()
        elif player_guess < random_number:
            print("Your guess is low")
        elif player_guess > random_number:
            print("Your guess is high")
        else:
            print("unexpected code branch executed, contact developer")

    chances -= 1
    if chances <= 3:
        print(f"Chances remaining : {chances} !!")


