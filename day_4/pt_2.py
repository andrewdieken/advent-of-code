import copy
from pprint import pprint

class BingoNumber(object):
  """
  Class representing a bingo number on a board.
  """

  def __init__(self, value):
    self.value = value.strip()
    self.marked = 0

class BingoBoard(object):
  """
  Class representing a bingo board.
  """

  def __init__(self, board_input):
    self.board = self._generate_board(board_input)

  def _generate_board(self, board_input):
    """
    Given a bingo board of any size, clean and convert number to instances of
    BingoNumbers.
    """
    board = [[] for i in range(len(board_input))]

    for row_index in range(len(board_input)):
      for board_number in board_input[row_index].split(' '):
        if board_number != '':
          board[row_index].append(BingoNumber(board_number))

    return board

  def mark_number_if_available(self, drawn_number):
    """
    Find and "mark" the BingoNumber instance that corresponds to the provided
    drawn number.
    """
    for row_index in range(len(self.board)):
      for board_number in self.board[row_index]:
        if board_number.value == drawn_number:
          board_number.marked = 1

  def has_bingo(self):
    """
    Whether the current instances contains a bingo.
    """
    for row_x_coordinate in range(len(self.board)):
      row_contains_bingo = True
      column_contains_bingo = True
      for row_y_coordinate in range(len(self.board[row_x_coordinate])):
        if not self.board[row_x_coordinate][row_y_coordinate].marked:
          row_contains_bingo = False
        if not self.board[row_y_coordinate][row_x_coordinate].marked:
          column_contains_bingo = False

      if row_contains_bingo or column_contains_bingo:
        return True
    
    return False

  def calculate_board_score(self, winning_number):
    """
    Add up all unmarked numbers.
    """
    unmarked_sum = 0
    for row_index in range(len(self.board)):
      for board_number in self.board[row_index]:
        if not board_number.marked:
          unmarked_sum += int(board_number.value)

    return unmarked_sum * int(winning_number)

  def print_board(self):
    """
    Print the bingo board with each "marked" number containing a 'x'.
    """
    marked_board = copy.deepcopy(self.board)
    for x_index in range(len(self.board)):
      for y_index in range(len(self.board[x_index])):
        number = marked_board[x_index][y_index]
        if number.marked:
          marked_board[x_index][y_index] = number.value + 'x'
        else:
          marked_board[x_index][y_index] = number.value

    pprint(marked_board)

# =========
# Read input
# =========
FILE_NAME = 'input.txt'
with open(FILE_NAME) as file:
  raw_bingo_input = file.readlines()
  raw_drawn_numbers = raw_bingo_input[0]
  raw_boards = raw_bingo_input[2:]

# =========
# Strip input
# =========
drawn_numbers = raw_drawn_numbers.strip()
boards = []
for row in raw_boards:
    stripped_row = row.strip()
    if stripped_row != '':
      boards.append(stripped_row)

# =========
# Convert board inputs into BingoBoard objects
# =========
bingo_boards = []
for i in range(0, len(boards), 5):
  bingo_board = BingoBoard(boards[i:i+5])
  bingo_boards.append(bingo_board)

# =========
# Loop through drawn numbers & find losing board
# Notes:
#   - Because elements are being removed from the `bingo_board` instance during
#     iteration it's necessary to iterate over a copy of the list.
# =========
losing_board = None
for drawn_number in drawn_numbers.split(','):
  for bingo_board in list(bingo_boards):
    bingo_board.mark_number_if_available(drawn_number)
    if bingo_board.has_bingo():
      if len(bingo_boards) == 1:
        losing_board = bingo_boards[0]
        break

      bingo_boards.remove(bingo_board)
  
  if losing_board:
    break

answer = losing_board.calculate_board_score(drawn_number)
print(answer)
