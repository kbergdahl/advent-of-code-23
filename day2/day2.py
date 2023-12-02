# Input: data with samples pulled from bag of colored cubes

import re

# Read data
with open('day2/data.txt') as f:
    lines = f.readlines()

# Sample lines
""" lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"] """

# Puzzle 1
# Task: find which games would be impossible given the max nbr of cubes of each colour, sum the game IDs

max_red = 12
max_green = 13
max_blue = 14

sum = 0

for game in lines:
    valid_game = True
    # Split into gameID and the samples from the game
    [gameID, samples] = game.split(':')
    samples = samples.split(';')

    for sample in samples:
        # Find the number of cubes of each color in the sample
        nbr_red = re.search('(?=(\d+ red))\d+', sample)
        nbr_green = re.search('(?=(\d+ green))\d+', sample)
        nbr_blue = re.search('(?=(\d+ blue))\d+', sample)

        # Check if there are too many cubes
        if ((nbr_red and int(nbr_red.group(0)) > max_red) or (nbr_green and int(nbr_green.group(0)) > max_green) or (nbr_blue and int(nbr_blue.group(0)) > max_blue)):
            valid_game = False
    
    # If the game is valid, extract the ID and add it to the sum
    if valid_game:
        sum += int(gameID[5:])

print(sum)

# Puzzle 2
# Find least ammount of cubes of each colour for each game, multiply, sum

sum = 0

for game in lines:
    [_, samples] = game.split(':')
    samples = samples.split(';')

    min_red = 0
    min_green = 0
    min_blue = 0

    for sample in samples:
        # Find nbr of each color
        nbr_red = re.search('(?=(\d+ red))\d+', sample)
        nbr_green = re.search('(?=(\d+ green))\d+', sample)
        nbr_blue = re.search('(?=(\d+ blue))\d+', sample)
        
        # Save highest number of color
        if (nbr_red and int(nbr_red.group(0)) > min_red):
            min_red = int(nbr_red.group(0))
        
        if (nbr_green and int(nbr_green.group(0)) > min_green):
            min_green = int(nbr_green.group(0))

        if (nbr_blue and int(nbr_blue.group(0)) > min_blue):
            min_blue = int(nbr_blue.group(0))
    
    sum += min_red*min_green*min_blue

print(sum)