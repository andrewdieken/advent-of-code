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

def generate_gamma_rate(binary_occurrence_mappings):
    gamma_rate = ''
    for binary_occurrences in binary_occurrence_mappings.values():
        if binary_occurrences['0'] > binary_occurrences['1']:
            gamma_rate += '0'
        else:
            gamma_rate += '1'

    return convert_binary_to_decimal(gamma_rate)

def generate_epsilon_rate(binary_occurrence_mappings):
    epsilon_rate = ''
    for binary_occurrences in binary_occurrence_mappings.values():
        if binary_occurrences['0'] < binary_occurrences['1']:
            epsilon_rate += '0'
        else:
            epsilon_rate += '1'

    return convert_binary_to_decimal(epsilon_rate)

number_of_binary_indices = len(binary_numbers[0])
binary_occurrences_by_index = create_default_dict(number_of_binary_indices)

for binary_number in binary_numbers:
    for index in range(number_of_binary_indices):
        indice_value = binary_number[index]
        binary_occurrences_by_index[index][indice_value] += 1

gamma_rate = generate_gamma_rate(binary_occurrences_by_index)
epsilon_rate = generate_epsilon_rate(binary_occurrences_by_index)
answer = gamma_rate * epsilon_rate