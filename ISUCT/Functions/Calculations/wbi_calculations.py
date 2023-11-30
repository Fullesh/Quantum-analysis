import os


def wbi_calc(file_result, data, WBI_PHRASE, file_directory, wbi_numbers, natoms):
    row_number = -1
    str_file_dir = str(file_directory)
    file_name_start_index = str_file_dir.rfind('\\')
    file_name = str_file_dir[file_name_start_index + 1:]
    WBI = []
    j = 0
    for j in range(natoms):
        WBI.append([])

    i = ''
    j = 0
    pos_WBI = 0
    wbi_file = open(file_directory, 'r', encoding='utf-8')

    for i in wbi_file.readlines():
        j += 1
        if WBI_PHRASE in i:
            pos_WBI = j + 3

    wbi_file.seek(0, os.SEEK_SET)
    wbi_file.close()

    wbi_file = open(file_directory, 'r', encoding='utf-8')
    if pos_WBI == 0:
        print(f'WBI not find in the file {file_directory}')
    else:
        i = ''
        j = 0
        for j in range(pos_WBI):
            i = wbi_file.readline()

        i = ''
        for n in range(natoms):
            for m in range(natoms):
                i = wbi_file.readline()
                WBI[m] += list(map(float, i.split()[2:]))
            i = wbi_file.readline()
            i = wbi_file.readline()
            i = wbi_file.readline()

            if all(list(map(lambda x: len(x) == natoms, WBI))):
                break

        natoms = 0
    j = 0
    if pos_WBI != 0:
        for j in range(len(wbi_numbers)):
            data[row_number] = WBI[wbi_numbers[j][0]-1][wbi_numbers[j][1]-1]
            file_result['File'] = file_name
            file_result['Results'].append(data[row_number])
        wbi_file.close()
        row_number += 1
    return data, file_result, row_number

