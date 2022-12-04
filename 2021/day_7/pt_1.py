def calculate_fuel_consumption(starting_crab_postions, optimal_position):
    """
    """
    fuel_consumption = 0
    for crab_position in starting_crab_postions:
        fuel_consumption += abs(crab_position - optimal_position)

    return fuel_consumption

def find_optimal_position(starting_positions, optimal_positions):
    # There's only 2 possible postions available, calculate fuel consumption for
    # each and return the minimum
    if len(optimal_positions) == 2:
        first = calculate_fuel_consumption(starting_positions, optimal_positions[0])
        second = calculate_fuel_consumption(starting_positions, optimal_positions[1])
        return first if first < second else second
    
    # Cast to int to get round number
    middle_index = int(len(optimal_positions) / 2)
    middle_consumption = calculate_fuel_consumption(starting_positions, optimal_positions[middle_index])
    lower_consumption = calculate_fuel_consumption(starting_positions, optimal_positions[middle_index - 1])
    higher_consumption = calculate_fuel_consumption(starting_positions, optimal_positions[middle_index + 1])

    # We have found the optimal postion
    if lower_consumption > middle_consumption and higher_consumption > middle_consumption:
        return middle_consumption

    if lower_consumption < middle_consumption:
        split_positions = optimal_positions[:middle_index]
        return find_optimal_position(starting_positions, split_positions)
    else:
        split_positions = optimal_positions[middle_index + 1:]
        return find_optimal_position(starting_positions, split_positions)

# =========
# Read input
# =========
FILE_NAME = 'input.txt'
with open(FILE_NAME) as file:
    raw_crab_positions = file.read()

crab_positions = [int(fish_age) for fish_age in raw_crab_positions.split(',')]
optimal_positions = list(range(min(crab_positions), (max(crab_positions) + 1)))
optimal_position = find_optimal_position(crab_positions, optimal_positions)
print(optimal_position)