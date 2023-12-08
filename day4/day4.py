import numpy as np


# Read data
with open('day4/data.txt') as f:
    lines = f.read().splitlines()

# Example data
""" lines = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
         'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
         'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
         'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
         'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
         'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'] """

points = 0
nbr_instances = np.ones(len(lines))

for ind, card in enumerate(lines):
    # Remove 'card X'
    [_, card] = card.split(':')

    # Split into litst with winning numbers and your numbers
    [winners, yours] = card.split('|')
    winners = winners.split()
    yours = yours.split()

    # Find the winning numbers you have
    common = list(set(winners) - (set(winners) - set(yours)))

    # For puzzle one: add any points
    if common:
        points += 2**(len(common)-1)

    # For puzzle 2: add won tickets
    if common:
        for i, _ in enumerate(common):
            if ((ind+i+1)<len(nbr_instances)):
                nbr_instances[ind+i+1] += nbr_instances[ind]

print("The answer to puzzle 1 is: " + str(points))
print("The solution to puzzle 2 is: " + str(int(np.sum(nbr_instances))))