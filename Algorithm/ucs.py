import heapq
import timeit
from Algorithm.rules import *
from Output.output import *

def list_to_string(input):
    return ' '.join(str(e) for e in input)


def ucs(puzzle):
    visited = set()
    queue = []
    search = []
    heapq.heappush(queue, (0,[(0, 0, puzzle)]))
    while queue:
        cost, path = heapq.heappop(queue)
        current_state = path[-1][2]
        if list_to_string(current_state) not in visited:
            visited.add(list_to_string(current_state))
            # search.append(str(cost) + ' ' + '0 ' + list_to_string(current_state))
            search.append("0" + ' ' + str(cost) + ' ' + "0"+ ' ' + list_to_string(current_state))
        if current_state == goal_1 or current_state == goal_2:
            return cost, path, search
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

def ucs_run(puzzle):
    start = timeit.default_timer()
    cost, path, visited = ucs(puzzle)
    stop = timeit.default_timer()
    timer = stop - start
    if stop > 60:
        print("NO SOLUTION")
    else:
        print("SUCCESSPATH")
        for i in path:
         print(i)
        print("TOTAL COST")
        print(cost)
        print("VISITED STATES")
        for i in visited:
            print(i)
        output_file("ucs_solution.txt", "ucs_search.txt", cost, path, visited, timer)








