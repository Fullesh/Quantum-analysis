from pathlib import Path
import os

file_directory = []


def select_file(log_dir):
    log_files_found = False
    counter = 0
    os.chdir(log_dir)
    while True:
        for file in Path('.').glob('*'):
            counter += 1
            file_str = str(file)
            if file_str[file_str.rfind('.'):] != '.log':
                if log_files_found is True:
                    pass
                else:
                    print(".log files did'nt found")
            else:
                print(f'{counter} - {file}')
                log_files_found = True
        counter = 0
        files = input('Enter the numbers of the selected files separated by commas: ')
        selected_files = files.split(',')
        for file in Path('.').glob('*'):
            counter += 1
            if str(counter) in selected_files:
                file_directory.append(file.absolute())
        if log_files_found is True:
            break
    return selected_files, file_directory
