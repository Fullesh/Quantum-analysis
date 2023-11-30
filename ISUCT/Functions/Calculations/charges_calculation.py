import os


def charge_calc(file_results, data, CHARGE_PHRASE, file_directory, charge_numbers):
    row_number = -1
    i = ''
    str_file_dir = str(file_directory)
    file_name_start_index = str_file_dir.rfind('\\')
    file_name = str_file_dir[file_name_start_index + 1:]
    j = 0
    pos_charges = 0
    natural_charges = []

    charge_file = open(file_directory, 'r', encoding='utf-8')
    for i in charge_file.readlines():
        j += 1
        if CHARGE_PHRASE in i:
            pos_charges = j + 5

    charge_file.seek(0, os.SEEK_SET)
    charge_file.close()

    charge_file = open(file_directory, 'r', encoding='utf-8')
    if pos_charges == 0:
        print(f'Natural charges are not found in the file {file_name}!')
    else:
        i = ''
        j = 0
        for j in range(pos_charges):
            i = charge_file.readline()
        i = ''

        while True:
            i = charge_file.readline()
            natural_charges.append(float(i.split()[2]))
            if len(natural_charges) > max(charge_numbers):
                break
        j = 0
        for j in range(len(charge_numbers)):
            # row_number += 1
            data[row_number] = natural_charges[charge_numbers[j] - 1]
            file_results['File'] = file_name
            file_results['Results'].append(data[row_number])
    charge_file.close()
    row_number += 1
    return data, file_results, row_number
