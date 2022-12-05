ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

play_mappings_and_scores = {
    ROCK: {
        LOSE: SCISSORS,
        WIN: PAPER,
        DRAW: ROCK,
        'score': 1
    },
    PAPER: {
        LOSE: ROCK,
        WIN: SCISSORS,
        DRAW: PAPER,
        'score': 2
    },
    SCISSORS: {
        LOSE: PAPER,
        WIN: ROCK,
        DRAW: SCISSORS,
        'score': 3
    }
}

def get_round_outcome_score(outcome):
    """
    Get the score of the round based on the round outcome.
    """
    if outcome == WIN:
        return 6
    elif outcome == DRAW:
        return 3

    return 0

# read input
input_file_path = '/Users/andrewdieken/dev/advent-of-code/2022/day_2/input.txt'
with open(input_file_path, 'r') as input_file:
    raw_input = input_file.readlines()

score = 0
for raw_round in raw_input:
    # clean input row
    cleaned_round = raw_round.strip().split(' ')
    opponent_shape, desired_outcome = cleaned_round[0], cleaned_round[1]

    # shape to play
    your_shape = play_mappings_and_scores[opponent_shape][desired_outcome]
    shape_score = play_mappings_and_scores[your_shape]['score']
    score += (shape_score + get_round_outcome_score(desired_outcome))

print(score)
