input_file_path = '/Users/andrewdieken/dev/advent-of-code/2022/day_1/input.txt'
elf_calorie_counts = {}

# Read file input
with open(input_file_path, 'r') as input_file:
    raw_elf_calories = input_file.read().split('\n\n')

elf_count = 1
for raw_calories in raw_elf_calories:
    calories = raw_calories.strip().split('\n')
    elf_calorie_counts[elf_count] = sum(map(int, calories))
    elf_count += 1

print(max(elf_calorie_counts.values()))
