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

    for segment_combo in wire_segment_connections.split(' '):
        combo_len = len(segment_combo)
        if segment_count_to_digit_mappings.get(combo_len):
            known_mappings[segment_count_to_digit_mappings.get(combo_len)] = segment_combo

    return known_mappings

def generate_wire_segment_connection_mappings(wire_segment_connections):
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
    known_segment_connection_mappings = generate_known_segment_connection_mappings(wire_segment_connections)
    mappings.update(known_segment_connection_mappings)

    #
    # Get 6 segment length digits
    #

    # 0

    # 9

    # 6

    #
    # Get 5 segment length digits
    #

    # 3

    # 5

    # 2

    return mappings

def decode_and_add_output_values(entry_output, segment_mappings):
    """
    """
    output_sum = 0
    for output in entry_output.split(' '):
        output_sum += segment_mappings[output]

# =========
# Read input
# =========
FILE_NAME = 'input.txt'
with open(FILE_NAME) as file:
    raw_input = file.readlines()

answer = 0
for entry in raw_input:
    wire_segment_connections, output_values = entry.strip().split(' | ')
    wire_segment_connection_mappings = generate_wire_segment_connection_mappings(wire_segment_connections)
    output_value_sum = decode_and_add_output_values(output_values, wire_segment_connection_mappings)
    answer += output_value_sum

print(answer)
