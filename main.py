import os
import sys
import builtins
from termcolor import colored

# 1. Clean ctypes fix to bypass deprecated os.system()
if sys.platform == "win32":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7 | 4)

# 2. Force termcolor to active mode inside the binary
os.environ["FORCE_COLOR"] = "1"

# 3. Wrapper to prevent notation glitches in the input() buffer
def colored_input(prompt_text=""):
    builtins.print(prompt_text, end="")
    return builtins.input()
input = colored_input

from pathlib import Path
from PIL import Image

def scale_setter(prompt):

    while True:
        try:
            scale = int(input(colored(prompt,"blue")))
            return scale
        except ValueError:
            print(colored("INVALID INPUT. INTEGER ANSWERS ONLY.", 'red'))
            continue


def y_or_n(prompt):

    answers = {'Y': True, 'N': False}
    while True:
        ans = input(colored(prompt,"blue")).upper()
        if ans in [*answers]:
            return answers[ans]
        else:
            print(colored("INVALID INPUT. (Y/N) ANSWERS ONLY.",'red'))
            continue


def main(file_path, bulk, gosub_folder=True, scale='50'):

    print(colored("Going Through: ","yellow"))
    print(colored(file_path, "yellow"))
    patterns = ("*.jpg", "*.png", "*.gif","*.jpeg")
    destination = Path(file_path.parent / "RESIZED_PHOTOS" )
    destination.mkdir(parents=True,exist_ok=True)
    if gosub_folder:
        img_files = Path.rglob(file_path,'*')
    else:
        img_files = Path.glob(file_path,'*')
    for img in img_files:
        if any(img.match(pat) for pat in patterns):
            pic_name = img.name
            print(colored(img ,'green'))
            if bulk == False:
                scale = scale_setter("Resize image by (%): ")
                pic = Image.open(img)
                x = int(round(pic.size[0]*0.01*scale))
                y = int(round(pic.size[1]*0.01*scale))
                new_pic = pic.resize((x,y))
                image_at = Path(destination / pic_name)
                new_pic.save(image_at)
                os.startfile(image_at)
            else:
                pic = Image.open(img)
                x = int(round(pic.size[0]*0.01*scale))
                y = int(round(pic.size[1]*0.01*scale))
                new_pic = pic.resize((x,y))
                image_at = Path(destination / pic_name)
                new_pic.save(image_at)
                os.startfile(destination)
    print(colored("\n\nYou can find the resized images at: " + str(destination),'yellow'))
    

if __name__ == "__main__":
    file_path = Path.cwd()
    scale='50'

    gosub_folder  = y_or_n("Resize the files in the sub folders?(Y/N): ")

    bulk = y_or_n("Resize all files as a group?(Y/N): ")
    if bulk:
     scale = scale_setter("Resize all images by (%): ")
     pass
    else:
     pass

    main (file_path=file_path,bulk=bulk,scale=scale,gosub_folder=gosub_folder)

    print(colored('''\n\n
MIT License

Copyright (c) 2026 Sanjay S
''','cyan'))
    input("\n\nPress Enter to close....")