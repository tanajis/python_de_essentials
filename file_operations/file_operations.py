import datetime

# Safe read with open. No need to close manually.
# Avoid open() without with in production pipelines
with open("file1.txt", 'r') as f:

    print("---------------------------------")
    # All content as string.
    print("1.All content as string.\n")
    content = f.read()
    print(content)
    print("---------------------------------")


# We need to open it separately.
with open("file1.txt", "r") as f:
    print("2.Line by Line.\n")
    for line in f:
        print(line.strip)


####################################

# Writing a file
# W mode: Overwrite file with every run. 
with open("file2.txt", 'w') as f:
    f.write('This line will be overwritten by following')

#-----------------------------------------
# Append a file
# a mode: Overwrite file with every run. 
# a+ means create first time if does not exist. Use this to avoid error in the first run
with open("file3.txt", 'a+') as f:
    f.write("\n" + str(datetime.datetime.now()))


################################################

# check if file exists

import os 
if not os.path.exists("file4.txt"):
    print("Error: file4.txt does not exists!")

# Path

################################################
# Pathlib
################################################
from pathlib import Path

# Get path of current file
CURR_DIR = Path(__file__)
print(f"Current DIR {CURR_DIR}")
print("Current DIR %s" %CURR_DIR)

# Get project root dir 
REPOSITORY_ROOT = CURR_DIR.parent.parent
print(f"Repository Root :{REPOSITORY_ROOT}") 

################################################
# shutil and Os: file copy rename dir creation
################################################

import os
import shutil

#os.mkdir('new_dir')  # Create dir
# shutil.rmtree('dir')  # Delete dir tree

fd = os.open("file5.txt", os.O_CREAT)
os.close(fd)
#os.remove("file5.txt")
# os.rename('old.txt', 'new.txt')  # Rename/move same F
# shutil.copy("file5", "file6")
# shutil.copy('src.txt', 'dst.txt')  # Copy
# shutil.move('src.txt', '/new/dir/')  # Move (cross-FS)


#######################################
# Error Handling
#######################################


try:
    with open('file10.txt', 'r') as f:
        f.read()
except FileNotFoundError:
    print("File does not exists!")
except PermissionError:
    print("No permission to read file!")
except UnicodeDecodeError:
    # Use encoding='utf-8', errors='replace'
    with open('file.txt', 'r', encoding='utf-8', errors='replace') as f:
        f.read()

######################################################
# Reading/Writing CSV , JSON
#######################################################

with open('data1.csv','r') as f:
    # print(f.read())  This read a whole text. Good for logs
    for line in f.readlines():
        print(line)


# CSVs can be handled using csv package

print("Reading usin CSV DictReader")
import csv 

# REad as row disctinory
with open('data1.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# Write as dictionary - input is dict 

with open('data2.csv','w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Name','age'])
    writer.writeheader() # add header first

    writer.writerow({'Name': 'Alice', 'age': '45'})
    writer.writerow({'Name': 'Bob', 'age': '50'})

# Write as row - input is list
with open('data3.csv', 'w', newline='') as f:
    writer = csv.writer(f) # 
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])

###########################################
# Json

import json

# Read json
with open('dummy.json', 'r') as f:
    loaded = json.load(f)
    print(loaded)


# Write json
data = {'name': 'Bob', 'age': 25}
with open('dummy2.json', 'w') as f:
    json.dump(data, f)