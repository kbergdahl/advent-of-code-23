

# Read data
#data_source = 'day12/example_data.txt'
data_source = 'day12/data.txt'

with open(data_source) as f:
    lines = f.read().split('\n')

memo_dict = {}

# Recursively check a line
def check_line(line, groups):
    # Line - string
    # groups - list of ints

    # If there is no line and all groups used, it worked
    if (not line) and (not groups):
        return 1
    
    # If the line is empty and there are groups remaining, it did not work
    elif (not line):
        return 0
    
    # If we have no groups remaining, we should check if there are any more # in the string and return based on that
    if not groups:
        if '#' in line:
            return 0
        else:
            return 1
    
    # We now check our dictionary
    myKey = line + ','.join([str(a) for a in groups])
    if myKey in memo_dict.keys():
        return memo_dict[myKey]
    
    else:
        # Now it depends on the start of the line
        match line[0]:
            # If it is a dot, remove it an check the rest of the line
            case '.':
                answer = check_line(line[1:], groups)
            
            # If it is unknown, test it with both # and . (. is equivalent to throwing away the thing)
            case '?':
                answer = check_line(line[1:], groups) + check_line('#' + line[1:], groups)
            
            # If it is #, check if we can fit the first group
            case '#':
                # If there is not enough space for the group, it is a fail
                if len(line) < groups[0]:
                    answer = 0
                # If there is a dot in the space that the group would take up, we cannot fit the group, this is a fail
                elif '.' in line[0:groups[0]]:
                    answer = 0
                
                # Now we know there is space for the group

                # If we are at the end of a line, we can place the group. If there are no more groups, we succeed
                elif len(line) == groups[0]:
                    if len(groups) == 1:
                        answer = 1
                    else:
                        answer = 0

                # If we are not at the end of the line, we should check that we have/can place a . after the group
                elif line[groups[0]] == '#':
                    # We cannot place the group here, this is a fail
                    answer = 0
                else:
                    # We can place the group
                    answer = check_line(line[(groups[0]+1):], groups[1:])
        # END OF CASES
        memo_dict[myKey] = answer
        return answer

sum = 0
for item in lines:
    line, groups = item.split()
    groups = groups.split(',')
    groups = [int(a) for a in groups]
    sum += check_line(line, groups)

print("The solution to puzzle 1 is: " + str(sum))

# Part 2, memoized the function to avoid horrificly long computations
sum = 0
for item in lines:
    line, groups = item.split()
    groups = groups.split(',')
    groups = [int(a) for a in groups]

    # Now do the "unfolding"
    line = (line + '?') * 5
    line = line[0:-1]
    groups = groups * 5

    sum += check_line(line, groups)

print("The solution to puzzle 2 is: " + str(sum))