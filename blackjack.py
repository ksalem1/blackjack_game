############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
import os

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
    '''Take a list of cards and return the score calculated from the cards'''
    # Check for a blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        #cards.remove(11)
        #cards.append(1)
        cards = [1 if x == 11 else x for x in cards]
    return sum(cards)


def compare(us,ds):
    #if us > 21 and ds > 21:
    #    return 'You went over. You lose'

    if us == ds:
        return "It's a draw"
    elif ds == 0:
        return 'You lose, dealer has a blackjack'
    elif us == 0:
        return 'You win, blackjack!'
    elif us > 21:
        return 'You went over. You lose'
    elif ds > 21:
        return 'You win! Dealer went over'
    elif us > ds:
        return 'You win!'
    else:
        return 'You lose'

def play_game():
    uc = []
    dc = []
    for i in range(2):
        uc.append(deal_card())
        dc.append(deal_card())

    is_game_over = False

    while not is_game_over:
        us = calculate_score(uc)
        ds = calculate_score(dc)
        print(uc, dc)
        print(us, ds)


        if us == 0 or ds == 0 or us > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to draw another card, or 'n' to pass:").lower()
            if user_deal == 'y':
                uc.append(deal_card())
            else:
                is_game_over = True

    while ds != 0 and ds <17:
        dc.append(deal_card())
        ds = calculate_score(dc)

    print(f"Final hand is {uc}. Dealer final hand is {dc}")
    print(compare(us,ds))

while input('Do you want to play a game of Blackjack? Type "y" for yes: ').lower() == 'y':
    os.system('cls')
    play_game()








