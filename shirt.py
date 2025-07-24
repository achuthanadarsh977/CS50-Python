import sys

from os.path import splitext
from PIL import Image , ImageOps


def main():

    check_command()
    try:
        image = Image.open(sys.argv[1])


    except FileNotFoundError:
        sys.exit("Input does not exist")


    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(image,size)
    photo.paste(shirt,shirt)
    photo.save(sys.argv[2])




def check_file(file):

    y = [".png",".jpeg",".jpg"]

    if file in y:
        return True
    return False





def check_command():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    f1 = splitext(sys.argv[1])
    f2 = splitext(sys.argv[2])

    if check_file(f1[1]) == False:
        sys.exit("Invalid input")

    if check_file(f2[1]) == False:
        sys.exit("Invalid output")

    if f1[1].lower() != f2[1].lower():
        sys.exit("Input and output have different extensions")



if __name__ == "__main__":
    main()
