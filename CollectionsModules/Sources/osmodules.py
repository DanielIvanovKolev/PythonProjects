# Look at from collections import namedtuples!!!!!
# It's like OOP , but strange!

'''
f = open('practice.txt', 'w+')
f.write('This is a test file')
f.close()

with open('practice_v2.txt', mode='a', newline='') as file:
    # The newline It tells Python to preserve the line endings exactly as they are in the file
    file.write("This is the second file test")
'''


import os

print(os.getcwd())
print(os.listdir())
print(os.listdir('D:\\Pictures'))

import shutil

shutil.move('practice.txt', '/CollectionsModules/Files')  # Takes a source and move it to a destination
#shutil.move('Files/practice.txt', 'D:\\Programming\\Projects\\PythonProjects\\CollectionsModules')  # Takes a source and move it to a destination

'''
os.unlink(path) - Deletes a file at the path provided
os.rmdir(path) - Deletes a directory (folder must be empty) at a path provided
shutil.rmtree(path) - It will remove all the files and folders contained in the path - Something like rm -f 
'''

import send2trash

send2trash.send2trash("../Files/practice.txt")

# There is os.walk if you want to check
