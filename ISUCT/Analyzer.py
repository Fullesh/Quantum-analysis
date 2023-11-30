import os

from ISUCT.Functions.select_file import select_file
from ISUCT.Functions.requests import user_requests
from ISUCT.Functions.check_renumber import check_renumber
from ISUCT.Functions.take_renumber import make_renumber
from ISUCT.Functions.make_coords import coord_writing
from ISUCT.Functions.make_orbs import orbs_writing
from ISUCT.Functions.make_charges import charges_writing
from ISUCT.Functions.make_wbi import wbi_writing
from ISUCT.Functions.make_nmr import nmr_writing
from ISUCT.Functions.Calculations.coord_calcultion import coord_calc
from ISUCT.Functions.Calculations.orbs_calculation import orbitals_calc
from ISUCT.Functions.Calculations.charges_calculation import charge_calc
from ISUCT.Functions.Calculations.wbi_calculations import wbi_calc
from ISUCT.Functions.Calculations.nmr_calculation import nmr_calc
from ISUCT.Functions.all_in_one_renumber import easy_renumber
from ISUCT.Functions.config_editing import edit_config_file
import pandas as pd

'''
Константы
'''
COORD_PHRASE = 'Standard orientation'
ORB_PHRASE = 'The electronic state'
CHARGE_PHRASE = 'Summary of Natural Population Analysis'
WBI_PHRASE = 'Wiberg bond index matrix in the NAO basis'
NMR_PHRASE = 'SCF GIAO Magnetic shielding tensor'
'''
Конец объявления констант
'''

'''
Инициализация переменных
'''
renumber_file = ''
dataframe_number = 0
df1 = pd.DataFrame({})

file_result = {
    'File': [],
    'Results': []
}

# Parsers
pos_coord = 0
pos_orbs = 0
pos_charges = 0
pos_WBI = 0
pos_NMR = 0

# Parameters
coord_parameters = 0
orb_parameters = 0
charge_parameters = 0
WBI_parameters = 0
NMR_parameters = 0

# Parameters_massives
distance_numbers = []

charge_numbers = []
WBI_Numbers = []
NMR_numbers = []

# Coords
CoordsX = []
CoordsY = []
CoordsZ = []

# Array of data from the received data
data = []

# Default_save_dir
def_save_dir = 'C:\\System32'

# save_dir undefiened exception
save_dir = def_save_dir

# printing variables exception
printing_coord = []
printing_orbs = []
printing_charges = []
printing_wbi = []
printing_nmr = []
renumber = []
'''
Конец инициализации переменных
'''

'''
Блок запросов к пользователю
'''
have_cfg = input('Do you have config file?')
if have_cfg not in ['y', 'Y']:
    request_result = user_requests()
    log_dir, do_coords, do_orbs, do_charges, do_wbi, do_nmr, do_renumber, do_save = request_result

    if do_save in ['y', 'Y']:
        while True:
            requested_dir = input('Specify the directory to save the analysis result: ')
            if '\\' not in requested_dir:
                print("It doesn't look like a directory")
            else:
                break
        save_dir = requested_dir + '\\' + 'result.csv'
        print('The directory to save has been successfully entered into the program!')
    files_numbers, files = select_file(log_dir)

    if do_renumber in ['y', 'Y']:
        print('Please specify the file with the atom renumbering')
        print('Sample: C:\\Users\\User\\directory\\file.txt')
        while True:
            renumber_file = input()
            if '.txt' not in renumber_file:
                print("It doesn't look like a .txt file."
                      "Try again and don't forget about the sample"
                      "Sample: C:\\Users\\User\\directory\\file.txt")
            else:
                break
        if check_renumber(renumber_file, files_numbers) is False:
            print('The number of selected .log files does not correspond to the number of '
                  'columns in the atom renumbering file')
        else:
            print('The atom renumbering file has successfully passed the compliance check!')
            print('The file renumbering of atoms has been successfully entered into the program!')
else:
    edit_config_file('config.txt')
    exit()
'''
Конец блока запросов к пользователю
'''

'''
Основной блок программы
'''

'''
Блок забора данных по анализу
'''
if do_renumber in ['y', 'Y']:
    renumber = make_renumber(renumber_file)

if do_coords in ['y', 'Y']:
    data, printing_coord = coord_writing(data)

if do_orbs in ['y', 'Y']:
    data, printing_orbs = orbs_writing(data)

if do_charges in ['y', 'Y']:
    data, printing_charges = charges_writing(data)

if do_wbi in ['y', 'Y']:
    data, printing_wbi = wbi_writing(data)

if do_nmr in ['y', 'Y']:
    data, printing_nmr = nmr_writing(data)
'''
Конец блока забора данных по анализу
'''

'''
Блок вычислений
'''
df1.insert(dataframe_number, 'Parameters', data, True)  # Creating a dataframe

total_parameters = len(df1)
row_number = 0

j = 0  # Counter
for j in range(len(files_numbers)):
    '''
    Filling a file_result dictionary with file names
    '''
    str_file_dir = str(files[j])
    file_name_start_index = str_file_dir.rfind('\\')
    file_name = str_file_dir[file_name_start_index + 1:]
    file_result['File'].append(file_name)

