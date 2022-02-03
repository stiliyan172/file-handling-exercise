from os import walk

files_by_extension = {}
for root, dirs, files in walk('.'):
    for file in files:
        extension = file.split('.')[-1]
        if extension not in files_by_extension:
            files_by_extension[extension] = []
        files_by_extension[extension].append(file)


with open('result.txt', 'w') as output:
    for ext, files in sorted(files_by_extension.items()):
        output.write(f".{extension}")
        for file in sorted(files):
            output.write(f'--- {file}')

for extension, files in sorted(files_by_extension.items()):
    print(f'.{extension}')
    for file in sorted(files):
        print(f'---{file}')