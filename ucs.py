import heapq
import timeit
from rules import *


def list_to_string(input):
    return ' '.join(str(e) for e in input)


def ucs(puzzle):
    visited = set()
    queue = []
    heapq.heappush(queue, (0,[(0, 0, puzzle)]))
    while queue:
        cost, path = heapq.heappop(queue)
        current_state = path[-1][2]
        if list_to_string(current_state) not in visited:
            visited.add(list_to_string(current_state))
        if current_state == goal_1 or current_state == goal_2:
            return cost, path, visited
        index = current_state.index(0)
        for move in regular_moves[index]:
            new_path = list(path)
            new_state = current_state.copy()
            tile_moved = new_state[move]
            new_state[index], new_state[move] = new_state[move], new_state[index]
            new_path.append((tile_moved, regular_cost, new_state))
            new_cost = cost + regular_cost
            if list_to_string(new_state) not in visited:
                heapq.heappush(queue, (new_cost,new_path))
        if index in wrapping_moves:
            for move in wrapping_moves[index]:
                new_path = list(path)
                new_state = current_state.copy()
                tile_moved = new_state[move]
                new_state[index], new_state[move] = new_state[move], new_state[index]
                new_path.append((tile_moved, regular_cost, new_state))
                new_cost = cost + wrapping_cost
                if list_to_string(new_state) not in visited:
                    heapq.heappush(queue, (new_cost,new_path))
            for move in diagonal_moves[index]:
                new_path = list(path)
                new_state = current_state.copy()
                tile_moved = new_state[move]
                new_state[index], new_state[move] = new_state[move], new_state[index]
                new_path.append((tile_moved, regular_cost, new_state))
                new_cost = cost + diagonal_cost
                if list_to_string(new_state) not in visited:
                    heapq.heappush(queue, (new_cost,new_path))




if __name__ == '__main__':
    output = open("ucs_output.txt", "w")
    search = open("ucs_search.txt", "w")
    start = timeit.default_timer()
    cost, path, visited = ucs([3, 0, 1, 4, 2, 6, 5, 7])
    stop = timeit.default_timer()
    print("TOTAL COST")
    print(cost)
    print("SUCCESSPATH")
    for i in path:
        output.write("{} {} {}\n".format(i[0],i[1],' '.join(str(e) for e in i[2])))
        print(i)
        # output.write(str(i) +"\n")
    output.write("Total cost: {}, Runtime: {}".format(cost, stop-start))
    print("VISITED STATES")
    for i in visited:
        search.write(str(i) + "\n")
        print(i)