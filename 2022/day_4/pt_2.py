input_file_path = '/Users/andrewdieken/dev/advent-of-code/2022/day_4/input.txt'
with open(input_file_path, 'r') as input_file:
    raw_input = input_file.readlines()

total_fully_contained_pairs = 0
for pairing in raw_input:
    pairing = pairing.strip()
    first_pair, second_pair = [pair.split('-') for pair in pairing.split(',')]

    if (int(second_pair[0]) <= int(first_pair[0]) <= int(second_pair[1])) or (int(second_pair[0]) <= int(first_pair[1]) <= int(second_pair[1])):
        total_fully_contained_pairs += 1
    elif (int(first_pair[0]) <= int(second_pair[0]) <= int(first_pair[1])) or (int(first_pair[0]) <= int(second_pair[1]) <= int(first_pair[1])):
        total_fully_contained_pairs += 1

print(total_fully_contained_pairs)
