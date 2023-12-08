import functools

# Read data
#data_source = 'day7/example_data.txt'
data_source = 'day7/data.txt'

with open(data_source) as f:
    lines = f.read().split()

hands = lines[0::2]
bids = [eval(i) for i in lines[1::2]]

data = [([*hand], string) for hand, string in 
    zip(hands, bids)]

hand_types = ["high card", "one pair", "two pair", "three", "full house", "four", "five"]

hand_split = {key: [] for key in hand_types}

# Classify all the hands, and put the in the dictionary

for item in data:
    unique_cards = list(set(item[0]))
    
    match len(unique_cards):
        case 1:
            hand_split["five"].append(item)
        case 2:
            # Can be full house or four of a kind
            if (item[0].count(item[0][0]) == 4) or (item[0].count(item[0][0]) == 1):
                hand_split["four"].append(item)
            else:
                hand_split["full house"].append(item)
        case 3:
            # Can be three of a kind or two pair
            match item[0].count(item[0][0]):
                case 3:
                    hand_split["three"].append(item)
                case 2:
                    hand_split["two pair"].append(item)
                case 1:
                    if item[0].count(item[0][1]) == 2:
                       hand_split["two pair"].append(item)
                    else:
                       hand_split["three"].append(item) 
        case 4:
            hand_split["one pair"].append(item)
        case 5:
            hand_split["high card"].append(item)

# Sort the hands within the type

def compare_hands(hand1, hand2):
    values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14}
    
    if (values[hand1[0][0]] > values[hand2[0][0]]):
        return 1
    elif (values[hand1[0][0]] < values[hand2[0][0]]):
        return -1
    elif (len(hand1[0]) == 1) or (len(hand2[0]) == 1):
        return 0
    else:
        return compare_hands((hand1[0][1:], hand1[1]), (hand2[0][1:], hand2[1]))

for key in hand_split:
    hand_split[key] = sorted(hand_split[key], key=functools.cmp_to_key(compare_hands))

# Get total calue
multiplier = 1
sum = 0
for key in hand_split:
    for hand in hand_split[key]:
        sum += multiplier * hand[1]
        multiplier += 1

print("The answer to puzzle 1 is: " + str(sum))

###################################################
# Part 2
###################################################

hand_split = {key: [] for key in hand_types}

# Classify all the hands, and put the in the dictionary

for item in data:
    unique_cards = list(set(item[0]))
    
    match len(unique_cards):
        case 1:
            hand_split["five"].append(item)
        case 2:
            # Can be full house or four of a kind or five if we have a joker
            if 'J' in item[0]:
                hand_split["five"].append(item)
            elif (item[0].count(item[0][0]) == 4) or (item[0].count(item[0][0]) == 1):
                hand_split["four"].append(item)
            else:
                hand_split["full house"].append(item)
        case 3:
            # Can be three of a kind or two pair
            # If we have a joker it could be 4 of a kind or full house
            match item[0].count(item[0][0]):
                case 3:
                    if 'J' in item[0]:
                        hand_split["four"].append(item)
                    else:
                        hand_split["three"].append(item)
                case 2:
                    # Here what happens depends on the number of jokers, 0, 1 or 2
                    match item[0].count('J'):
                        case 2:
                            hand_split["four"].append(item)
                        case 1:
                            hand_split["full house"].append(item)
                        case 0:
                            hand_split["two pair"].append(item)
                case 1:
                    if item[0].count(item[0][1]) == 2:
                       match item[0].count('J'):
                            case 2:
                                hand_split["four"].append(item)
                            case 1:
                                hand_split["full house"].append(item)
                            case 0:
                                hand_split["two pair"].append(item)
                    else:
                        if 'J' in item[0]:
                            hand_split["four"].append(item)
                        else:
                            hand_split["three"].append(item)
        case 4:
            if 'J' in item[0]:
                hand_split["three"].append(item)
            else:
                hand_split["one pair"].append(item)
        case 5:
            if 'J' in item[0]:
                hand_split["one pair"].append(item)
            else:
                hand_split["high card"].append(item)

def compare_hands_2(hand1, hand2):
    values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 0,
        'Q': 12,
        'K': 13,
        'A': 14}
    
    if (values[hand1[0][0]] > values[hand2[0][0]]):
        return 1
    elif (values[hand1[0][0]] < values[hand2[0][0]]):
        return -1
    elif (len(hand1[0]) == 1) or (len(hand2[0]) == 1):
        return 0
    else:
        return compare_hands_2((hand1[0][1:], hand1[1]), (hand2[0][1:], hand2[1]))
    
for key in hand_split:
    hand_split[key] = sorted(hand_split[key], key=functools.cmp_to_key(compare_hands_2))

# Get total calue
multiplier = 1
sum = 0
for key in hand_split:
    for hand in hand_split[key]:
        sum += multiplier * hand[1]
        multiplier += 1

print("The answer to puzzle 2 is: " + str(sum))