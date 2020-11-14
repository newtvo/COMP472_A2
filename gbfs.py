import heapq
import timeit

from rules import *


def list_to_string(input):
    return ''.join(str(e) for e in input)


def gbfs(puzzle):
    visited = set()
    queue = []
    heapq.heappush(queue, (0,[(0, puzzle)],0))
    while queue:
        h, path, cost = heapq.heappop(queue)
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
            heuristic = heuristic1(new_state)
            new_cost = cost + regular_cost
            if list_to_string(new_state) not in visited:
                heapq.heappush(queue, (heuristic,new_path,new_cost))
        if index in wrapping_moves:
            for move in wrapping_moves[index]:
                new_path = list(path)
                new_state = current_state.copy()
                new_state[index], new_state[move] = new_state[move], new_state[index]
                new_path.append((wrapping_cost,new_state))
                heuristic = heuristic1(new_state)
                new_cost = cost + wrapping_cost
                if list_to_string(new_state) not in visited:
                    heapq.heappush(queue, (heuristic,new_path, new_cost))
            for move in diagonal_moves[index]:
                new_path = list(path)
                new_state = current_state.copy()
                new_state[index], new_state[move] = new_state[move], new_state[index]
                new_path.append((diagonal_cost, new_state))
                new_cost = cost + diagonal_cost
                heuristic = heuristic1(new_state)
                if list_to_string(new_state) not in visited:
                    heapq.heappush(queue, (heuristic,new_path, new_cost))




if __name__ == '__main__':
    output = open("gbfs_output.txt", "w")
    search = open("gbfs_search.txt", "w")
    start = timeit.default_timer()
    cost, path, visited = gbfs([1, 0, 3, 6, 5, 2, 7, 4])
    stop = timeit.default_timer()
    print("SUCCESSPATH")
    for i in path:
        print(i)
        output.write("{} {} {}\n".format("0", i[0], ' '.join(str(e) for e in i[1])))
    print("TOTAL COST")
    print(cost)
    output.write("Total cost: {}, Runtime: {}".format(cost, stop - start))
    print("VISITED STATES")
    for i in visited:
        search.write(str(i) + "\n")
        print(i)