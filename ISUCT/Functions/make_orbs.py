printing_orbs = []


def orbs_writing(data):
    orbs_parameters = int(input('Specify the number of orbs to be analyzed: '))

    #��������� ������ � ������
    print('Specify the numbers of orbitals that will be indicated in the output: ')
    data.append('Orbitals:')
    for j in range(orbs_parameters):
        tmps = input(f'Parameter {j + 1} ')
        printing_orbs.append(list(map(int, tmps.split('-'))))
        data.append(' ' + tmps)
        # ��������� ������ � ������
    return data, printing_orbs
