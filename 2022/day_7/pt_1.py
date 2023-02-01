import re


def calculate_total_directories_size(root_directory):
    """
    """
    total_size = root_directory.get_size() if root_directory.get_size() <= 100000 else 0

    if not root_directory.child_directories:
         return total_size

    for child_directory in root_directory.child_directories:
        total_size += calculate_total_directories_size(child_directory)

    return total_size


CHANGE_DIRECTORY_IN = r'\$ cd (?P<name>[\w]+)'
CHANGE_DIRECTORY_OUT = '$ cd ..'
LIST_DIRECTORY = '$ ls'
OUTTER_MOST_DIRECTORY = '/'
DIRECTORY = r'dir (?P<name>[\w]+)'
FILE = r'(?P<size>[\d]+) (?P<name>([\w]+)?.?(\w)+)'


class File(object):
    """
    """

    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory(object):
    """
    """

    def __init__(self, name, parent=None):
        self.name = name
        self.parent_directory = parent
        self.size = 0
        self.child_files = []
        self.child_directories = []

    def add_child_file(self, file):
        """
        """
        self.child_files.append(file)

    def add_child_directory(self, directory):
        """
        """
        self.child_directories.append(directory)

    def get_child_directory(self, directory_name):
        for child_dir in self.child_directories:
            if child_dir.name == directory_name:
                return child_dir

        return None

    def get_size(self):
        if self.size:
            return self.size

        file_sizes = sum(file.size for file in self.child_files)
        directory_sizes = sum(directory.get_size() for directory in self.child_directories)
        self.size = file_sizes + directory_sizes
        return self.size


input_file_path = '/Users/andrewdieken/dev/advent-of-code/2022/day_7/input.txt'
with open(input_file_path, 'r') as input_file:
    raw_input = input_file.readlines()

root_directory = Directory(OUTTER_MOST_DIRECTORY)
current_directory = root_directory

# Skip first line since it's just the root directory
for line in raw_input[1:]:
    line = line.strip()

    try:
        if re.match(CHANGE_DIRECTORY_IN, line):
            match = re.match(CHANGE_DIRECTORY_IN, line)
            dir_name = match.groupdict().get('name')
            current_directory = current_directory.get_child_directory(dir_name)
        elif CHANGE_DIRECTORY_OUT == line:
            current_directory = current_directory.parent_directory
        elif re.match(DIRECTORY, line):
            match = re.match(DIRECTORY, line)
            dir_name = match.groupdict().get('name')
            directory = Directory(dir_name, parent=current_directory)
            current_directory.add_child_directory(directory)
        elif re.match(FILE, line):
            match = re.match(FILE, line)
            file_name = match.groupdict().get('name')
            file_size = int(match.groupdict().get('size'))
            file = File(file_name, file_size)
            current_directory.add_child_file(file)
        else:
            # This should *only* be LIST_DIRECTORY commands
            if LIST_DIRECTORY != line:
                raise Exception(f'ERROR: else block entered with command other than {LIST_DIRECTORY}: {line}')

            continue
    except Exception:
        print(f'ERROR with line: {line}')
        import ipdb; ipdb.set_trace()
        raise


print(f'Answer: {calculate_total_directories_size(root_directory)}')