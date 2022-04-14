from itertools import combinations

def get_hand_value(hand):
    num_aces = sum([n['v'] for n in hand if n['v'] == 1])
    non_ace_total = sum([n['v'] for n in hand if n['v'] != 1])

    if num_aces > 0:
        if non_ace_total + 11 + (num_aces - 1)*1 <= 21:
            ace_value = 11 + (num_aces - 1)*1
        else:
            ace_value = num_aces*1
    else:
        ace_value = 0
        
    hand_total = non_ace_total + ace_value

    return hand_total

def sub_set_sum(size, my_array, sub_set_sum):

    sub_sets = []

    for i in range(size+1):
        for my_sub_set in combinations(my_array, i):

            if get_hand_value(my_sub_set) == sub_set_sum:
                sub_sets.append(list(my_sub_set))
    return sub_sets

def get_maximum_number_of_sub_set(sub_sets):
    all_combos = []
    for sub_set in sub_sets:
        distinct_sub_sets = [sub_set]
        for sub_set_2 in sub_sets:
            if len([x for x in sub_set if x in sub_set_2]) == 0:
                distinct_sub_sets.append(sub_set_2)
        all_combos.append(distinct_sub_sets)
    
    return max(all_combos,key=len)


suits = ["H", "D", "C", "S"]

numbers = [1,2,3,4,5,6,7,8,9,10,10,10,10]

deck = [{'v': number,'s': suit}
        for suit in suits for number in numbers]
# print(deck)


hand = [
    {
        "v": 10,
        "s": 'H'
    },
    {
        "v": 10,
        "s": 'C'
    },
    {
        "v": 8,
        "s": 'H'
    },
    {
        "v": 3,
        "s": 'C'
    },
    {
        "v": 1,
        "s": 'H'
    },
]

# print(get_hand_value(deck))
import random
random.shuffle(deck)
print(deck)

s = sub_set_sum(7, deck[:len(deck)//4], 21)
# s = sub_set_sum(7, hand, 21)
a = get_maximum_number_of_sub_set(s)

# print(a)
a = list(map(lambda lst: list(map( lambda t: str(t['v'])+t['s'], lst)), a))
print(a)
print(len(a))


