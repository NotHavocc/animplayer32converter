import os

print("Welcome to FileNumerator")
targetdir = input("Insert path of target files: ")

os.chdir(targetdir)
filecount = os.listdir()

print("Count of files is:", len(filecount))
confirm1 = input("Would you like to rename all files in a numeric order? (Y/N): ")
confirm1 = confirm1.upper()  # Corrected to assign the result back to confirm1
if confirm1 == "Y":
    for index, filename in enumerate(filecount):
        old_filepath = os.path.join(targetdir, filename)  # Get the full path of the old file
        new_filename = f"{index + 1}.jpg"  # Generating new filename with numeric order
        new_filepath = os.path.join(targetdir, new_filename)  # Get the full path of the new file
        os.rename(old_filepath, new_filepath)  # Renaming the file while keeping the path
        print("Done!")
if confirm1 == "N":
    exit()
