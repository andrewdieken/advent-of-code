import string

combined_lower_and_upper_characters = (string.ascii_lowercase + string.ascii_uppercase)
def get_item_priority(item):
    """
    Given an item (i.e. a character) return it's priority.
    """
    return combined_lower_and_upper_characters.index(str(item)) + 1


input_file_path = '/Users/andrewdieken/dev/advent-of-code/2022/day_3/input.txt'
with open(input_file_path, 'r') as input_file:
    raw_input = input_file.readlines()

priority_sum = 0
for i in range(0, len(raw_input), 3):
    first_rucksack = set(raw_input[i].strip())
    second_rucksack = set(raw_input[i+1].strip())
    third_rucksack = set(raw_input[i+2].strip())

    shared_item = list(first_rucksack & second_rucksack & third_rucksack)[0]
    priority_sum += get_item_priority(shared_item)

print(priority_sum)