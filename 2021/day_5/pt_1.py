from doctest import debug_src


FILE_NAME = 'input.txt'
with open(FILE_NAME) as file:
  raw_line_coordinate_input = file.readlines()

# =========
# Format input
# =========
line_coordinate_list = []
for raw_line_coordinates in raw_line_coordinate_input:
    stripped_line_coordinates = raw_line_coordinates.strip()
    start_coordinates, end_coordinates = stripped_line_coordinates.split(' -> ')
    start_x_coordinate, start_y_coordinate = start_coordinates.split(',')
    end_x_coordinate, end_y_coordinate = end_coordinates.split(',')
    line_coordinate_list.append(
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

def is_horizontal_or_vertical_line(coordinates):
    """
    Whether the given line coordinates form a horizontal or vertical line.
    """
    return coordinates['start']['x'] == coordinates['end']['x'] or coordinates['start']['y'] == coordinates['end']['y']

def generate_coordinate_range(start_coord, end_coord, length):
    """
    Given a starting & ending x or y coordinate, generate a list of all the
    coordinates on that line.
    """
    if start_coord == end_coord:
        return [start_coord] * length
    elif end_coord > start_coord:
        return list(range(start_coord, end_coord + 1))
    else:
        # reverse the list to ensure correct order
        return list(range(start_coord, end_coord - 1, -1))

line_point_occurrence_mappings = {}

for coordinates in line_coordinate_list:
    if not is_horizontal_or_vertical_line(coordinates):
        continue

    x_line_length = abs(coordinates['start']['x'] - coordinates['end']['x']) + 1
    y_line_length = abs(coordinates['start']['y'] - coordinates['end']['y']) + 1
    line_length = max(x_line_length, y_line_length)
    x_coordinate_range = generate_coordinate_range(coordinates['start']['x'], coordinates['end']['x'], line_length)
    y_coordinate_range = generate_coordinate_range(coordinates['start']['y'], coordinates['end']['y'], line_length)

    for index in range(line_length):
        line_point = "{},{}".format(x_coordinate_range[index], y_coordinate_range[index])
        line_point_occurrence_mappings[line_point] = line_point_occurrence_mappings.get(line_point, 0) + 1
        
occurrences_list = list(line_point_occurrence_mappings.values())
filtered_occurrences = list(filter(lambda occurrence: occurrence > 1, occurrences_list))
answer = len(filtered_occurrences)
print(answer)