from posixpath import basename
from PIL import Image, ImageFile
import os

count = 0
clear_count = 0
my_path = os.path.abspath(os.curdir)


def isImage(file):
    return ".png" in file or ".jpg" in file or ".jpeg" in file


def isNotWebp(file):
    return ".png" in file or ".jpg" in file or ".jpeg" in file


def convert(basepath):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    image = Image.open(basepath)
    name = os.path.basename(basepath).split('.')[0] + ".webp"
    dir_name = os.path.dirname(basepath)
    image.save(dir_name + "/" + name, format="webp")


def recursion_folder(basepath):
    global count
    if os.path.isfile(basepath):
        if isImage(basepath):
            count = count + 1
            convert(os.path.abspath(basepath))
        return
    else:
        for files in os.listdir(basepath):
            recursion_folder(os.path.join(basepath, files))


def clear(basepath):
    global clear_count
    if os.path.isfile(basepath):
        if isNotWebp(basepath):
            clear_count = clear_count + 1
            os.remove(basepath)
        return
    else:
        for files in os.listdir(basepath):
            clear(os.path.join(basepath, files))


recursion_folder(os.path.join(os.path.realpath(my_path)))
clear(os.path.join(os.path.realpath(my_path)))

print(count)
print(clear_count)

