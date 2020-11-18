# 2x5 puzzle
scaled_goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
regular_cost = 1
wrapping_cost = 2
diagonal_cost = 3
scaled_regular_moves = {
    0: [1, 5],
    1: [0, 2, 6],
    2: [1, 3, 7],
    3: [2, 4, 8],
    4: [3, 9],
    5: [0, 6],
    6: [1, 5, 7],
    7: [2, 6, 8],
    8: [3, 7, 9],
    9: [4, 8],
}
scaled_wrapping_moves = {
    0: [4],
    4: [0],
    5: [9],
    9: [5]
}
scaled_diagonal_moves = {
    0: [6, 9],
    4: [8, 5],
    5: [1, 4],
    9: [3, 0]
}


def heuristic1(current_state):
    count = 0
    for i in range(len(current_state)):
        if current_state[i] != scaled_goal[i]:
            count += 1
    return count
