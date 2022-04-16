import os
os.system('color')
from termcolor import colored

from playsound import playsound 


deck = 5*[0] + 4*[1] + 4*[2] + 4*[3] + 4*[4] + 4*[5] + 4*[6] + 4*[7] + 4*[8] + 4*[9] + 4*4*[10]

def get_hand_value(hand):
    num_aces = sum([n for n in hand if n == 1])
    non_ace_total = sum([n for n in hand if n != 1])

    if num_aces > 0:
        if non_ace_total + 11 + (num_aces - 1)*1 <= 21:
            ace_value = 11 + (num_aces - 1)*1
        else:
            ace_value = num_aces*1
    else:
        ace_value = 0
        
    hand_total = non_ace_total + ace_value

    return hand_total


def main():
    print('----------------------------')

    lives = 3
    scores = 0

    arr = [[], [], [], []]
    hold = None

    while len(deck) != 0:
        # Draw next number
        draw = input('Number:').lower()
        draw = 10 if draw == 'q' else int(draw)

        if draw not in deck:
            print('Number has been removed from Deck!')
            continue
        
        # Remove number from deck
        deck.remove(draw)

        # Get next move (col number or Hold)
        move = get_move3(arr, draw, hold, deck)
        if move == 1: playsound('C:\\Users\\admin\Code\\21-cash\\sounds\\one.mp3')
        elif move == 2: playsound('C:\\Users\\admin\Code\\21-cash\\sounds\\two.mp3')
        elif move == 3: playsound('C:\\Users\\admin\Code\\21-cash\\sounds\\three.mp3')
        elif move == 4: playsound('C:\\Users\\admin\Code\\21-cash\\sounds\\four.mp3')

        print('==>', move)

        # if move == 'h':
        #     if hold == None:
        #         hold = draw
        #         print(colored(arr, 'blue'))
        #         print('Hold', hold)
        #         continue
        #     else:
        #         draw = hold
        #         hold = None
        #         print(colored('hold: ' + str(hold) + ', draw: ' + str(draw), 'red'))
        #         # move = get_move3(arr, draw, hold, deck)
        #         move = input('Col:')

        move = int(move)
        bucket = arr[move - 1]

        if draw == 0:
            bucket.clear()
            scores += 250
            print(colored('Destroy!', 'green'))
        elif get_hand_value([*bucket, draw]) == 21:
            bucket.clear()
            scores += 500
            print(colored('Twenty-One!','green'))
        elif len(bucket) == 4 and get_hand_value([*bucket, draw]) <= 21:
            bucket.clear()
            scores += 500
            print(colored('5 Cards!','green'))
        elif  get_hand_value([*bucket, draw]) > 21:
            print(colored('Busted!','green'))
            lives -= 1
            bucket.clear()
        else: 
            bucket.append(draw)
            
        print(colored(arr, 'blue'))
        print('Hold', hold)

        if lives == 0:
            break

        print('----------------------------')

    print('Scores', scores)
    print('Lives', lives)

def get_twenty_count(hand, draw, deck, level):
    if level > 1:
        return 0

    deck_without_jokers = [n for n in deck if n != 0]
    twenty_one_counter = 0
    pair_sum = []
    for n in deck_without_jokers:
        if get_hand_value([*hand, draw, n]) == 21: 
            twenty_one_counter += 1
            pair_sum.append([*hand, draw, n])
        else:
            deck_without_n =  [x for x in deck_without_jokers if n != x]
            twenty_one_counter += get_twenty_count([*hand, draw], n, deck_without_n, level+1)
    # print(pair_sum)

    return twenty_one_counter

hand = [6]
# print(get_twenty_count(hand, 5, deck, 1))

def get_busted_count(hand, draw, deck, level):
    if level > 1:
        return 0

    deck_without_jokers = [n for n in deck if n != 0]
    busted_counter = 0
    pair_sum = []
    for n in deck_without_jokers:
        if get_hand_value([*hand, draw, n]) > 21: 
            busted_counter += 1
            pair_sum.append([*hand, draw, n])
        else:
            deck_without_n =  [x for x in deck_without_jokers if n != x]
            busted_counter += get_busted_count([*hand, draw], n, deck_without_n, level+1)
    # print(level, pair_sum)

    return busted_counter
        

hand = [9,3]
# print(get_busted_count(hand, 2, deck, 1))


