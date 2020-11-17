# 3x3 puzzle
scaled_goal_1 = [1, 2, 3, 4, 5, 6, 7, 8, 0]
scaled_regular_moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}
scaled_wrapping_moves = {
    0: [2, 6],
    2: [0, 8],
    6: [0, 8],
    8: [2, 6]
}
scaled_diagonal_moves = {
    0: [4, 8],
    2: [4, 6],
    6: [4, 1],
    8: [4, 0]
}


def scaled_heuristic2(current_state):
    dist_1 = sum(abs(b % 3 - g % 3) + abs(b // 3 - g // 3)
                 for b, g in ((current_state.index(i), scaled_goal_1.index(i)) for i in range(1, 8)))
    return dist_1
