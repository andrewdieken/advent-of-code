def spawn_fish(live_fishes):
    """
    Given current spawned fish, spawn new fish and age existing ones.
    """
    aged_fish = live_fishes.copy()
    spawned_fish = []

    for index in range(len(live_fishes)):
        if live_fishes[index] == 0:
            # Spawn new fish
            spawned_fish.append(8)

            # Reset fish age after spawning
            aged_fish[index] = 6
        else:
            # Age fish by one day
            aged_fish[index] -= 1
    
    # Combine spawned fish & aged fish
    return aged_fish + spawned_fish
    

# =========
# Read input
# =========
FILE_NAME = 'input.txt'
with open(FILE_NAME) as file:
    raw_fish_ages = file.read()

spawned_fish = [int(fish_age) for fish_age in raw_fish_ages.split(',')]

spawning_days = 80
while spawning_days > 0:
    spawned_fish = spawn_fish(spawned_fish)
    spawning_days -= 1

answer = len(spawned_fish)
print(answer)