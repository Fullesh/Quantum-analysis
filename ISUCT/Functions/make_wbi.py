printing_wbi = []


def wbi_writing(data):
    # ÂÍÅÑÒÈ ÈÇÌÅÍÅÍÈß Â ÊÎÍÔÈÃ
    wbi_parameters = input('Specify the number of analyzed WBI indexes: ')
    data.append('WBI:')
    print('Specify the pairs of atoms to be specified in the WBI output')
    print('Example: 1-2, 3-4')

    for j in range(int(wbi_parameters)):
        tmps = input(f'Atoms {j+1}: ')
        printing_wbi.append(list(map(int, tmps.split('-'))))
        data.append(tmps)
    return data, printing_wbi
