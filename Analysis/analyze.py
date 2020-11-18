import random

from Algorithm.a_star_h1 import a_star_h1_run
from Algorithm.a_star_h2 import a_star_h2_run
from Algorithm.gbfs_h1 import gbfs_h1_run
from Algorithm.gbfs_h2 import gbfs_h2_run
from Algorithm.ucs import ucs_run


def generate_puzzles(goal):
    puzzles = []
    for i in range(50):
        puzzle = goal[:]
        random.shuffle(puzzle)
        puzzles.append(puzzle)
    return puzzles

def ucs_analyze(puzzles):
    total_time = visited_nodes = solution_nodes = total_cost = 0
    for i, p in enumerate(puzzles):
        time, search_length, solution_length, cost = ucs_run(i, p, output=False)
        total_time += time
        visited_nodes += search_length
        solution_nodes += solution_length
        total_cost += cost
    print("UCS average time: {}".format(total_time / 50))
    print("UCS average visted nodes: {}".format(visited_nodes/ 50))
    print("UCS average solution nodes: {}".format(solution_nodes/ 50))
    print("UCS average cost: {}".format(total_cost / 50))
def gbfs1_analyze(puzzles):
    total_time = visited_nodes = solution_nodes = total_cost = 0
    for i, p in enumerate(puzzles):
        time, search_length, solution_length, cost = gbfs_h1_run(i, p, output=False)
        total_time += time
        visited_nodes += search_length
        solution_nodes += solution_length
        total_cost += cost
    print("GBFS1 average time: {}".format(total_time / 50))
    print("GBFS1average visted nodes: {}".format(visited_nodes/ 50))
    print("GBFS1 average solution nodes: {}".format(solution_nodes/ 50))
    print("GBFS1 average cost: {}".format(total_cost / 50))
def gbfs2_analyze(puzzles):
    total_time = visited_nodes = solution_nodes = total_cost = 0
    for i, p in enumerate(puzzles):
        time, search_length, solution_length, cost = gbfs_h2_run(i, p, output=False)
        total_time += time
        visited_nodes += search_length
        solution_nodes += solution_length
        total_cost += cost
    print("GBFS2 average time: {}".format(total_time / 50))
    print("GBFS2average visted nodes: {}".format(visited_nodes/ 50))
    print("GBFS2 average solution nodes: {}".format(solution_nodes/ 50))
    print("GBFS2 average cost: {}".format(total_cost / 50))
def a_star_h1_analyze(puzzles):
    total_time = visited_nodes = solution_nodes = total_cost = 0
    for i, p in enumerate(puzzles):
        time, search_length, solution_length, cost = a_star_h1_run(i, p, output=False)
        total_time += time
        visited_nodes += search_length
        solution_nodes += solution_length
        total_cost += cost
    print("A*1 average time: {}".format(total_time / 50))
    print("A*1 average visted nodes: {}".format(visited_nodes/ 50))
    print("A*1 average solution nodes: {}".format(solution_nodes/ 50))
    print("A*1 average cost: {}".format(total_cost / 50))
def a_star_h2_analyze(puzzles):
    total_time = visited_nodes = solution_nodes = total_cost = 0
    for i, p in enumerate(puzzles):
        time, search_length, solution_length, cost = a_star_h2_run(i, p, output=False)
        total_time += time
        visited_nodes += search_length
        solution_nodes += solution_length
        total_cost += cost
    print("A*2 average time: {}".format(total_time / 50))
    print("A*2 average visted nodes: {}".format(visited_nodes/ 50))
    print("A*2 average solution nodes: {}".format(solution_nodes/ 50))
    print("A*2 average cost: {}".format(total_cost / 50))

if __name__ == '__main__':
    puzzles = generate_puzzles([1,2,3,4,5,6,7,0])
    ucs_analyze(puzzles)
    gbfs1_analyze(puzzles)
    gbfs2_analyze(puzzles)
    a_star_h1_analyze(puzzles)
    a_star_h2_analyze(puzzles)
