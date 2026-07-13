import random

def player(prev_play,
           opponent_history=[],
           play_order={},
           counter=[0]):

    if prev_play:
        opponent_history.append(prev_play)

    # First few moves are random
    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

    # Record previous sequences
    last_sequence = "".join(opponent_history[-5:])

    if last_sequence not in play_order:
        play_order[last_sequence] = {}

    if len(opponent_history) > 5:
        prev_sequence = "".join(opponent_history[-6:-1])

        if prev_sequence not in play_order:
            play_order[prev_sequence] = {}

        next_move = opponent_history[-1]

        if next_move not in play_order[prev_sequence]:
            play_order[prev_sequence][next_move] = 0

        play_order[prev_sequence][next_move] += 1

    prediction = random.choice(["R", "P", "S"])

    if last_sequence in play_order:
        counts = play_order[last_sequence]

        if counts:
            prediction = max(counts, key=counts.get)

    ideal_response = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    return ideal_response[prediction]