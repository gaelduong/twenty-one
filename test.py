from itertools import combinations

def get_card_value(formatted_card):
    #10H => 10
    if formatted_card[0] in ['J','Q','K']:
        return 10
    return int(formatted_card[:-1])

def get_card_suit(formatted_card):
    #10H => H
    return int(formatted_card[-1])

def get_hand_value(hand):
    num_aces = sum([get_card_value(n) for n in hand if get_card_value(n) == 1])
    non_ace_total = sum([get_card_value(n) for n in hand if get_card_value(n) != 1])
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

def generate_edges(tuples):
    edges = []
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            tup = tuples[i]
            tup2 = tuples[j]
            if len([card for card in tup if card in tup2]) > 0:
                edges.append((tup,tup2))
    return edges

def get_maximum_number_of_sub_set(sub_sets):
    all_combos = []
    for sub_set in sub_sets:
        distinct_sub_sets = [sub_set]
        for sub_set_2 in sub_sets:
            if len([x for x in sub_set if x in sub_set_2]) == 0:
                distinct_sub_sets.append(sub_set_2)
        all_combos.append(distinct_sub_sets)
    
    return max(all_combos,key=len)


len4count = 0

for i in range(1):

    suits = ["H","D","C","S"]
    numbers = [1,2,3,4,5,6,7,8,9,10,'J','Q','K']
    numbers = [1,2,3,4,5,6,7,8,9,10]

    deck = [str(number) + suit for suit in suits for number in numbers]
    # print(deck)

    import random
    random.shuffle(deck)
    hand = deck[:18]
    hand = ['7H', '6H', '8D', 'QH', '3H', '5C', 'QD', '4D', '2C', '6S', '2D', '5H', '3S']
    hand = ['1H', '2H', '3D', '4H', '5H', '6C', '7D', '8D', '9C', '10S', 'JD', 'QH', 'KS']
    # hand = ['10H','10C','8H','3C','1H']
    print(hand)
    print(len(hand))
    # print(deck)

    c = sub_set_sum(4, deck, 21)
    for i in range(len(c)):
        for j in range(len(c[i])):
            c[i][j] = int(c[i][j][:-1])

    import itertools
    c.sort()
    c = list(k for k,_ in itertools.groupby(c))
    print(c)
    print(len(c))
    # s = [s]
    # s = generate_edges(s)
    # print(s)
    # a = get_maximum_number_of_sub_set(s)


    # import networkx
    # import matplotlib.pyplot as plt
    # w = 4
    # h = 3
    # d = 70
    # plt.figure(figsize=(w, h), dpi=d)
    # G = networkx.Graph()
    # G.add_edges_from([(one,two), (one,three), (two,three), (one,four), (one,five), (two,four), (three,five), (four,five)])
    # G.add_edges_from(s)

    # labels = [1, 2, 3, 4, 5]
    # networkx.draw_networkx(G, with_labels=labels)
    # plt.axis ("off")
    # plt.show()
    # plt.savefig("out.png")
    # maxIS=networkx.algorithms.approximation.clique.maximum_independent_set(G)
    # print(maxIS)
    # if len(maxIS) <= 4: len4count += 1

print(len4count)