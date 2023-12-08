# Read data
data_source = 'day8/example_data.txt'
#data_source = 'day8/data.txt'

with open(data_source) as f:
    lines = f.read().split('\n')


# Process data
instructions = lines[0]
paths = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2:]}

