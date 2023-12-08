# time you hold button = x
# time limimt = t
# distance = x(t-x) = -x^2 + tx
# if the record is R
# solve for x(t-x) > R
# that will be between the 2 solutions to x(t-x) = R <-> x^2 - tx + R = 0

from numpy.polynomial import Polynomial
import numpy as np

# Read data
#data_source = 'day6/example_data.txt'
data_source = 'day6/data.txt'

with open(data_source) as f:
    lines = f.read().splitlines()

# Process data into lists of ints
times = lines[0].split()[1:]
times = [eval(i) for i in times]

records = lines[1].split()[1:]
records = [eval(i) for i in records]

# Start mathing
product = 1

for time, record in zip(times, records):
    p = Polynomial((record, -1*time, 1))
    roots = p.roots()
    product *= np.ceil(max(roots) - 1) - np.floor(min(roots) + 1) + 1

print("The solution to puzzle 1 is: " + str(int(product)))

# Puzzle 2

# Concatenate all the numbers to one number
time = eval(''.join(lines[0].split()[1:]))
record = eval(''.join(lines[1].split()[1:]))

p = Polynomial((record, -1*time, 1))
roots = p.roots()
nbr_ways = np.ceil(max(roots) - 1) - np.floor(min(roots) + 1) + 1

print("The solution to puzzle 2 is: " + str(int(nbr_ways)))