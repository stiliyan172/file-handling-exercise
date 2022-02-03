
from os import listdir, path


def traverse_dir(current_path, files_by_ext):
    for element in listdir(current_path):
        if path.isdir(path.join(current_path, element)):
            # check if this is dir
            traverse_dir(path.join(current_path, element), files_by_ext)
        else:
            # check if it is file
            extension = element.split(".")[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(element)


files_by_ext = {}
traverse_dir('.', files_by_ext)

with open('result.txt', 'w') as output:
    for ext, files in sorted(files_by_ext.items()):
        output.write(f".{ext}")
        for file in sorted(files):
            output.write(f'--- {file}')
