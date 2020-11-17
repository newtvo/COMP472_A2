# 2x5 puzzle
scaled_goal_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
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
def scaled_heuristic2(current_state):
    dist_1 = sum(abs(b % 5 - g % 5) + abs(b // 5 - g // 5)
                 for b, g in ((current_state.index(i), scaled_goal_1.index(i)) for i in range(1, 9)))
    return dist_1
