import heapq
import timeit
import random
from OtherPuzzles.rules_25 import *


def list_to_string(input):
    return ' '.join(str(e) for e in input)
def gbfs_scale(puzzle):
    visited = set()
    search = [] #include h(n)
    queue = []
    heapq.heappush(queue, (heuristic1(puzzle),[(0, 0, puzzle)],0))
    while queue:
        h, path, cost = heapq.heappop(queue)
        current_state = path[-1][2]
        if list_to_string(current_state) not in visited:
            visited.add(list_to_string(current_state))
            search.append(str(h + 0) + ' ' + "0"+ ' ' + str(h) + ' ' + list_to_string(current_state))
        if current_state == scaled_goal:
            return cost, path, search
        index = current_state.index(0)
        for move in scaled_regular_moves[index]:
            new_path = list(path)
            new_state = current_state.copy()
            tile_moved = new_state[move]
            new_state[index], new_state[move] = new_state[move], new_state[index]
            new_path.append((tile_moved, regular_cost, new_state))
            heuristic = heuristic1(new_state)
            new_cost = cost + regular_cost
            if list_to_string(new_state) not in visited:
                heapq.heappush(queue, (heuristic,new_path,new_cost))
        if index in scaled_diagonal_moves:
            for move in scaled_wrapping_moves[index]:
                new_path = list(path)
                new_state = current_state.copy()
                tile_moved = new_state[move]
                new_state[index], new_state[move] = new_state[move], new_state[index]
                new_path.append((tile_moved, wrapping_cost, new_state))
                heuristic = heuristic1(new_state)
                new_cost = cost + wrapping_cost
                if list_to_string(new_state) not in visited:
                    heapq.heappush(queue, (heuristic,new_path, new_cost))
            for move in scaled_diagonal_moves[index]:
                new_path = list(path)
                new_state = current_state.copy()
                tile_moved = new_state[move]
                new_state[index], new_state[move] = new_state[move], new_state[index]
                new_path.append((tile_moved, wrapping_cost, new_state))
                new_cost = cost + diagonal_cost
                heuristic = heuristic1(new_state)
                if list_to_string(new_state) not in visited:
                    heapq.heappush(queue, (heuristic,new_path, new_cost))
def scale_run(puzzle):
    start = timeit.default_timer()
    cost, path, visited = gbfs_scale(puzzle)
    stop = timeit.default_timer()
    timer = stop - start
    return timer, len(visited), len(path), cost
if __name__ == '__main__':
    def generate_puzzles(goal):
        puzzles = []
        for i in range(50):
            puzzle = goal[:]
            random.shuffle(puzzle)
            puzzles.append(puzzle)
        return puzzles
    puzzles = generate_puzzles([1,2,3,4,5,6,7,8,9,0])
    total_time = visited_nodes = solution_nodes = total_cost = 0
    for i, p in enumerate(puzzles):
        time, search_length, solution_length, cost = scale_run(p)
        total_time += time
        visited_nodes += search_length
        solution_nodes += solution_length
        total_cost += cost
    print("GBFS1 2*5 average time: {}".format(total_time / 50))
    print("GBFS1 2*5 average visted nodes: {}".format(visited_nodes / 50))
    print("GBFS1 2*5 average solution nodes: {}".format(solution_nodes / 50))
    print("GBFS1 2*5 average cost: {}".format(total_cost / 50))
