import heapq
import timeit
import random
from Algorithm.rules import *
from OtherPuzzles.rules_33 import *
from Output.output import output_file


def list_to_string(input):
    return ' '.join(str(e) for e in input)

def a_star(puzzle):
    visited = set()
    search = [] #include g(n) + h(n)
    queue = []
    heapq.heappush(queue, (scaled_heuristic2(puzzle),[(0, 0, puzzle)],0))
    while queue:
        f, path, cost = heapq.heappop(queue)
        current_state = path[-1][2]
        print(current_state)
        if list_to_string(current_state) not in visited:
            visited.add(list_to_string(current_state))
            search.append(str(f) + ' ' + str(cost) + ' ' + str(f - cost) + ' ' + list_to_string(current_state))
        if current_state == scaled_goal_1:
            return cost, path, search
        index = current_state.index(0)
        for move in scaled_regular_moves[index]:
            new_path = list(path)
            new_state = current_state.copy()
            tile_moved = new_state[move]
            new_state[index], new_state[move] = new_state[move], new_state[index]
            new_path.append((tile_moved, regular_cost, new_state))
            heuristic = scaled_heuristic2(new_state)
            new_cost = cost + regular_cost
            f_cost = heuristic + new_cost
            if list_to_string(new_state) not in visited:
                heapq.heappush(queue, (f_cost, new_path, new_cost))
        if index in scaled_wrapping_moves:
            for move in scaled_wrapping_moves[index]:
                new_path = list(path)
                new_state = current_state.copy()
                tile_moved = new_state[move]
                new_state[index], new_state[move] = new_state[move], new_state[index]
                new_path.append((tile_moved, wrapping_cost, new_state))
                heuristic = scaled_heuristic2(new_state)
                new_cost = cost + wrapping_cost
                f_cost = heuristic + new_cost
                if list_to_string(new_state) not in visited:
                    heapq.heappush(queue, (f_cost, new_path, new_cost))
            for move in scaled_diagonal_moves[index]:
                new_path = list(path)
                new_state = current_state.copy()
                tile_moved = new_state[move]
                new_state[index], new_state[move] = new_state[move], new_state[index]
                new_path.append((tile_moved, diagonal_cost, new_state))
                new_cost = cost + diagonal_cost
                heuristic = scaled_heuristic2(new_state)
                f_cost = heuristic + new_cost
                if list_to_string(new_state) not in visited:
                    heapq.heappush(queue, (f_cost, new_path, new_cost))
def scale_run(puzzle):
    start = timeit.default_timer()
    cost, path, visited = a_star(puzzle)
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
        output_file("3x3_solution.txt", "3x3_search.txt", cost, path, visited, timer)
if __name__ == '__main__':
    puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    random.shuffle(puzzle)
    scale_run(puzzle)
