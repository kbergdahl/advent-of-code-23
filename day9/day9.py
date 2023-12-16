# Read data
#data_source = 'day9/example_data.txt'
data_source = 'day9/data.txt'

with open(data_source) as f:
    lines = f.read().split('\n')


def reduce_and_extrapolate(sequence):
    if not any(sequence):
        return 0
    else:
        new_sequence = [b-a for a,b in zip(sequence, sequence[1:])]
        return sequence[-1] + reduce_and_extrapolate(new_sequence)


sum = 0

for line in lines:
    sequence = [int(item) for item in line.split()]
    sum += reduce_and_extrapolate(sequence)

print('The solution to puzzle 1 is: ' + str(sum))

#####################################
def reduce_and_extrapolate_left(sequence):
    if not any(sequence):
        return 0
    else:
        new_sequence = [b-a for a,b in zip(sequence, sequence[1:])]
        return sequence[0] - reduce_and_extrapolate_left(new_sequence)

sum = 0

for line in lines:
    sequence = [int(item) for item in line.split()]
    sum += reduce_and_extrapolate_left(sequence)

print('The solution to puzzle 2 is: ' + str(sum))