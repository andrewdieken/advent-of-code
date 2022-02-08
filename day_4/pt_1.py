class BingoNumber(object):
  def __init__(self, value):
    self.value = value.strip()
    self.marked = 0

class BingoBoard(object):
  """
  Functionality:
    1. track whether a number has been "marked"
    2. determine any row or column contains all "marked" numbers
  """
  def __init__(self, board_input):
    self.board = self._generate_board(board_input)

  def _generate_board(self, board_input):
    board = [[] for i in range(len(board_input))]

    for row_index in range(len(board_input)):
      for board_number in board_input[row_index].split(' '):
        if board_number != '':
          board[row_index].append(BingoNumber(board_number))

    return board

  def mark_number_if_available(self, drawn_number):
    for row_index in range(len(self.board)):
      for board_number in self.board[row_index]:
        if board_number.value == drawn_number:
          board_number.marked = 1

  def has_bingo(self):
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
    """ Add up all unmarked numbers. """
    unmarked_sum = 0
    for row_index in range(len(self.board)):
      for board_number in self.board[row_index]:
        if not board_number.marked:
          unmarked_sum += int(board_number.value)

    return unmarked_sum * int(winning_number)

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
# Loop through drawn numbers & find winning board
# =========
winning_board = None
for drawn_number in drawn_numbers.split(','):
  for bingo_board in bingo_boards:
    bingo_board.mark_number_if_available(drawn_number)
    if bingo_board.has_bingo():
      winning_board = bingo_board
      break

  if winning_board:
    break

answer = winning_board.calculate_board_score(drawn_number)

"""
NOTES:

#
# Option 1
# good - whether a board contains a number
# bad - whether a board contains a bingo
bingo_board = [
  {22: 0, 13: 0, 17: 0, 11: 0, 0: 0},
  {8: 0, 12: 0, 23: 0, 4: 0, 24: 0},
  {21: 0, 9: 0, 14: 0, 16: 0, 7: 0},
  {6: 0, 10: 0, 3: 0, 18: 0, 5: 0},
  {1: 0, 12: 0, 20: 0, 15: 0, 19: 0}
]

#
# Option 2
# good - whether a board contains a bingo
# bad - whether a board contains a number
bingo_board = [
  [BingoIndex(22), BingoIndex(13), BingoIndex(17), BingoIndex(11), BingoIndex(0)],
  [BingoIndex(8), BingoIndex(2), BingoIndex(23), BingoIndex(4), BingoIndex(24)],
  [BingoIndex(21), BingoIndex(9), BingoIndex(14), BingoIndex(16), BingoIndex(7)],
  [BingoIndex(6), BingoIndex(10), BingoIndex(3), BingoIndex(18), BingoIndex(5)],
  [BingoIndex(1), BingoIndex(12), BingoIndex(20), BingoIndex(15), BingoIndex(19)]
]

#
# Option 3
# good - whether a board contains a number
# good - whether a board contains a bingo
bingo_board = [
  ['22', '13', '17', '11', '0'],
  ['8',  '2', '23',  '4', '24'],
  ['21', '9', '14', '16', '7'],
  ['6', '10', '3', '18', '5'],
  ['1', '12', '20', '15', '19']
]
"""