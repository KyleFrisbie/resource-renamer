from math import log10, ceil, floor
from os import path, makedirs
from string import ascii_lowercase

test_dir_path = "./test_files"
number_of_files = 399

# create test dir if it doesn't exist
if not path.exists(test_dir_path):
    makedirs(test_dir_path)

# determine number of decimal places in total files to create
decimal_places = ceil(log10(number_of_files))

# iterate over the range of files and create them
for i in range(0, number_of_files):
    # pad file number with leading zeros based on number of decimal places
    file_number = '{:0{decimal_places}d}'.format(i, decimal_places=decimal_places)

    # create sections with letters
    #   get the quotient and the remainder and store it in carry_over
    carry_over = divmod(floor(i/10), 26)

    # create the letter section by repeating the position of the remainder by the quotient
    file_letter_section = (carry_over[0] + 1) * ascii_lowercase[carry_over[1]]

    with open(f'./test_files/test_file_{file_letter_section}_{file_number}.txt', 'w') as open_file:
        # do nothing, just create the file for testing
        print(f'{file_number} written')
