with open("practice.txt", 'w') as practice_txt_file:
    practice_txt_file.write("This is test string")
import os
print(os.getcwd())

print(os.listdir()) # it will list all the item the current location(directory)

print(os.listdir('C:\\Users\\vsaroha\\Documents\\complete python')) # it will list all dir in mentioned location

import shutil # to copy and move file from one location to another location
#shutil.move(src='..\\practice.txt',dst='C:\\Users\\vsaroha\\Documents\\complete python\\advance python\\') # to move file from one location to another location
#print(os.listdir("C:\\Users\\vsaroha\\Documents\\complete python\\"))
#shutil.rmtree will remove non empty directory and file

file_path = ('C:\\Users\\vsaroha\\Documents\\complete python')
print("this is output",os.listdir("C:\\Users\\vsaroha\\Documents\\complete python"))
for folder,sub_folder,files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print("\n")
    print("The subfolders are:")
    for sub_fold in sub_folder:
        print(f"subfolders: {sub_fold}")
    print('\n')
    print("The files are: ")
    for f in files:
        print(f"File: {f}")
    print('\n')