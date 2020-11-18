from Algorithm.a_star_h2 import a_star_h2_run
from Algorithm.gbfs_h2 import gbfs_h2_run
from Algorithm.ucs import *
from Algorithm.gbfs_h1 import *
from Algorithm.a_star_h1 import *

def read_input(file_name, puzzle):
    with open(file_name, "r") as puzzles:
        lines = puzzles.readlines()
        for l in lines:
           puzzle.append(l.replace("\n", ""))

if __name__ == '__main__':
    puzzles = []
    read_input("Data/puzzle.txt", puzzles)
    list_of_puzzles = []
    for puzzle in puzzles:
        p = puzzle.split()
        map_object = map(int, p)
        list_of_integers = list(map_object)
        list_of_puzzles.append(list_of_integers)
    #     print(list_of_integers)
    # print(list_of_puzzles)

    for i, p in enumerate(list_of_puzzles):
        print("<-----------------------------------------UCS SEARCH ALGORITHM------------------------------------------>")
        ucs_run(i, p, output=False)
        print("<-----------------------------------------GBFS SEARCH ALGORITHM------------------------------------------>")
        print("<------------------------------------------HEURISTIC 1------------------------------------------->")
        gbfs_h1_run(i,p)
        print("<------------------------------------------HEURISTIC 2------------------------------------------->")
        gbfs_h2_run(i, p)
        print("<------------------------------------------A* SEARCH ALGORITHM------------------------------------------->")
        print("<------------------------------------------HEURISTIC 1------------------------------------------->")
        a_star_h1_run(i, p)
        print("<------------------------------------------HEURISTIC 2------------------------------------------->")
        a_star_h2_run(i, p)
        print("=========================================================================================================")


