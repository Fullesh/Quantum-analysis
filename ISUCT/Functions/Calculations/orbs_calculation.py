import os


def orbitals_calc(file_results, data, ORB_PHRASE, file_directory, orbital_numbers):
    row_number = -1
    i = ''
    str_file_dir = str(file_directory)
    file_name_start_index = str_file_dir.rfind('\\')
    file_name = str_file_dir[file_name_start_index + 1:]
    j = 0
    pos_orbs = 0
    orbital_enegries = []

    orb_file = open(file_directory, 'r', encoding='utf-8')
    for i in orb_file.readlines():
        j += 1
        if ORB_PHRASE in i:
            pos_orbs = j

    orb_file.seek(0, os.SEEK_SET)
    orb_file.close()

    orb_file = open(file_directory, 'r', encoding='utf-8')
    if pos_orbs == 0:
        print(f'Orbitals are not found in the file {file_name}!')
    else:
        i = ''
        j = 0
        for j in range(pos_orbs):
            i = orb_file.readline()
        i = ''

        while True:
            i = orb_file.readline()
            orbital_enegries += list(map(float, i.split()[4:]))
            if len(orbital_enegries) > max(orbital_numbers):
                break
        j = 0
        for j in range(len(orbital_numbers)):
            row_number += 1
            data[row_number] = orbital_enegries[orbital_numbers[j] - 1]
            file_results['File'] = file_name
            file_results['Results'].append(data[row_number])
    orb_file.close()
    row_number += 1
    return data, file_results, row_number
