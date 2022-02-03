FILE_NAME = ''
with open(FILE_NAME) as file:
    raw_depths = file.readlines()

depths = []
for depth in raw_depths:
    depths.append(depth.strip())

increase_count = 0
previous_depth = depths[0]
for depth in depths[1:]:
    if int(depth) > int(previous_depth):
        increase_count += 1
    previous_depth = depth