# Read data
data_source = 'day21/example_data.txt'
#data_source = 'day21/data.txt'

with open(data_source) as f:
    myMap = f.read().split('\n')

# Create a set with all rock positions
# (Using imaginary numbers to represent positions)
rocks = set()
for row, line in enumerate(myMap):
    for col, symbol in enumerate(line):
        if symbol == '#':
            rocks.add(row + col*1j)
        elif symbol == 'S':
            start = row + col*1j

row_len = row+1
col_len = col+1

nogo = {r - 1j for r in range(-1, row+1)}.union({r + (col+1)*1j for r in range(-1,row+1)}).union({-1 + c*1j for c in range(-1,col+1)}).union({(row+1) + c*1j for c in range(-1,col+1)})

nogo.update(rocks)
# You can always go back to where you were before. So a new set of possible positions will always include the one before the current
# We will use two sets, for odd and even steps
odds = set()
evens = {start}

nbr_steps = 64

for i in range(nbr_steps//2):
    # Start by taking the odd step
    for pos in evens:
        odds.add(pos + 1)
        odds.add(pos - 1)
        odds.add(pos + 1j)
        odds.add(pos - 1j)
    odds = odds.difference(nogo)

    # Then take the even steps
    for pos in odds:
        evens.add(pos + 1)
        evens.add(pos - 1)
        evens.add(pos + 1j)
        evens.add(pos - 1j)
    evens = evens.difference(nogo)

print("The solution to puzzle 1 is: " + str(len(evens)))

################################################
