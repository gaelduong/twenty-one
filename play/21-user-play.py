import os
os.system('color')
from termcolor import colored
import random

import sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.common import get_hand_value

TWENTY_ONE_SCORE = 500
FIVE_CARDS_SCORE = 750
JOKER_DESTROY_SCORE = 250
BASE_BONUS = 300
BUST_FREE_BONUS = 250

def play():
    # 0 = Joker/Wild Card | 1 = Ace | 10 = 10, J, Q, K
    deck = 4*[1] + 4*[2] + 4*[3] + 4*[4] + 4*[5] + 4*[6] + 4*[7] + 4*[8] + 4*[9] + 4*4*[10]

    # Convert 2 random cards into Jokers
    i1, i2 = random.sample(range(0, len(deck)), 2)
    deck[i1] = 0
    deck[i2] = 0
    
    random.shuffle(deck)

    lives = 3
    score = 0
    streaks = -1
    all_buckets = [[], [], [], []]

    while len(deck) > 0 and lives != 0:
        # Draw next card
        card = deck.pop()
        print('Card:', card)

        # Get next move (Col number 1 | 2 | 3 | 4)
        move = int(input('Column:'))

        bucket = all_buckets[move - 1]

        # Joker Destroy
        if card == 0:
            score += JOKER_DESTROY_SCORE
            streaks += 1
            bucket.clear()
            print(colored('Destroy!', 'green'))
            print('+', JOKER_DESTROY_SCORE)
        # 5 Cards and 21
        elif len([*bucket, card]) == 5 and get_hand_value([*bucket, card]) == 21:
            score += FIVE_CARDS_SCORE
            score += TWENTY_ONE_SCORE
            streaks += 1
            bucket.clear()
            print(colored('5 Cards AND Twenty-One!','green'))
            print('+', FIVE_CARDS_SCORE)
            print('+', TWENTY_ONE_SCORE)
        # 5 Cards < 21
        elif len([*bucket, card]) == 5 and get_hand_value([*bucket, card]) < 21:
            score += FIVE_CARDS_SCORE
            streaks += 1
            bucket.clear()
            print(colored('5 Cards!','green'))
            print('+', FIVE_CARDS_SCORE)
        # 21 with less than 5 cards
        elif get_hand_value([*bucket, card]) == 21:
            score += TWENTY_ONE_SCORE
            streaks += 1
            bucket.clear()
            print(colored('Twenty-One!','green'))
            print('+', TWENTY_ONE_SCORE)
        # Busted
        elif get_hand_value([*bucket, card]) > 21:
            print(colored('Busted!','green'))
            lives -= 1
            bucket.clear()
        # None of the above
        else: 
            bucket.append(card)
            streaks = -1

        bonus = streaks * BASE_BONUS
        if bonus > 0:
            score += bonus
            print('Bonus: +', bonus)
            
        print(colored(all_buckets, 'blue'))
        print(colored('Deck','red'), colored(deck, 'red'))
        print('Score:', score)
        print('----------------------------')

    # Bonus +250 if bust free
    bust_free_bonus = BUST_FREE_BONUS if lives == 3 else 0
    total_score = score + bust_free_bonus

    # Result
    print('----------Result------------')
    print('Lives:', lives)
    print('Score:', score)
    print('Bonus (bust free):', bust_free_bonus)
    print('Total score:', total_score)
    return total_score

