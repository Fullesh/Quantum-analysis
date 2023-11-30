

def_coords = 'n'
def_orbs = 'n'
def_charges = 'n'
def_WBI = 'n'
def_NMR = 'n'
def_renumber = 'n'
def_save = 'n'


def user_requests():
    with open('config.txt') as cfg_file:
        while True:
            log_dir = input('Enter the directory with the .log files: ')
            if '\\' not in str(log_dir):
                print("It doesn't look like a directory. Try again")
            else:
                cfg_file.write(log_dir)
                break
        do_coords = input('Is it necessary to analyze geometric parameters?(y/n): ')
        if do_coords not in ['y', 'n', 'Y', 'N']:
            do_coords = def_coords
        cfg_file.write(do_coords)
        do_orbs = input('Is an analysis of orbital energies necessary?(y/n): ')
        if do_orbs not in ['y', 'n', 'Y', 'N']:
            do_orbs = def_orbs
        cfg_file.write(do_orbs)
        do_charge = input('Is it necessary to analyze natural charges?(y/n): ')
        if do_charge not in ['y', 'n', 'Y', 'N']:
            do_charge = def_charges
        cfg_file.write(do_charge)
        do_wbi = input('Is WBI analysis necessary?(y/n): ')
        if do_wbi not in ['y', 'n', 'Y', 'N']:
            do_wbi = def_WBI
        cfg_file.write(do_wbi)
        do_nmr = input('Is NMR analysis necessary?(y/n): ')
        if do_nmr not in ['y', 'n', 'Y', 'N']:
            do_nmr = def_NMR
        cfg_file.write(do_nmr)
        have_renumber = input('Do you have a file with atom renumbering?(y/n): ')
        if have_renumber not in ['y', 'n', 'Y', 'N']:
            have_renumber = def_renumber
        cfg_file.write(have_renumber)
        save_result = input('Is it necessary to save the analysis results?(y/n): ')
        if save_result not in ['y', 'n', 'Y', 'N']:
            save_result = def_save
        cfg_file.write(save_result)
    return [log_dir, do_coords, do_orbs, do_charge, do_wbi, do_nmr, have_renumber, save_result]
