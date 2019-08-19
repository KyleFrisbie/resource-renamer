from glob import glob
from os import path, rename

target_dir_path = './test_files'
recursive_search = True
target_file_type = '*.txt' # also works with just a wildcard (*) for all types
delimeter = "_"
rename_target = "z" # the section we're looking to rename
rename_text_update = "Z" # the new name for the rename target after we find it
target_files = "" # set after determining full path with recursive search

if recursive_search:
    target_files = f'{target_dir_path}/**/{target_file_type}'
else:
    target_files = f'{target_dir_path}/{target_file_type}'

exception_count = 0
# for filename in glob(path.join(target_dir_path, target_file_type)):
for filename in glob(target_files, recursive=recursive_search):
    basename = path.basename(filename).split(delimeter)
    try:
        for i, item in enumerate(basename):
            if rename_target in basename[i]:
                basename[i] = rename_text_update
                updated_name = delimeter.join(basename)
                updated_path = path.split(filename)
                updated_path = path.join(updated_path[0], updated_name)
                rename(filename, updated_path)
    except Exception as e:
        exception_count += 1
        print(f'Exception: {e} \t error processing {basename}, count: {exception_count}')
