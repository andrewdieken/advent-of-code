input_file_path = '/Users/andrewdieken/dev/advent-of-code/2022/day_6/input.txt'
with open(input_file_path, 'r') as input_file:
    raw_input = input_file.read()

current_index = 0
while current_index <= (len(raw_input) - 14):
    window = raw_input[current_index:current_index+14]

    # Start of packet detected
    if len(set(window)) == len(window):
        break

    current_index += 1

print(f'Answer: {current_index + 14}')
