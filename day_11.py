# Capstone project - Blackjack
# More than 21 - Bust
# 2-10 --> Face Value
# Jack, Queen, King --> each count as 10
# Ace can count as 1 or 11 - based on if you are over or under
# if under 17 --> dealer has to pull a card

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
suits = ['Spades', 'Diamonds', 'Clover', 'Hearts']
deck = []

for suit in suits:
    for card in cards:
        curr_card = str(card) + ' ' + suit
        deck.append(curr_card)

# print(deck)
game_over = False
player_cards = []
dealer_cards = []

def card_value(card_list):
    total_value = 0
    for card in card_list:
        total_value += int(card.strip().split(' ')[0])
    return total_value


while not game_over:
    for cards in range(2):
        # Select one card for player
        player_card = random.choice(deck)
        deck.remove(player_card)
        player_cards.append(player_card)

        # Select one card for dealer
        dealer_card = random.choice(deck)
        deck.remove(dealer_card)
        dealer_cards.append(dealer_card)

    # Reveal cards - 2 player, 1 dealer
    print('Players cards are: ', end=' ')
    for card in player_cards:
        print(card, end=', ')
    print('\n', end='')

    print('Dealer card is: ', end = '')
    print(dealer_cards[0])
    print('\n', end='')

    print(f"Player total card value = {card_value(player_cards)}")

    # In below while loop, player decides if they want to draw anymore cards
    draw_stop = False
    while not draw_stop:
        draw_next = input("Player, do you want to draw next card (y/n) ?: ")
        if draw_next == 'y':
            # Select one card for player
            player_card = random.choice(deck)
            deck.remove(player_card)
            player_cards.append(player_card)

            print('Players cards are: ', end=' ')
            for card in player_cards:
                print(card, end=', ')
            print('\n', end='')
            print(f"Player total card value = {card_value(player_cards)}")
            if card_value(player_cards) > 21:
                print("\nPlayer Bust ! Game over ! Player loses")
                game_over = True
                exit()

        elif draw_next == 'n':
            print('Player has decided not to draw any more cards')
            draw_stop = True
        else:
            print('Incorrect input, you are not to draw any more cards')
            draw_stop = True

    # Once player has stopped drawing - reveal dealer cards
    dealer_card_value = card_value(dealer_cards)
    print(f"\nDealer total card value = {dealer_card_value}")
    print('\n', end='')

    while dealer_card_value < 17:
        print("Dealer will now draw")
        # Select one card for dealer
        dealer_card = random.choice(deck)
        deck.remove(dealer_card)
        dealer_cards.append(dealer_card)

        print('Dealer cards are: ', end=' ')
        for card in dealer_cards:
            print(card, end=', ')
        print('\n', end='')

        dealer_card_value = card_value(dealer_cards)
        if dealer_card_value > 21:
            print("Dealer Bust ! Game over ! Player wins")
            game_over = True
            exit()

    # Compare cards values - decide win/bust
    print("Compare Player and Dealer hands")
    print(f"Dealer total card value = {dealer_card_value}")
    print(f"Player total card value = {card_value(player_cards)}")

    if card_value(dealer_cards) > card_value(player_cards):
        print("Dealer Wins !")
    elif card_value(dealer_cards) < card_value(player_cards):
        print("Player Wins !")
    elif card_value(dealer_cards) == card_value(player_cards):
        print("Its a Draw !")
    else:
        print("Unexpected comparison, developer needs to check code")

    game_over = True


# print(player_cards)
# print(dealer_cards)
