ROCK = 'X'
OPPONENT_ROCK = 'A'

PAPER = 'Y'
OPPONENT_PAPER = 'B'

SCISSORS = 'Z'
OPPONENT_SCISSORS = 'C'

play_mappings_and_scores = {
    ROCK: {
        'match': OPPONENT_ROCK,
        'defeats': OPPONENT_SCISSORS,
        'score': 1
    },
    PAPER: {
        'match': OPPONENT_PAPER,
        'defeats': OPPONENT_ROCK,
        'score': 2
    },
    SCISSORS: {
        'match': OPPONENT_SCISSORS,
        'defeats': OPPONENT_PAPER,
        'score': 3
    }
}

# read input
input_file_path = '/Users/andrewdieken/dev/advent-of-code/2022/day_2/input.txt'
with open(input_file_path, 'r') as input_file:
    raw_input = input_file.readlines()

score = 0
for raw_round in raw_input:
    # clean input row
    cleaned_round = raw_round.strip().split(' ')
    opponent_play, your_play = cleaned_round[0], cleaned_round[1]
    shape_score = play_mappings_and_scores[your_play]['score']

    # tie
    if opponent_play == play_mappings_and_scores[your_play]['match']:
        score += (3 + shape_score)
    # win
    elif play_mappings_and_scores[your_play]['defeats'] == opponent_play:
        score += (6 + shape_score)
    # loss
    else:
        score += shape_score

print(score)
