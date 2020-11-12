regular_cost = 1
wrapping_cost = 2
diagonal_cost = 3
goal_1 = [1, 2, 3, 4, 5, 6, 7, 0]
goal_2 = [1, 3, 5, 7, 2, 4, 6, 0]

regular_moves = {
    0: [1, 4],
    1: [0, 2, 5],
    2: [1, 3, 6],
    3: [2, 7],
    4: [0, 5],
    5: [1, 4, 6],
    6: [2, 5, 7],
    7: [6, 3]
}
wrapping_moves = {
    0: [3],
    3: [0],
    4: [7],
    7: [4]
}
diagonal_moves = {
    0: [5, 7],
    3: [4, 6],
    4: [1, 3],
    7: [0, 2]
}
