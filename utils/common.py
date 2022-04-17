# A = 1 or 11
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