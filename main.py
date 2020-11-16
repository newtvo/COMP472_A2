from Algorithm.ucs import *
from Algorithm.gbfs import *
from Algorithm.a_star import *

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

    for p in list_of_puzzles:
        print("<-----------------------------------------UCS SEARCH ALGORITHM------------------------------------------>")
        ucs_run(p)
        print("<-----------------------------------------GBFS SEARCH ALGORITHM------------------------------------------>")
        gbfs_run(p)
        print("<------------------------------------------A* SEARCH ALGORITHM------------------------------------------->")
        a_star_run(p)
        print("=========================================================================================================")


