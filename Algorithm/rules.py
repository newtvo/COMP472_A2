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

#number of misplaced tiles
def heuristic1(current_state):
    count_1 = 0
    count_2 = 0
    for i in range(len(current_state)):
        if current_state[i] != goal_1[i]:
            count_1 += 1
        if current_state[i] != goal_2[i]:
            count_2 += 1
    return min(count_1,count_2)

#sum of Manhattan distances for each tile to its goal position
def heuristic2(current_state):
    sum_1 = 0
    sum_2 = 0
    for i in range(len(current_state)):
        sum_1 += abs((current_state[i]) % 3 - goal_1[i] % 3) + abs((current_state[i]) // 3 - goal_1[i] // 3)
    for i in range(len(current_state)):
        sum_2 += abs((current_state[i]) % 3 - goal_2[i] % 3) + abs((current_state[i]) // 3 - goal_2[i] // 3)
    return min(sum_1, sum_2)

