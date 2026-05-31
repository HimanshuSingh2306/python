import os

path = "'/New folder"

contents = os.listdir(path)

for item in contents:
    print(item)