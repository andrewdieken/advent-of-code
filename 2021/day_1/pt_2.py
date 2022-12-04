FILE_NAME = 'input.txt'
with open(FILE_NAME) as file:
    raw_depths = file.readlines()

depths = []
for depth in raw_depths:
    depths.append(depth.strip())

increased_total = 0
for idx in range(len(depths) - 3):
    cur_window = depths[idx:idx+3]
    nxt_window = depths[idx+1:idx+4]
    if sum(nxt_window) > sum(cur_window):
        increased_total += 1