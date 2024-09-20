import os

print("Welcome to FileNumerator")
targetdir = input("Insert path of target files: ")

os.chdir(targetdir)
filecount = os.listdir()

print("Count of files is:", len(filecount))
confirm1 = input("Would you like to rename all files in a numeric order? (Y/N): ")
confirm1 = confirm1.upper() 
if confirm1 == "Y":
    for index, filename in enumerate(filecount):
        old_filepath = os.path.join(targetdir, filename) 
        new_filename = f"{index + 1}.jpg" 
        new_filepath = os.path.join(targetdir, new_filename)  
        os.rename(old_filepath, new_filepath)  
        print("Done!")
if confirm1 == "N":
    exit()
