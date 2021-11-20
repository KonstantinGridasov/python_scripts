from PIL import Image, ImageFile
import os

count = 0


def isImage(file):
    return ".png" in file or ".jpg" in file or ".webp" in file


def resize_image_by_param(sizes, basepath):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    img = Image.open(basepath)
    w, h = img.size
    neww, newh = sizes, sizes
    left, top, right, bottom = 0, 0, w, h
    if (w > sizes and h > sizes):
        if (w != h):
            if(w > h):
                neww = w/h * sizes
            else:
                newh = h/w * sizes
            img = img.resize((int(neww), int(newh)), Image.ANTIALIAS)
            neww, newh = img.size
            right = neww/2 + sizes/2
            left = neww/2 - sizes/2

            bottom = newh/2 + sizes/2
            top = newh/2 - sizes/2

            img = img.crop((left, top, right, bottom))
        else:
            img = img.resize((int(neww), int(newh)), Image.ANTIALIAS)

        img.save(basepath)
    img.close()


def recursion_folder(sizes, basepath):
    global count
    if os.path.isfile(basepath):
        if isImage(basepath):
            count = count + 1
            resize_image_by_param(sizes, os.path.abspath(basepath))
        return
    else:
        for files in os.listdir(basepath):
            recursion_folder(sizes, os.path.join(basepath, files))


recursion_folder(512, os.path.curdir)
print(count)
