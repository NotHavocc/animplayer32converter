from PIL import Image
import os

gif_path = input("Type in path of the target GIF: ")
gif = Image.open(gif_path)

output_folder = input("Type in letter of SD card (or file if not using AnimPlayer32): ")
print("GIF output folder is", output_folder)
confirm = input("Confirm? (Y/N) ").upper()

if confirm == "Y":

    os.makedirs(output_folder, exist_ok=True)

    frame = 0
    while True:
        try:
            gif.seek(frame)
            new_filename = f"{frame + 1}.jpg"
            new_filepath = os.path.join(output_folder, new_filename)
            gif.convert('RGB').save(new_filepath, 'JPEG')
            
            print(f'Saved as {new_filepath}')
            frame += 1
        except EOFError:
            print("Done!")
            os.system('pause')
            break
else:
    exit()




