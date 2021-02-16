#!/usr/bin/env python3

from PIL import Image, UnidentifiedImageError
import os

text_file = open('text.txt', 'w')
list_files = os.listdir(path=".")


for image in list_files:
    try:
        img = Image.open(image)
        text_file.write(str(img.size)+ " .... "  + image + '\n')
    except UnidentifiedImageError:
        pass
    except IsADirectoryError:
        pass
    

text_file.close()
