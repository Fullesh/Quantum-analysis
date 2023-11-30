
printing_coords = []


def coord_writing(data):
    coord_parameters = int(input('Specify the number of geometric parameters to be analyzed: '))

    # ÏĞÎÏÈÑÀÒÜ ÇÀÏÈÑÜ Â ÊÎÍÔÈÃ

    data.append('Geometry:')
    for j in range(coord_parameters):
        TMPS = input(f'Parameter {j + 1} ')
        printing_coords.append(list(map(int, TMPS.split('-'))))
        data.append(' ' + TMPS)
        # ÏĞÎÏÈÑÀÒÜ ÇÀÏÈÑÜ Â ÊÎÍÔÈÃ
    return data, printing_coords
