# =========
# Read input
# =========
FILE_NAME = 'input.txt'
with open(FILE_NAME) as file:
    raw_input = file.readlines()

segment_count_to_digit_mappings =  {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

total = 0
for segment_input in raw_input:
    unique_signal_patters, output_value = segment_input.strip().split(' | ')
    for digit in output_value.split(' '):
        digit_len = len(digit)
        # print("digit: {} & len: {}".format(digit, digit_len))
        if segment_count_to_digit_mappings.get(digit_len):
            total += 1

print(total)
