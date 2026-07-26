import os
import re
from pathlib import Path
from PIL import Image


file_path = Path.cwd()
print(file_path)

for folders,subfolders,files in os.walk(file_path):
    for file in files:
        try:
            pic_name = re.match('^.+[.](jpg|jpeg|png|gif)$',file).group()
            picture = rf'{folders}\{pic_name}'
            print(picture)
            pic = Image.open(picture)
            x = int(round(pic.size[0]/2))
            y = int(round(pic.size[1]/2))
            resized = (x,y)
            new_pic = pic.resize(resized)
            new_pic.show()
        except AttributeError:
            pass