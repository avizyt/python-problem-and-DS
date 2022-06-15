import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file_list = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        file_list.append(path)
print(file_list)

# with generator expression
def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in get_files(dir_path):
    print(file)