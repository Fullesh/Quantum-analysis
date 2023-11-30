import math
import os


def coord_calc(data, coord_phrase, file_directory, natoms, distance_numbers, do_save, row_number):
    result = ''
    str_file_dir = str(file_directory)
    file_name_start_index = str_file_dir.rfind('\\')
    file_name = str_file_dir[file_name_start_index + 1:]
    file_result = {
        'File': None,
        'Results': []
    }
    j = 0
    coordsx = []
    coordsy = []
    coordsz = []
    pos_coord = 0
    file = open(file_directory, 'r')
    for i in file.readlines():
        j += 1
        if coord_phrase in i:
            pos_coord = j + 4
    file.seek(0, os.SEEK_SET)
    file.close()

    file = open(file_directory, 'r')
    if pos_coord == 0:
        print(f'The coordinates in the file {file_directory} were not found!')
    else:
        for j in range(pos_coord):
            i = file.readline()
        i = ''
        for j in range(natoms - 1):
            i = file.readline()
            coordsx.append(float(i[36:47]))
            coordsy.append(float(i[47:59]))
            coordsz.append(float(i[59:71]))
        for j in range(len(distance_numbers)):
            if len(distance_numbers[j]) == 2:  # distance calculation
                result = math.sqrt(
                    math.pow((coordsx[distance_numbers[j][0] - 1]) -
                             (coordsx[distance_numbers[j][1] - 1]), 2) +
                    math.pow((coordsy[distance_numbers[j][0] - 1]) -
                             (coordsy[distance_numbers[j][1] - 1]), 2) +
                    math.pow((coordsz[distance_numbers[j][0] - 1]) -
                             (coordsy[distance_numbers[j][1] - 1]), 2))
                result = round(result, 5)
                if do_save not in ['y', 'Y']:
                    file_result['File'] = file_name
                    file_result['Results'].append(f"{result:10.5f} angstorms")
            if len(distance_numbers[j]) == 3:  # angle calculation
                coordx_vektora_1 = coordsx[distance_numbers[j][0] - 1] - coordsx[distance_numbers[j][1] - 1]
                coordy_vektora_1 = coordsy[distance_numbers[j][0] - 1] - coordsy[distance_numbers[j][1] - 1]
                coordz_vektora_1 = coordsz[distance_numbers[j][0] - 1] - coordsz[distance_numbers[j][1] - 1]

                coordx_vektora_2 = coordsx[distance_numbers[j][1] - 1] - coordsx[distance_numbers[j][2] - 1]
                coordy_vektora_2 = coordsy[distance_numbers[j][1] - 1] - coordsy[distance_numbers[j][2] - 1]
                coordz_vektora_2 = coordsz[distance_numbers[j][1] - 1] - coordsz[distance_numbers[j][2] - 1]

                coordx_vektora_3 = coordsx[distance_numbers[j][0] - 1] - coordsx[distance_numbers[j][2] - 1]
                coordy_vektora_3 = coordsy[distance_numbers[j][0] - 1] - coordsy[distance_numbers[j][2] - 1]
                coordz_vektora_3 = coordsz[distance_numbers[j][0] - 1] - coordsz[distance_numbers[j][2] - 1]

                dlina_vektora_1 = math.sqrt((math.pow(coordx_vektora_1, 2)) +
                                            (math.pow(coordy_vektora_1, 2)) +
                                            (math.pow(coordz_vektora_1, 2)))
                dlina_vektora_2 = math.sqrt((math.pow(coordx_vektora_2, 2)) +
                                            (math.pow(coordy_vektora_2, 2)) +
                                            (math.pow(coordz_vektora_2, 2)))
                dlina_vektora_3 = math.sqrt((math.pow(coordx_vektora_3, 2)) +
                                            (math.pow(coordy_vektora_3, 2)) +
                                            (math.pow(coordz_vektora_3, 2)))

                angle = ((math.pow(dlina_vektora_1, 2)) + (math.pow(dlina_vektora_2, 2)) - (
                    math.pow(dlina_vektora_3, 2))) / (2 * dlina_vektora_1 * dlina_vektora_2)

                result = math.degrees(math.acos(angle))
                result = round(result, 3)
                if do_save not in ['y', 'Y']:
                    file_result['File'] = file_name
                    file_result['Results'].append(f"{result:10.5f} degrees")
            if len(distance_numbers[j]) == 4:  # Dihedral angle
                # Calculation of planes
                a0 = coordsx[distance_numbers[j][1] - 1] - coordsx[distance_numbers[j][0] - 1]
                a1 = coordsx[distance_numbers[j][2] - 1] - coordsx[distance_numbers[j][0] - 1]
                b0 = coordsy[distance_numbers[j][1] - 1] - coordsy[distance_numbers[j][0] - 1]
                b1 = coordsy[distance_numbers[j][2] - 1] - coordsy[distance_numbers[j][0] - 1]
                c0 = coordsz[distance_numbers[j][1] - 1] - coordsz[distance_numbers[j][0] - 1]
                c1 = coordsz[distance_numbers[j][2] - 1] - coordsz[distance_numbers[j][0] - 1]
                a2 = coordsx[distance_numbers[j][2] - 1] - coordsx[distance_numbers[j][1] - 1]
                a3 = coordsx[distance_numbers[j][3] - 1] - coordsx[distance_numbers[j][1] - 1]
                b2 = coordsy[distance_numbers[j][2] - 1] - coordsy[distance_numbers[j][1] - 1]
                b3 = coordsy[distance_numbers[j][3] - 1] - coordsy[distance_numbers[j][1] - 1]
                c2 = coordsz[distance_numbers[j][2] - 1] - coordsz[distance_numbers[j][1] - 1]
                c3 = coordsz[distance_numbers[j][3] - 1] - coordsz[distance_numbers[j][1] - 1]

                a = b0 * c1 - b1 * c0
                b = a1 * c0 - a0 * c1
                c = a0 * b1 - b0 * a1
                a_1 = b2 * c3 - b3 * c2
                b_1 = a3 * c2 - a2 * c3
                c_1 = a2 * b3 - b2 * a3

                diff_sqrts = (math.sqrt((math.pow(a, 2)) + (math.pow(b, 2)) + (math.pow(c, 2)))) * (
                    math.sqrt((math.pow(a_1, 2)) + (math.pow(b_1, 2)) + (math.pow(c_1, 2))))
                diff_angle = ((a * a_1) + (b * b_1) + (c * c_1)) / diff_sqrts

                result = math.degrees(math.acos(diff_angle))
                result = round(result, 5)

                if do_save not in ['y', 'Y']:
                    if file_result['File'] != 'None':
                        file_result['File'] = file_name
                        file_result['Results'].append(f"{result:10.5f} degrees")

            row_number += 1
            data[row_number] = result
    file.close()
    row_number += 1
    return data, file_result, row_number
