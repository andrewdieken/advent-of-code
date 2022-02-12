FILE_NAME = 'input.txt'
with open(FILE_NAME) as file:
  raw_line_coordinate_input = file.readlines()

# =========
# Format input
# =========
line_coordinates = []
for raw_line_coordinates in raw_line_coordinate_input:
    stripped_line_coordinates = raw_line_coordinates.strip()
    start_coordinates, end_coordinates = stripped_line_coordinates.split(' -> ')
    start_x_coordinate, start_y_coordinate = start_coordinates.split(',')
    end_x_coordinate, end_y_coordinate = end_coordinates.split(',')
    line_coordinates.append(
        {
            'start': {
                'x': int(start_x_coordinate),
                'y': int(start_y_coordinate)
            },
            'end': {
                'x': int(end_x_coordinate),
                'y': int(end_y_coordinate)
            }
        }
    )

# =========
# Mapping of a point to the number of occurrences.
#
# str => int
# example: "0,9" => 2
# =========
coordinate_occurrences = {}

for line in line_coordinates:
    if line['start']['x'] == line['end']['x']:
        if line['start']['y'] > line['end']['y']:
            while line['start']['y'] >= line['end']['y']:
                x_coord = line['start']['x']
                y_coord = line['start']['y']
                point = "{},{}".format(x_coord, y_coord)
                coordinate_occurrences[point] = coordinate_occurrences.get(point, 0) + 1
                line['start']['y'] -= 1
        else:
            while line['end']['y'] >= line['start']['y']:
                x_coord = line['start']['x']
                y_coord = line['end']['y']
                point = "{},{}".format(x_coord, y_coord)
                coordinate_occurrences[point] = coordinate_occurrences.get(point, 0) + 1
                line['end']['y'] -= 1
    elif line['start']['y'] == line['end']['y']:
        if line['start']['x'] > line['end']['y']:
            while line['start']['x'] >= line['end']['y']:
                x_coord = line['start']['x']
                y_coord = line['start']['y']
                point = "{},{}".format(x_coord, y_coord)
                coordinate_occurrences[point] = coordinate_occurrences.get(point, 0) + 1
                line['start']['x'] -= 1
        else:
            while line['end']['x'] >= line['start']['x']:
                x_coord = line['end']['x']
                y_coord = line['start']['y']
                point = "{},{}".format(x_coord, y_coord)
                coordinate_occurrences[point] = coordinate_occurrences.get(point, 0) + 1
                line['end']['x'] -= 1
    elif line['start']['x'] > line['end']['x']:
        if line['start']['y'] > line['end']['y']:
            # start x bigger
            # start y bigger
            while line['start']['y'] >= line['end']['y']:
                x_coord = line['start']['x']
                y_coord = line['start']['y']
                point = "{},{}".format(x_coord, y_coord)
                coordinate_occurrences[point] = coordinate_occurrences.get(point, 0) + 1
                line['start']['x'] -= 1
                line['start']['y'] -= 1
        else:
            # start x bigger
            # end y bigger
            while line['end']['y'] >= line['start']['y']:
                x_coord = line['start']['x']
                y_coord = line['end']['y']
                point = "{},{}".format(x_coord, y_coord)
                coordinate_occurrences[point] = coordinate_occurrences.get(point, 0) + 1
                line['start']['x'] -= 1
                line['end']['y'] -= 1
    else:
        if line['start']['y'] > line['end']['y']:
            # end x bigger
            # start y bigger
            while line['start']['y'] >= line['end']['y']:
                x_coord = line['end']['x']
                y_coord = line['start']['y']
                point = "{},{}".format(x_coord, y_coord)
                coordinate_occurrences[point] = coordinate_occurrences.get(point, 0) + 1
                line['end']['x'] -= 1
                line['start']['y'] -= 1
        else:
            # end x bigger
            # end y bigger
            while line['end']['y'] >= line['start']['y']:
                x_coord = line['end']['x']
                y_coord = line['end']['y']
                point = "{},{}".format(x_coord, y_coord)
                coordinate_occurrences[point] = coordinate_occurrences.get(point, 0) + 1
                line['end']['x'] -= 1
                line['end']['y'] -= 1

coordinate_occurrence_values = list(coordinate_occurrences.values())
filtered_coordinate_occurrence_values = list(filter(lambda occurrence: occurrence > 1, coordinate_occurrence_values))
answer = len(filtered_coordinate_occurrence_values)
print(answer)
