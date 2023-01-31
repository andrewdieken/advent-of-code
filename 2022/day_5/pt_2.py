import re


input_file_path = '/Users/andrewdieken/dev/advent-of-code/2022/day_5/input.txt'
with open(input_file_path, 'r') as input_file:
    raw_input = input_file.read()

raw_stack_input, raw_action_input = raw_input.split('\n\n')

# (1) construct stacks
stack_rows = raw_stack_input.split('\n')
num_stacks = int(stack_rows.pop().strip()[-1])
stacks = [[] for i in range(num_stacks)]

for row in stack_rows:
    crate = 0
    for i in range(1, len(stack_rows[0]), 4):
        if row[i] != ' ':
            stacks[crate].insert(0, row[i])
        crate += 1

# (2) complete actions
actions = raw_action_input.split('\n')
action_regex = r'move (?P<quantity>\d+) from (?P<start_crate>\d+) to (?P<end_crate>\d+)'
for action in actions:
    match = re.search(action_regex, action)
    quantity = int(match.groups()[0])
    start_crate = int(match.groups()[1]) - 1
    end_crate = int(match.groups()[2]) - 1

    # Move crates to new stack
    stacks[end_crate].extend(stacks[start_crate][-quantity:])

    # Remove crates from existing stack
    stacks[start_crate] = stacks[start_crate][:-quantity]

output = ''
for stack in stacks:
    output += stack.pop()

print(output)
