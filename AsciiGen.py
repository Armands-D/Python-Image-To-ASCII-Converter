from PIL import Image, ImageOps

image_file = input("Enter Your Image Name / Path: ")
try:
    image = Image.open(image_file)
except:
    print("Incorrect file / path given")
    quit()

try:
    dimension = input("Enter a size, it will be both your width and height. No larger than 375.\nEnter ! to exit: ")
    if dimension == "!":
        quit()
    else:
        dimension = int(dimension)
except:
    dimension = -1

while dimension > 375 or dimension < 1:
    try:
        dimension = input("Invalid input given.\nEnter ! to exit: ")
        if dimension == "!":
            quit()
        else:
            dimension = int(dimension)
    except:
        print("Invalid input given.\nEnter ! to exit: ")

size = (dimension, dimension)
image.thumbnail(size)
print("Converting image to grayscale")
image = ImageOps.grayscale(image)

characters = ['#', '@', 'F', '&', '£', '$', '?', 'I', 'i', '=', ';', 'o', '-', ',', '.']
pixel = image.load()
width, height = image.size
output = open("out.txt", "w")
string = ""
for x in range(width):
    for y in range(height):
        value = int(image.getpixel((x, y)) / 17)
        string += characters[::-1][value - 1]
    string += "\n"

output.write(string)
output.close()

print("Image has been saveds as resizedFILENAME")
image.save("resizedflower.jpg")
print("You Ascii art has been generated, check out.txt")
