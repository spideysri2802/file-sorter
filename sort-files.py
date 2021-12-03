import os

current_dir = os.getcwd()

file_extensions = []

# print file extensions in current directory
for file in os.listdir(current_dir):
    file_extensions.append(os.path.splitext(file)[1])

file_extensions = set(file_extensions)

# make folder for each extension in file_extensions
for extension in file_extensions:
    os.mkdir(extension[1:])

# move files to their respective folders except for .py files.. 
# this is to ensure this script does not move from the current directory

for file in os.listdir(current_dir):
    if os.path.splitext(file)[1] == '.py':
        continue
    else:
        os.rename(file, os.path.join(os.path.splitext(file)[1][1:], file))