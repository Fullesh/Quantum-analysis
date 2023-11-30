printing_charges = []


def charges_writing(data):
    data.append('Charges:')
    charge_parameters = input('Specify the number of analyzed atomic charges: ')
    print('Specify the number of atoms that will be indicated in the output')

    # ÇÀÍÅÑÒÈ ÈÇÌÅÍÅÍÈß Â ÊÎÍÔÈÃ
    for j in range(int(charge_parameters)):
        tmps = input(f'Atom {j+1}: ')
        printing_charges.append(int(tmps))
        data.append(tmps)
    return data, printing_charges
