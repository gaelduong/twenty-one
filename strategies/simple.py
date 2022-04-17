from utils.common import get_hand_value

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
        

# hand = [9,3]
# print(get_busted_count(hand, 2, deck, 1))

def get_move(arr, draw, hold, deck):
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