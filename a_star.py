import heapq
import timeit

from rules import *


def list_to_string(input):
    return ' '.join(str(e) for e in input)


def a_star(puzzle):
    visited = set()
    search = [] #include g(n) + h(n)
    queue = []
    heapq.heappush(queue, (heuristic1(puzzle),[(0, 0, puzzle)],0))
    while queue:
        f, path, cost = heapq.heappop(queue)
        current_state = path[-1][2]
        if list_to_string(current_state) not in visited:
            visited.add(list_to_string(current_state))
            search.append(str(f) + ' ' + str(cost) + ' ' + str(f - cost) + ' ' + list_to_string(current_state))
        if current_state == goal_1 or current_state == goal_2:
            return cost, path, search
        index = current_state.index(0)
        for move in regular_moves[index]:
            new_path = list(path)
            new_state = current_state.copy()
            tile_moved = new_state[move]
            new_state[index], new_state[move] = new_state[move], new_state[index]
            new_path.append((tile_moved, regular_cost, new_state))
            heuristic = heuristic1(new_state)
            new_cost = cost + regular_cost
            f_cost = heuristic + new_cost
            if list_to_string(new_state) not in visited:
                heapq.heappush(queue, (f_cost, new_path, new_cost))
        if index in wrapping_moves:
            for move in wrapping_moves[index]:
                new_path = list(path)
                new_state = current_state.copy()
                tile_moved = new_state[move]
                new_state[index], new_state[move] = new_state[move], new_state[index]
                new_path.append((tile_moved, wrapping_cost, new_state))
                heuristic = heuristic1(new_state)
                new_cost = cost + wrapping_cost
                f_cost = heuristic + new_cost
                if list_to_string(new_state) not in visited:
                    heapq.heappush(queue, (f_cost, new_path, new_cost))
            for move in diagonal_moves[index]:
                new_path = list(path)
                new_state = current_state.copy()
                tile_moved = new_state[move]
                new_state[index], new_state[move] = new_state[move], new_state[index]
                new_path.append((tile_moved, diagonal_cost, new_state))
                new_cost = cost + diagonal_cost
                heuristic = heuristic1(new_state)
                f_cost = heuristic + new_cost
                if list_to_string(new_state) not in visited:
                    heapq.heappush(queue, (f_cost, new_path, new_cost))

if __name__ == '__main__':
    output = open("a_star_output.txt", "w")
    search = open("a_star_search.txt", "w")
    start = timeit.default_timer()
    cost, path, visited = a_star([1, 0, 3, 6, 5, 2, 7, 4])
    stop = timeit.default_timer()
    if stop > 60:
        print("NO SOLUTION")
        output.write("no solution")
    else:
     print("SUCCESSPATH")
     for i in path:
        print(i)
        output.write("{} {} {}\n".format(i[0], i[1], ' '.join(str(e) for e in i[2])))
     print("TOTAL COST")
     print(cost)
     output.write("Total cost: {}, Runtime: {}".format(cost, stop - start))
     print("VISITED STATES")
     for i in visited:
        search.write(str(i) + "\n")
        print(i)


