#main_ucs
# if __name__ == '__main__':
#     output = open("ucs_output.txt", "w")
#     search = open("ucs_search.txt", "w")
#     start = timeit.default_timer()
#     cost, path, visited = ucs([3, 0, 1, 4, 2, 6, 5, 7])
#     stop = timeit.default_timer()
#     print("TOTAL COST")
#     print(cost)
#     print("SUCCESSPATH")
#     for i in path:
#         output.write("{} {} {}\n".format(i[0],i[1],' '.join(str(e) for e in i[2])))
#         print(i)
#         # output.write(str(i) +"\n")
#     output.write("Total cost: {}, Runtime: {}".format(cost, stop-start))
#     print("VISITED STATES")
#     for i in visited:
#         search.write("{} {}\n".format("0", str(i)))
#         print(i)


#=======================================================
#main_gbfs
# if __name__ == '__main__':
#     output = open("gbfs_output.txt", "w")
#     search = open("gbfs_search.txt", "w")
#     start = timeit.default_timer()
#     cost, path, visited = gbfs([3, 0, 1, 4, 2, 6, 5, 7])
#     stop = timeit.default_timer()
#     print("SUCCESSPATH")
#     for i in path:
#         print(i)
#         output.write("{} {} {}\n".format(i[0], i[1], ' '.join(str(e) for e in i[2])))
#     print("TOTAL COST")
#     print(cost)
#     output.write("Total cost: {}, Runtime: {}".format(cost, stop - start))
#     print("VISITED STATES")
#     for i in visited:
#         search.write("{} {} {}\n".format("0", "0", str(i)))
#         print(i)

#=======================================================
#main_a_star
# if __name__ == '__main__':
#     output = open("a_star_output.txt", "w")
#     search = open("a_star_search.txt", "w")
#     start = timeit.default_timer()
#     cost, path, visited = a_star([3, 0, 1, 4, 2, 6, 5, 7])
#     stop = timeit.default_timer()
#     if stop > 60:
#         print("NO SOLUTION")
#         output.write("no solution")
#     else:
#      print("SUCCESSPATH")
#      for i in path:
#         print(i)
#         output.write("{} {} {}\n".format(i[0], i[1], ' '.join(str(e) for e in i[2])))
#      print("TOTAL COST")
#      print(cost)
#      output.write("Total cost: {}, Runtime: {}".format(cost, stop - start))
#      print("VISITED STATES")
#      for i in visited:
#         search.write(str(i) + "\n")
#         print(i)