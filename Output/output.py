import os

def output_file(file_name_solution, file_name_search, cost, path, visited, timer):
    #solution_files
    if os.path.exists("Output/"  + file_name_solution):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not
    output = open('Output/' + file_name_solution, append_write)
    # write output for solution files
    for i in path:
        output.write("{} {} {}\n".format(i[0], i[1], ' '.join(str(e) for e in i[2])))
    output.write("Total cost: {}, Runtime: {}".format(cost, timer))
    output.write("\n=======================================================\n")

    #search_files
    if os.path.exists("Output/" + file_name_search):
        append_write_search = 'a'  # append if already exists
    else:
        append_write_search = 'w'  # make a new file if not
    search = open('Output/' + file_name_search, append_write_search)
    #write output for search files
    for i in visited:
        # search.write("{} {}\n".format("0", str(i)))
        search.write(str(i) + "\n")
    search.write("\n=======================================================\n")

    #close IO
    output.close()
    search.close()