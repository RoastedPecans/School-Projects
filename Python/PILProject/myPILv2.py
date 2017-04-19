# Creates "Checkerboard" pattern on a new image from two images So every other pixel will be from the other image.
# This creates a unique image where you can see both of the previous images on the same image
# Written March 2015
import PIL
import ctypes
from PIL import Image
import PIL.ImageOps
#Set height and width to size of images 
userInputWidth = input("Enter the desired width for your new image: ")
userInputHeight = input("Enter the desired height for your new image: ")

height = userInputHeight
width = userInputWidth

a = 1
b = 1
iteration = 0
value = (0, 0, 0 , 1)
#Setup images and make them RGBA and the same size
img1 = Image.open("IMAGE1.jpg")
img1 = img1.convert("RGBA")
img1 = img1.resize((int(userInputWidth), int(userInputHeight)), Image.ANTIALIAS)

img2 = Image.open("IMAGE2.jpg")
img2 = img2.convert("RGBA")
img2 = img2.resize((int(width), int(height)), Image.ANTIALIAS
)

pix = img1.load()
#print img1.size

#Set height and width to size of images (Failsafe...)
[height, width] = img1.size

#Prints the Height and the Width of the Image
#print "Height = " + str(height) + " Width = " + str(width)

#Cycles through all pixels in the image
while a < height and b < width:
    #print a

    #Sets checkerboard to pixels from second image
    if a % 2 == 0 or a == 0 or a == userInputHeight:
        rgb = img2.getpixel((a, b))
        img1.putpixel((a, b), rgb)
        a = a + 2
    if a % 2 != 0:
        rgb = img2.getpixel((a, b))
        img1.putpixel((a, b), rgb)
        a = a + 2
    if a == width or width - a == 1: #If a is equal to the width of the picture, go to the next row
        rgb = img2.getpixel((a, b))
        img1.putpixel((a, b), rgb)
        iteration = iteration + 1
        #print 'ITERATION = ' + str(iteration)
        a = a - int(userInputWidth) + 1
        b = b + 1
        
            
img1.show()

