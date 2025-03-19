import sys
import os
from PIL import Image, ImageOps

def main():
    file_check()
    ext_check()
    before = open_image(sys.argv[1])
    shirt = open_image("shirt.png")
    resized = resize(before,shirt)
    overlay(resized,shirt)

def resize(photo, shirt):
    size = shirt.size
    return ImageOps.fit(photo, size)

def overlay(photo, shirt):
    photo_copy = photo.copy()
    shirt_copy = shirt.copy()
    photo_copy.paste(shirt_copy,shirt_copy)
    photo_copy.save(sys.argv[2])


def open_image(image_in):
    try:
        return Image.open(image_in)
    except FileNotFoundError:
        sys.exit("Input does not exist")

def ext_check():
    in_ext = os.path.splitext(sys.argv[1])
    out_ext = os.path.splitext(sys.argv[2])
    if in_ext[1] != out_ext[1]:
        sys.exit("Input and output have different extensions")

def file_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[2].lower().endswith((".png",".jpeg",".jpg")):
        sys.exit("Invalid output")

if __name__ == "__main__":
    main()