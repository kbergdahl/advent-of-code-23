import numpy as np

# Read data
#data_source = 'day20/example_data.txt'
data_source = 'day20/data.txt'

with open(data_source) as f:
    module_list = f.read().split('\n')

# Create a dictionary of the modules, start by finding all conjuctions
modules = {}
for line in module_list:
    if line[0] == '&':

        line = line.split()

        mod_type = line[0][0]
        mod_name = line[0][1:]
        recievers = line[2:]
        recievers = [r.replace(',', '') for r in recievers]

        modules[mod_name] = {'mod_type': mod_type, 'recievers': recievers, 'watching': {}}

# Then add the other modules
for line in module_list:
    if line[0] != '&':
        line = line.split()

        mod_type = line[0][0]
        mod_name = line[0][1:]
        recievers = line[2:]
        recievers = [r.replace(',', '') for r in recievers]

        if mod_type == '%':
            # Create a flipflop with status off
            modules[mod_name] = {'mod_type': mod_type, 'recievers': recievers, 'status': False}
        else:
            # This is the broadcaster
            modules['broadcaster'] = {'mod_type': 'b', 'recievers': recievers}
        
        # If there are any conjunctions in the recievers list, add the node to those watch lists
        for reciever in recievers:
            if reciever in modules.keys():
                if modules[reciever]['mod_type'] == '&': modules[reciever]['watching'][mod_name] = 'l'
highs = 0
lows = 0

for i in range(1000):
    todo = [('broadcaster', 'l', 'button')]
    while todo:
        name, signal, sender = todo.pop(0)

        # Count the signals
        if signal == 'l':
            lows += 1
        else:
            highs += 1


        # For part to, notify when 'rx' is hit
        if name == 'rx' and signal == 'l': print("The solution to puzzle 2 is: " + str(i+1))
        if name not in modules.keys(): continue

        # If we have a flipflop
        if modules[name]['mod_type'] == '%':
            if signal == 'l':
                out_signal = 'l' if modules[name]['status'] else 'h'
                modules[name]['status'] = not modules[name]['status']

                for r in modules[name]['recievers']:
                    todo.append((r, out_signal, name))
        
        # If we have a conjunction
        if modules[name]['mod_type'] == '&':
            modules[name]['watching'][sender] = signal
            # Check all the watching, if we have any low, we send a high
            out_signal = 'h' if 'l' in modules[name]['watching'].values() else 'l'

            for r in modules[name]['recievers']:
                todo.append((r, out_signal, name))
        
        # If we have a broadcaster
        if modules[name]['mod_type'] == 'b':
            for r in modules[name]['recievers']:
                todo.append((r, 'l', name))

print("The answer to puzzle 1 is: " + str(lows * highs))

###################################################
# Part 2

# Reset the modules
# Create a dictionary of the modules, start by finding all conjuctions
modules = {}
for line in module_list:
    if line[0] == '&':

        line = line.split()

        mod_type = line[0][0]
        mod_name = line[0][1:]
        recievers = line[2:]
        recievers = [r.replace(',', '') for r in recievers]

        modules[mod_name] = {'mod_type': mod_type, 'recievers': recievers, 'watching': {}}

# Then add the other modules
for line in module_list:
    if line[0] != '&':
        line = line.split()

        mod_type = line[0][0]
        mod_name = line[0][1:]
        recievers = line[2:]
        recievers = [r.replace(',', '') for r in recievers]

        if mod_type == '%':
            # Create a flipflop with status off
            modules[mod_name] = {'mod_type': mod_type, 'recievers': recievers, 'status': False}
        else:
            # This is the broadcaster
            modules['broadcaster'] = {'mod_type': 'b', 'recievers': recievers}
        
        # If there are any conjunctions in the recievers list, add the node to those watch lists
        for reciever in recievers:
            if reciever in modules.keys():
                if modules[reciever]['mod_type'] == '&': modules[reciever]['watching'][mod_name] = 'l'


# rx gets it's input from lx, a &-module
# so when lx gets all high, it send low to rx
# Check the inputs to lx, see if there is a cycle to when they get low signals (which makes them send high to lx)

ls_inputs = {'cl':[], 'rp':[], 'lb':[], 'nj':[]}                

for i in range(1, 10000):
    todo = [('broadcaster', 'l', 'button')]
    while todo:
        name, signal, sender = todo.pop(0)

        # Note high signals from lx-inputs
        if name in ls_inputs.keys() and signal == 'l':
            ls_inputs[name].append(i)

        if name not in modules.keys(): continue

        # If we have a flipflop
        if modules[name]['mod_type'] == '%':
            if signal == 'l':
                out_signal = 'l' if modules[name]['status'] else 'h'
                modules[name]['status'] = not modules[name]['status']

                for r in modules[name]['recievers']:
                    todo.append((r, out_signal, name))
        
        # If we have a conjunction
        if modules[name]['mod_type'] == '&':
            modules[name]['watching'][sender] = signal
            # Check all the watching, if we have any low, we send a high
            out_signal = 'h' if 'l' in modules[name]['watching'].values() else 'l'

            for r in modules[name]['recievers']:
                todo.append((r, out_signal, name))
        
        # If we have a broadcaster
        if modules[name]['mod_type'] == 'b':
            for r in modules[name]['recievers']:
                todo.append((r, 'l', name))

print("Cycles when inputs to ls get a low signal: " + str(ls_inputs))

my_loops = [3733, 4091, 3911, 4093]

# Getting some overflow error applying reduce to the whole thing so take in steps
lcm = 1
for item in my_loops:
    lcm = np.lcm(lcm, item, dtype=np.int64)

print("The solution to puzzle 2 is: " + str(lcm))