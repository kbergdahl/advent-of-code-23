# Read data
#data_source = 'day15/example_data.txt'
data_source = 'day15/data.txt'

with open(data_source) as f:
    sequence = f.read().split(',')

def santa_hash(mystring):
    a = 0
    for c in mystring:
        a += ord(c)
        a = a * 17
        a = a % 256
    return a

sum = 0
for item in sequence:
    sum += santa_hash(item)

print("The solution to puzzle 1 is: " + str(sum))

##################
# Handle boxes
boxes = {}
for item in sequence:
    if '=' in item:
        sign_pos = item.index('=')
        label = item[0:sign_pos]
        focal_len = int(item[(sign_pos+1):])
        box = santa_hash(label)

        if box in boxes.keys():
            if label in boxes[box]:
                label_ind = boxes[box].index(label)
                boxes[box][label_ind + 1] = focal_len
            else:
                boxes[box] = boxes[box] + [label, focal_len]
        else:
            boxes[box] = [label, focal_len]
    
    else:
        label = item[0:-1]
        box = santa_hash(label)

        if box in boxes.keys():
            if label in boxes[box]:
                label_ind = boxes[box].index(label)
                del boxes[box][label_ind:label_ind+2]

sum = 0
# Compute focusing power
for box in boxes:
    for pos in range(int(len(boxes[box])/2)):
        sum += (box + 1) * (pos + 1) * boxes[box][2*pos+1]
print("The solution to puzzle 2 is: " + str(sum))