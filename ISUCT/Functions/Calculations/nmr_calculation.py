import os


def nmr_calc(file_result, data, NMR_PHRASE, file_directory, NMR_numbers):
    NMR = []
    row_number = -1
    i = ''
    j = 0
    pos_NMR = 0
    NMR_file = open(file_directory)
    for i in NMR_file.readlines():
        j += 1
        if NMR_PHRASE in i:
            pos_NMR = j

    NMR_file.seek(0, os.SEEK_SET)
    NMR_file.close()

    NMR_file = open(file_directory)
    if pos_NMR == 0:
        print(f'NMR parameters not found in {file_directory}')
    else:
        i = ''
        j = 0
        for j in range(pos_NMR):
            i = NMR_file.readline()

        i = ''
        while True:
            i = NMR_file.readline()
            NMR.append(float(i.split()[4]))
            i = NMR_file.readline()
            i = NMR_file.readline()
            i = NMR_file.readline()
            i = NMR_file.readline()

            if len(NMR) > max(NMR_numbers):
                break

            j = 0
            for j in range(len(NMR_numbers)):
                row_number += 1
                data[row_number] = NMR[NMR_numbers[j]]
            NMR_file.close()
    return data, file_result, row_number