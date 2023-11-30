def easy_renumber(j, printing_coords, printing_orbs, printing_charges, printing_wbi, printing_nmr, renumber, distance_numbers, charge_numbers, WBI_Numbers, NMR_numbers, do_coords, do_orbs, do_charges, do_wbi, do_nmr):
    if do_coords in ['y', 'Y']:
        for i in range(len(printing_coords)):
            tmpp = printing_coords[i]  # Temporary variable of printing coord parameter
            tmpf = []  # Temporary variable of renumbered parameter

            for m in range(len(tmpp)):
                number = 0  # Temporary variable of renumbered parameter
                f = 0  # Counter

                for g in range(len(printing_coords[i])):
                    number = 0
                    f = 0

                    for h in range(len(renumber[0])):
                        if renumber[0][h] == tmpp[m]:  # If our printed paramter respond of renumber the break
                            break
                        else:
                            f += 1  # else we icrease counter at 1
                    number = renumber[j][f]
                    tmpf.append(number)
                distance_numbers.append(tmpf)  # Making renumbered massive with data to calculation
        return distance_numbers
    elif do_orbs in ['y', 'Y']:
        orbital_numbers = []
        for i in range(len(printing_orbs)):
            tmpp = int(*printing_orbs[i])  # Temporary variable of printing orbitals parameter
            tmpf = 0
            f = 0

            for m in range(len(renumber[0])):
                if renumber[0][m] == tmpp:
                    break
                else:
                    f += 1
            tmpf = renumber[j][f]
            orbital_numbers.append(tmpf)
        return orbital_numbers
    elif do_charges in ['y', 'Y']:
        for i in range(len(printing_charges)):
            tmpp = int(printing_charges[i])  # Temporary variable of printing charges parameter
            tmpf = 0
            f = 0

            for m in range(len(renumber[0])):
                if renumber[0][m] == tmpp:
                    break
                else:
                     f += 1
            tmpf = renumber[j][f]
            charge_numbers.append(tmpf)
        return charge_numbers
    elif do_wbi in ['y', 'Y']:
        for i in range(len(printing_wbi)):
            tmpp = printing_wbi[i]  # Temporary variable of printing wbi parameter
            tmpf = []

            for m in range(len(tmpp)):
                number = 0
                f = 0

                for g in range(len(printing_wbi[i])):
                    number = 0
                    f = 0

                    for h in range(len(renumber[0])):
                        if renumber[0][h] == tmpp[m]:
                            break
                        else:
                            f += 1
                    number = renumber[j][f - 1]
                    tmpf.append(number)
                WBI_Numbers.append(tmpf)
        return WBI_Numbers
    elif do_nmr in ['y', 'Y']:
        for i in range(len(printing_nmr)):
            tmpp = int(printing_nmr[i])  # Temporary variable of printing nmr parameter
            tmpf = 0
            f = 0

            for m in range(len(renumber)):
                if renumber[0][m] == tmpp:
                    break
                else:
                    f += 1
            tmpf = renumber[j][f]
            NMR_numbers.append(tmpf)
        return NMR_numbers