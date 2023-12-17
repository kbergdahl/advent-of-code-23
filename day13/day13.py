import numpy as np

# Read data
#data_source = 'day13/example_data.txt'
data_source = 'day13/data.txt'

with open(data_source) as f:
    patterns = f.read().split('\n\n')

sum = 0

for pattern in patterns:
    horizontal_point = 0
    vertical_point = 0

    # Convert to numpy array bc they have useful functions
    pattern = pattern.split('\n')
    pattern = [[*row] for row in pattern]
    pattern = np.array(pattern)

    rows, cols = pattern.shape

    # Check all possible horizontal reflection points (reflectionpoint being between row-1 and row)
    for ref_point in range(1,rows):
        # if the potential reflection is in the top half
        if ref_point <= rows/2:
            top_half = pattern[:ref_point]
            bottom_half = np.flipud(pattern[ref_point:(2*ref_point)])
        
        # if we are in the bottom half
        else:
            bottom_half = np.flipud(pattern[ref_point:])
            top_half = pattern[(2*ref_point - rows):ref_point]
        
        if np.array_equal(top_half, bottom_half):
            horizontal_point = ref_point
    
    # Then do the same for vertical points
    flipped_pattern = np.transpose(pattern)
    for ref_point in range(1,cols):
        # if the potential reflection is in the top half
        if ref_point <= cols/2:
            top_half = flipped_pattern[:ref_point]
            bottom_half = np.flipud(flipped_pattern[ref_point:(2*ref_point)])
        
        # if we are in the bottom half
        else:
            bottom_half = np.flipud(flipped_pattern[ref_point:])
            top_half = flipped_pattern[(2*ref_point - cols):ref_point]
        
        if np.array_equal(top_half, bottom_half):
            vertical_point = ref_point
    
    # Add in the results
    sum += 100*horizontal_point + vertical_point

print("The solution to puzzle 1 is: " + str(sum))

# Part 2
sum = 0

for pattern in patterns:
    horizontal_point = 0
    vertical_point = 0

    # Convert to numpy array bc they have useful functions
    pattern = pattern.split('\n')
    pattern = [[*row] for row in pattern]
    pattern = np.array(pattern)

    rows, cols = pattern.shape

    # Check all possible horizontal reflection points (reflectionpoint being between row-1 and row)
    for ref_point in range(1,rows):
        # if the potential reflection is in the top half
        if ref_point <= rows/2:
            top_half = pattern[:ref_point]
            bottom_half = np.flipud(pattern[ref_point:(2*ref_point)])
        
        # if we are in the bottom half
        else:
            bottom_half = np.flipud(pattern[ref_point:])
            top_half = pattern[(2*ref_point - rows):ref_point]
        
        if np.sum(top_half != bottom_half) == 1:
            horizontal_point = ref_point
    
    # Then do the same for vertical points
    flipped_pattern = np.transpose(pattern)
    for ref_point in range(1,cols):
        # if the potential reflection is in the top half
        if ref_point <= cols/2:
            top_half = flipped_pattern[:ref_point]
            bottom_half = np.flipud(flipped_pattern[ref_point:(2*ref_point)])
        
        # if we are in the bottom half
        else:
            bottom_half = np.flipud(flipped_pattern[ref_point:])
            top_half = flipped_pattern[(2*ref_point - cols):ref_point]
        
        if np.sum(top_half != bottom_half) == 1:
            vertical_point = ref_point
    
    # Add in the results
    sum += 100*horizontal_point + vertical_point

print("The solution to puzzle 2 is: " + str(sum))