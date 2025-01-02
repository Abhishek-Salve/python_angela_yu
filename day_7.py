# Hangman game
import random

hang_stages = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
  |   |
 /    |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
  |   |
 / \\  |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
 /|   |
 / \\  |
      |
=========
    ''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
    '''
]



word_list = ['mixture', 'exhibition', 'resignation', 'straighten', 'empirical', 'organisation']
random_word = random.choice(word_list)
print(random_word)

blank_string = ''
for letter in random_word:
    blank_string += '_'

# print(blank_string)
guess_string = blank_string
# print(guess_string)
# index = 3
# guess_string = guess_string[:index] + 'F' + guess_string[index+1:]
# print(guess_string)
#
# temp_list = list(guess_string)
# temp_list[index] = 'a'
# guess_string = "".join(temp_list)
# print(guess_string)


game_over = False
life_used = 0

while not game_over:
    temp_string = ''
    letter_guess = input("Guess a letter from the word :\n").lower()
    # print(letter_guess)

    if letter_guess not in random_word:
        life_used += 1

    for num, letter in enumerate(guess_string):
        if letter_guess == random_word[num]:
            temp_string += random_word[num]
        elif letter != '_':
            temp_string += guess_string[num]
        else:
            temp_string += '_'

    guess_string = temp_string
    print(guess_string)
    print(hang_stages[life_used])

    if "_" not in guess_string:
        print("All letters have been guessed correctly ! You win !")
        game_over = True

    if life_used == 6:
        print("Man hangs ! You lose !")
        game_over = True