def get_move(arr, draw, hold, deck):
    if draw == 0:
        v1 = get_hand_value([*arr[0], draw])
        v2 = get_hand_value([*arr[1], draw])
        v3 = get_hand_value([*arr[2], draw])
        v4 = get_hand_value([*arr[3], draw])
        
        maxV = max(v1,v2,v3,v4)

        if hold == 0:
            if v1 == maxV: return 1
            if v2 == maxV: return 2
            if v3 == maxV: return 3
            if v4 == maxV: return 4
        else:
            if v1 == maxV and v1 > 12: return 1
            if v2 == maxV and v2 > 12: return 2
            if v3 == maxV and v3 > 12: return 3
            if v4 == maxV and v4 > 12: return 4

        return 'h'


    if get_hand_value([*arr[0], draw]) == 21: return 1
    if get_hand_value([*arr[1], draw]) == 21: return 2
    if get_hand_value([*arr[2], draw]) == 21: return 3
    if get_hand_value([*arr[3], draw]) == 21: return 4

    t1 = get_twenty_count(arr[0], draw, deck, 1) 
    t2 = get_twenty_count(arr[1], draw, deck, 1) 
    t3 = get_twenty_count(arr[2], draw, deck, 1)
    t4 = get_twenty_count(arr[3], draw, deck, 1)

    print(t1,t2,t3,t4)
    
    maxT = max(t1,t2,t3,t4)
    
    if maxT == t1: return 1
    if maxT == t2: return 2
    if maxT == t3: return 3
    if maxT == t4: return 4

def get_move2(arr, draw, hold, deck):
    if get_hand_value([*arr[0], draw]) == 21: return 1
    if get_hand_value([*arr[1], draw]) == 21: return 2
    if get_hand_value([*arr[2], draw]) == 21: return 3
    if get_hand_value([*arr[3], draw]) == 21: return 4

    t1 = get_busted_count(arr[0], draw, deck, 1)
    t2 = get_busted_count(arr[1], draw, deck, 1)
    t3 = get_busted_count(arr[2], draw, deck, 1)
    t4 = get_busted_count(arr[3], draw, deck, 1)

    print(t1,t2,t3,t4)
    
    minT = min(t1,t2,t3,t4)
    
    if minT == t1: return 1
    if minT == t2: return 2
    if minT == t3: return 3
    if minT == t4: return 4


def get_move3(arr, draw, hold, deck):
    if get_hand_value([*arr[0], draw]) == 21: return 1
    if get_hand_value([*arr[1], draw]) == 21: return 2
    if get_hand_value([*arr[2], draw]) == 21: return 3
    if get_hand_value([*arr[3], draw]) == 21: return 4

    t1 = get_twenty_count(arr[0], draw, deck, 1)*1.5 - get_busted_count(arr[0], draw, deck, 1)
    t2 = get_twenty_count(arr[1], draw, deck, 1)*1.5 - get_busted_count(arr[1], draw, deck, 1)
    t3 = get_twenty_count(arr[2], draw, deck, 1)*1.5 - get_busted_count(arr[2], draw, deck, 1)
    t4 = get_twenty_count(arr[3], draw, deck, 1)*1.5 - get_busted_count(arr[3], draw, deck, 1)

    if get_hand_value([*arr[0], draw]) > 21: t1 -= 999999
    if get_hand_value([*arr[1], draw]) > 21: t2 -= 999999
    if get_hand_value([*arr[2], draw]) > 21: t3 -= 999999
    if get_hand_value([*arr[3], draw]) > 21: t4 -= 999999

    minT = min(t1,t2,t3,t4)
    maxT = max(t1,t2,t3,t4)

    if draw == 0:
        if minT == t1: return 1
        if minT == t2: return 2
        if minT == t3: return 3
        if minT == t4: return 4
    
    if maxT == t1: return 1
    if maxT == t2: return 2
    if maxT == t3: return 3
    if maxT == t4: return 4


# deck = [10,3,8,10]
# arr = [[],[],[],[]]
# draw = 1

# print('get_move', get_move(arr, draw, None, deck))
# print('get_move2', get_move2(arr, draw, None, deck))
# print('get_move3', get_move3(arr, draw, None, deck))
main()


from itertools import combinations

def sub_set_sum(size, my_array, sub_set_sum):

    sub_sets = []

    for i in range(size+1):
        for my_sub_set in combinations(my_array, i):

            if get_hand_value(my_sub_set) == 21:
                sub_sets.append(list(my_sub_set))
    return sub_sets

# my_size = 6
# my_list = [21, 32, 56, 78, 45, 99, 0]
# print("The list is :")
# print(my_list)
# subset_sum = 53
# print("The result is :")
# sub_set_sum(my_size, my_list, subset_sum)

print(sub_set_sum(7, [1,3,2,5,6,2,2], 9))
print(sub_set_sum(7, [1,2,3,4,5,6], 9))
print(sub_set_sum(7, [10,10,8,3,1,5,7], 9))