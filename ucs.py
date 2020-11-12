import heapq
from rules import *


def list_to_string(input):
    return ''.join(str(e) for e in input)


def uniform_cost(puzzle):
    visited = set()
    queue = []
    heapq.heappush(queue, (0,[(0, puzzle)]))
    while queue:
        cost, path = heapq.heappop(queue)
        current_state = path[-1][1]
        if list_to_string(current_state) not in visited:
            visited.add(list_to_string(current_state))
        if current_state == goal_1 or current_state == goal_2:
            return cost, path, visited
        index = current_state.index(0)
        for move in regular_moves[index]:
            new_path = list(path)
            new_state = current_state.copy()
            new_state[index], new_state[move] = new_state[move], new_state[index]
            new_path.append((regular_cost, new_state))
            new_cost = cost + regular_cost
            if list_to_string(new_state) not in visited:
                heapq.heappush(queue, (new_cost,new_path))
        if index in wrapping_moves:
            for move in wrapping_moves[index]:
                new_path = list(path)
                new_state = current_state.copy()
                new_state[index], new_state[move] = new_state[move], new_state[index]
                new_path.append((wrapping_cost,new_state))
                new_cost = cost + wrapping_cost
                if list_to_string(new_state) not in visited:
                    heapq.heappush(queue, (new_cost,new_path))
            for move in diagonal_moves[index]:
                new_path = list(path)
                new_state = current_state.copy()
                new_state[index], new_state[move] = new_state[move], new_state[index]
                new_path.append((diagonal_cost, new_state))
                new_cost = cost + diagonal_cost
                if list_to_string(new_state) not in visited:
                    heapq.heappush(queue, (new_cost,new_path))




if __name__ == '__main__':
    cost, path ,visited= uniform_cost([1, 0, 3, 6, 5, 2, 7, 4])
    print(cost)
    for i in path:
        print(i)
    for i in visited:
        print(i)