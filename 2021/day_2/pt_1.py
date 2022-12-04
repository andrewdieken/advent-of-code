import operator
from os import urandom

FILE_NAME = 'input.txt'
with open(FILE_NAME) as file:
    raw_commands = file.readlines()

commands = []
for command in raw_commands:
    commands.append(command.strip())

horizontal_position = 0
depth = 0

def forward_action(unit):
  global horizontal_position
  horizontal_position += unit

def down_action(unit):
  global depth
  depth += unit

def up_action(unit):
  global depth
  depth -= unit

command_mappings = {
  'forward': forward_action,
  'down': down_action,
  'up': up_action
}

for command in commands:
  direction, unit = command.split(' ')
  command_action = command_mappings[direction]
  command_action(int(unit))

answer = horizontal_position * depth