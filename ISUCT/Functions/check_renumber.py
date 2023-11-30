def check_renumber(renumber_file, file_numbers):
    with open(renumber_file, 'r') as renumber_file_check:
        num_of_columns = len(renumber_file_check.readline().split())
        if num_of_columns != len(file_numbers):
            return False
        else:
            return True
