# Input data: file with lines
# Find the first and last digit of each line, make them into a 2-digit number, sum all the numbers

import re

# Read data
with open('day1/data.txt') as f:
    lines = f.readlines()


# Testlines, should give 281 for puzzle 2
# lines = ['two1nine',
#         'eightwothree',
#         'abcone2threexyz',
#         'xtwone3four',
#         '4nineeightseven2',
#         'zoneight234',
#         '7pqrstsixteen']

# Puzzle 1, only use digits
sum = 0
for line in lines:
    first_digit = int(re.search('\d', line).group(0))
    last_digit = int(re.search('\d', line[::-1]).group(0))
    sum += (first_digit*10 + last_digit)

print(sum)

# Puzzle 2, also use spelled out digits
patternFront = '\d|one|two|three|four|five|six|seven|eight|nine'
patternBack = '\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin'

# Function to transform strings to digits
def toDigit(str):
    match str:
        case 'one':
            return 1
        case 'two':
            return 2
        case 'three':
            return 3
        case 'four':
            return 4
        case 'five':
            return 5
        case 'six':
            return 6
        case 'seven':
            return 7
        case 'eight':
            return 8
        case 'nine':
            return 9
        case _:
            return int(str)

sum = 0
for line in lines:
    first_digit = re.search(patternFront, line).group(0)
    last_digit = re.search(patternBack, line[::-1]).group(0)
    sum += (toDigit(first_digit)*10 + toDigit(last_digit[::-1]))

print(sum)

