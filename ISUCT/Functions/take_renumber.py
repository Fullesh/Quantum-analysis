def make_renumber(renumber_file):
    renumber = []
    with open(renumber_file, 'r') as renumbering_file:
        num_of_columns = len(renumbering_file.readline().split())
        renumbering_file.seek(0, 0)
        for j in range(num_of_columns):
            renumber.append([])
        for string in renumbering_file.readlines():
            tmp = string.split()
            for j in range(num_of_columns):
                renumber[j].append(int(tmp[j]))
    return renumber
