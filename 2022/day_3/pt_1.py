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
for raw_rucksack_contents in raw_input:
    rucksack_contents = raw_rucksack_contents.strip()
    first_comartment_contents = set(rucksack_contents[:(len(rucksack_contents) // 2)])
    second_compartent_contents = set(rucksack_contents[(len(rucksack_contents) // 2):])

    shared_item = list(first_comartment_contents & second_compartent_contents)[0]
    priority_sum += get_item_priority(shared_item)

print(priority_sum)