for j in range(len(files_numbers)):
    distance_numbers = []
    natoms = 0
    dataframe_number += 1
    row_number = -1
    data = ['' for k in range(total_parameters)]
    testfile = open(files[j], 'r')  # Openning file in files list for reading data from it
    for i in testfile.readlines():
        if 'NAtoms=' in i:  # A phrase for identifying the number of atoms
            natoms = int(i[11:14])
            if len(str(natoms)) < 2:  # If len number of atoms < 2 then increase the slice
                natoms = int(i[11:15])
        if natoms != 0:  # If we find number of atoms, and he not 0 we break the cicle
            break
    if natoms == 0:  # If we didn't find number of atoms, and he is 0 we request number of atoms from user
        tmps = input('The number of atoms in the file could not be detected in this file. Enter the number of atoms: ')
        natoms = int(tmps)
        # ДОПИЛИТЬ ЗАПИСЬ В КОНФИГ
    testfile.seek(0, os.SEEK_SET)
    testfile.close()

    # Coord section
    if do_coords in ['y', 'Y']:
        row_number += 1  # Increase number of row at 1

        if do_renumber in ['y', 'Y']:
            distance_numbers = easy_renumber(j, printing_coord, printing_orbs, printing_charges, printing_wbi,
                                             printing_nmr, renumber, distance_numbers, charge_numbers, WBI_Numbers,
                                             NMR_numbers, do_coords, do_orbs, do_charges, do_wbi, do_nmr)
        else:
            for i in range(len(printing_coord)):
                distance_numbers.append(printing_coord[i])  # Else we just transmit printed values
        data, file_result, row_number = coord_calc(data, COORD_PHRASE, files[j], natoms, distance_numbers, do_save,
                                                   row_number)  # Requesting calculation function
    # Orbitals section
    orbital_numbers = []
    if do_orbs in ['y', 'Y']:
        row_number += 1

        if do_renumber in ['y', 'Y']:
            orbital_numbers = easy_renumber(j, printing_coord, printing_orbs, printing_charges, printing_wbi,
                                            printing_nmr, renumber, distance_numbers, charge_numbers, WBI_Numbers,
                                            NMR_numbers, do_coords, do_orbs, do_charges, do_wbi, do_nmr)
        else:
            for k in range(len(printing_orbs)):
                orbital_numbers.append(*printing_orbs[k])

        # Requesting calculation function
        data, file_result, row_number = orbitals_calc(file_result, data, ORB_PHRASE, files[j], orbital_numbers)

    # Charges section
    if do_charges in ['y', 'Y']:
        row_number += 1

        if do_renumber in ['y', 'Y']:
            charge_numbers = easy_renumber(j, printing_coord, printing_orbs, printing_charges, printing_wbi,
                                           printing_nmr, renumber, distance_numbers, charge_numbers, WBI_Numbers,
                                           NMR_numbers, do_coords, do_orbs, do_charges, do_wbi, do_nmr)
        else:
            for k in range(len(printing_charges)):
                charge_numbers.append(printing_charges[k])
        data, file_result, row_number = charge_calc(file_result, data, CHARGE_PHRASE, files[j], charge_numbers)

    # WBI section
    if do_wbi in ['y', 'Y']:
        row_number += 1

        if do_renumber in ['y', 'Y']:
            WBI_Numbers = easy_renumber(j, printing_coord, printing_orbs, printing_charges, printing_wbi,
                                        printing_nmr, renumber, distance_numbers, charge_numbers, WBI_Numbers,
                                        NMR_numbers, do_coords, do_orbs, do_charges, do_wbi, do_nmr)
        else:
            for k in range(len(printing_wbi)):
                WBI_Numbers.append(printing_wbi[k])

        data, file_result, row_number = wbi_calc(file_result, data, WBI_PHRASE, files[j], WBI_Numbers, natoms)

    # NMR section
    if do_nmr in ['y', 'Y']:
        row_number += 1

        if do_renumber in ['y', 'Y']:
            NMR_numbers = easy_renumber(j, printing_coord, printing_orbs, printing_charges, printing_wbi,
                                        printing_nmr, renumber, distance_numbers, charge_numbers, WBI_Numbers,
                                        NMR_numbers, do_coords, do_orbs, do_charges, do_wbi, do_nmr)
        else:
            for k in range(len(printing_nmr)):
                NMR_numbers.append(printing_nmr[k])

        data, file_result, row_number = nmr_calc(file_result, data, NMR_PHRASE, files[j], NMR_numbers)

    # Conservation section
    if do_save not in ['y', 'Y']:
        if file_result['Results']:
            print(file_result)

    # Creating a file name from an absolute path
    str_file_full_directory = str(files[j])
    represent_name = str_file_full_directory[str_file_full_directory.rfind('\\') + 1:len(str_file_full_directory) - 4]
    df1.insert(dataframe_number, represent_name, data, True)  # Appending a DataFrame with received data

# Checking the output of an empty result
if do_save not in ['y', 'Y'] and (not file_result["Results"]):
    print('The results are empty')
'''
Конец блока вычислений
'''
if do_save in ['y', 'Y']:
    df1.to_csv(f'{save_dir}', sep=';', mode='w', index=False)  # Saving result as Result.csv in saving directory
'''
Конец основого блока программы
'''
