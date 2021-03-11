# Python-Image-To-ASCII-Converter
A python program to turn your image into ASCII art.

You give it a path to your image, then you enter a size for your ascii art (ascii art will be a square).
Then the program will generate your ascii art into a file out.txt.
You will also receive a copy of your image resized and in greyscale for comparison.

The  program takes an a psecified image, resizes it and turns it to greyscale. It then goes through each pixel and prints an ascii character depending on how dark the pixel is.

Here are the characters used ordered dark to light.

              DARK  < ---------------                         --------------- >   LIGHT
characters = ['#', '@', 'F', '&', '£', '$', '?', 'I', 'i', '=', ';', 'o', '-', ',', '.']
