import copy

"""
IMPROVEMENT:
there are 8 possible fish ages (0-8). Instead of storing an individual
instances of each fish age in a master list, track the total number of fish
for each available fish age.

e.g.
      {
        0: 2,
        1: 1,
        2: 5,
        3: 3,
        4: 8,
        5: 1,
        6: 10,
        7: 0,
        8: 4
      }
"""

def generate_default_spawned_fish_age_to_occurrences_mapping():
    """
    Generate the default age to number of fish occurrences mapping.
    """
    return {age: 0 for age in range(9)}

def spawn_fish(spawned_fish_mappings):
    """
    Given current spawned fish, spawn new fish and age existing ones.
    """
    aged_spawned_fish_mappings = generate_default_spawned_fish_age_to_occurrences_mapping()

    for age in range(9):
        if age == 0:
            # Spawn new fish
            aged_spawned_fish_mappings[8] = spawned_fish_mappings[0]

            # Reset fish age after spawning
            aged_spawned_fish_mappings[6] += spawned_fish_mappings[0]
        else:
            # Age fish by one day
            aged_spawned_fish_mappings[age - 1] += spawned_fish_mappings[age]

    return aged_spawned_fish_mappings

# =========
# Read input
# =========
FILE_NAME = 'input.txt'
with open(FILE_NAME) as file:
    raw_fish_ages = file.read()

# =========
# Populate age to occurrence mappings with starting values
# =========
spawned_fish_ages_to_occurrence_mappings = generate_default_spawned_fish_age_to_occurrences_mapping()
for fish_age in raw_fish_ages.split(','):
  spawned_fish_ages_to_occurrence_mappings[int(fish_age)] += 1

# =========
# Spawn fish
# =========
spawning_days = 256
while spawning_days > 0:
    spawned_fish_ages_to_occurrence_mappings = spawn_fish(spawned_fish_ages_to_occurrence_mappings)
    spawning_days -= 1

answer = sum(spawned_fish_ages_to_occurrence_mappings.values())
print(answer)