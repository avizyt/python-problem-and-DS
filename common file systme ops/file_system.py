from pathlib import Path

home = Path.home()
current_directory = Path.cwd()


# iter current directory
for file in current_directory.iterdir():
    print(file)
