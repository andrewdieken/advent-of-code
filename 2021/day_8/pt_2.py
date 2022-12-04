def generate_known_segment_connection_mappings(wire_segment_connections):
    """
    """
    segment_count_to_digit_mappings =  {
        2: 1,
        4: 4,
        3: 7,
        7: 8
    }

    known_mappings = {
        1: "",
        4: "",
        7: "",
        8: ""
    }

    for segment_combo in wire_segment_connections:
        combo_len = len(segment_combo)
        if segment_count_to_digit_mappings.get(combo_len):
            known_mappings[segment_count_to_digit_mappings.get(combo_len)] = ''.join(sorted(segment_combo))

    return known_mappings

def generate_wire_segment_connection_mappings(signal_patterns):
    """
    """
    mappings = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: ""
    }

    # Get known mappings
    known_segment_connection_mappings = generate_known_segment_connection_mappings(signal_patterns)
    mappings.update(known_segment_connection_mappings)

    #
    # Get 6 segment length digits
    #
    six_segment_length_patterns = [pattern for pattern in signal_patterns if len(pattern) == 6]
    for pattern in six_segment_length_patterns:
        # 9
        if all(segment in pattern for segment in mappings[4]):
            mappings[9] = ''.join(sorted(pattern))
        # 0
        elif all(segment in pattern for segment in mappings[1]):
            mappings[0] = ''.join(sorted(pattern))
        # 6
        else:
            mappings[6] = ''.join(sorted(pattern))

    #
    # Get 5 segment length digits
    #
    five_segment_length_patterns = [pattern for pattern in signal_patterns if len(pattern) == 5]
    for pattern in five_segment_length_patterns:
        # 3
        if all(segment in pattern for segment in mappings[1]):
            mappings[3] = ''.join(sorted(pattern))
        # 5
        elif all(segment in mappings[6] for segment in pattern):
            mappings[5] = ''.join(sorted(pattern))
        # 2
        else:
           mappings[2] = ''.join(sorted(pattern))

    return mappings

def decode_and_add_output_values(entry_output, segment_mappings):
    """
    """
    reverse_mappings = {v:k for k,v in segment_mappings.items()}

    output_num = ''
    for signal_pattern in entry_output:
        sorted_output = ''.join(sorted(signal_pattern))
        output_num += str(reverse_mappings[sorted_output])

    return int(output_num)

# =========
# Read input
# =========
FILE_NAME = 'input.txt'
with open(FILE_NAME) as file:
    raw_input = file.readlines()

answer = 0
for entry in raw_input:
    signal_patterns, output_values = entry.strip().split(' | ')
    wire_segment_connection_mappings = generate_wire_segment_connection_mappings(signal_patterns.split(' '))
    output_value_sum = decode_and_add_output_values(output_values.split(' '), wire_segment_connection_mappings)
    answer += output_value_sum

print(answer)
