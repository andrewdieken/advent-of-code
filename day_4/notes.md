# Option 1
## good - whether a board contains a number
## bad - whether a board contains a bingo

__Example board:__

bingo_board = [
  {22: 0, 13: 0, 17: 0, 11: 0, 0: 0},
  {8: 0, 12: 0, 23: 0, 4: 0, 24: 0},
  {21: 0, 9: 0, 14: 0, 16: 0, 7: 0},
  {6: 0, 10: 0, 3: 0, 18: 0, 5: 0},
  {1: 0, 12: 0, 20: 0, 15: 0, 19: 0}
]

# Option 2
## good - whether a board contains a bingo
## bad - whether a board contains a number

__Example board:__

bingo_board = [
  [BingoIndex(22), BingoIndex(13), BingoIndex(17), BingoIndex(11), BingoIndex(0)],
  [BingoIndex(8), BingoIndex(2), BingoIndex(23), BingoIndex(4), BingoIndex(24)],
  [BingoIndex(21), BingoIndex(9), BingoIndex(14), BingoIndex(16), BingoIndex(7)],
  [BingoIndex(6), BingoIndex(10), BingoIndex(3), BingoIndex(18), BingoIndex(5)],
  [BingoIndex(1), BingoIndex(12), BingoIndex(20), BingoIndex(15), BingoIndex(19)]
]

# Option 3
## good - whether a board contains a number
## good - whether a board contains a bingo

__Example board:__

bingo_board = [
  ['22', '13', '17', '11', '0'],
  ['8',  '2', '23',  '4', '24'],
  ['21', '9', '14', '16', '7'],
  ['6', '10', '3', '18', '5'],
  ['1', '12', '20', '15', '19']
]