printing_nmr = []


def nmr_writing(data):
    nmr_parameters = input('Specify the number of NMR parameters to be analyzed: ')
    data.append('NMR:')

    print('Specify the atoms to be specified in the NMR output')

    for j in range(int(nmr_parameters)):
        tmps = input(f'Atom {j+1}: ')
        printing_nmr.append(int(tmps))
        data.append(tmps)
    return data, printing_nmr
