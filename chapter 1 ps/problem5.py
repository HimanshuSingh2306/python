# Import the os module to interact with the operating system
import os

# Specify the directory path
# "." means the current working directory
directory_path = "."

# Get the list of all files and folders in the directory
contents = os.listdir(directory_path)

# Print a heading
print("Contents of the directory are:")

# Loop through each item in the directory and print it
for item in contents:
    print(item)