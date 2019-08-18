from glob import glob
from os import path

target_dir_path = './test_files'
recursive_search = True
target_file_type = '*.txt' # also works with just a wildcard (*) for all types
target_files = ""
delimeter = "_"
rename_target = "z"

if recursive_search:
    target_files = f'{target_dir_path}/**/{target_file_type}'
else:
    target_files = f'{target_dir_path}/{target_file_type}'

# for filename in glob(path.join(target_dir_path, target_file_type)):
for filename in glob(target_files, recursive=recursive_search):
    print(f'file open: {filename}')
