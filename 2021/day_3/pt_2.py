from termios import VINTR


FILE_NAME = 'input.txt'
with open(FILE_NAME) as file:
    raw_binary_numbers = file.readlines()

binary_numbers = []
for binary_number in raw_binary_numbers:
    binary_numbers.append(binary_number.strip())

def convert_binary_to_decimal(binary_str):
    return int(binary_str, 2)

def create_default_dict(num_indices):
    return {k: {'0': 0, '1': 0} for k in range(num_indices)}

def get_valid_binaries(index, valid_bit, binaries):
    return [binary for binary in binaries if binary[index] == valid_bit]

def generate_binary_occurrence_mappings(binary_numbers):
    number_of_binary_indices = len(binary_numbers[0])
    binary_occurrences_by_index = create_default_dict(number_of_binary_indices)

    for binary_number in binary_numbers:
        for index in range(number_of_binary_indices):
            indice_value = binary_number[index]
            binary_occurrences_by_index[index][indice_value] += 1

    return binary_occurrences_by_index

def get_oxygen_generator_rating(starting_binaries):
    valid_binaries = starting_binaries.copy()

    for index in range(len(valid_binaries[0])):        
        # Check to see if we've found the correct binary
        if len(valid_binaries) == 1:
            break
        
        binary_bit_occurrence_mappings = generate_binary_occurrence_mappings(valid_binaries)
        bit_occurrences = binary_bit_occurrence_mappings[index]
        if bit_occurrences['1'] >= bit_occurrences['0']:
            valid_binaries = get_valid_binaries(index, '1', valid_binaries)
        else:
            valid_binaries = get_valid_binaries(index, '0', valid_binaries)

    return convert_binary_to_decimal(valid_binaries[0])

def get_co2_scrubber_rating(starting_binaries):
    valid_binaries = starting_binaries.copy()

    for index in range(len(valid_binaries[0])):
        # Check to see if we've found the correct binary
        if len(valid_binaries) == 1:
            break

        binary_bit_occurrence_mappings = generate_binary_occurrence_mappings(valid_binaries)
        bit_occurrences = binary_bit_occurrence_mappings[index]
        if bit_occurrences['0'] <= bit_occurrences['1']:
            valid_binaries = get_valid_binaries(index, '0', valid_binaries)
        else:
            valid_binaries = get_valid_binaries(index, '1', valid_binaries)

    return convert_binary_to_decimal(valid_binaries[0])

oxygen_generator_rating = get_oxygen_generator_rating(binary_numbers)
co2_scrubber_rating = get_co2_scrubber_rating(binary_numbers)
answer = oxygen_generator_rating * co2_scrubber_rating