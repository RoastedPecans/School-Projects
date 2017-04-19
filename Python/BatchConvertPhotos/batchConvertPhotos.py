# Converts batches of photos into desired format
# Written: 5/27/2015
# NOTE: USES PYTHON 2.7

from Tkinter import *
from tkFileDialog import *
import PIL
from PIL import Image
import Tkinter

master = Tkinter.Tk()

def Convert():

    images = askopenfilenames(parent = master, title="Choose files to convert")
    master.focus_set()
    images = master.tk.splitlist(images)

    
    Format = raw_input("What format? (PNG, JPG, BMP, Tiff, Etc) ")
    Format = Format.lower()
    Format = Format.strip()
    while str(Format) != 'bmp' or 'eps' or 'gif' or 'im' or 'jpeg' or 'jpg' or 'jpeg 2000' or 'msp' or 'pcx' or 'png' or 'ppm' or 'spider' or 'tiff' or 'webp' or 'xbm' or 'xv thumbnails':
        Format = raw_input("Invalid Format. Please try again. ")
        if str(Format) == 'bmp' or 'eps' or 'gif' or 'im' or 'jpeg' or 'jpg' or 'jpeg 2000' or 'msp' or 'pcx' or 'png' or 'ppm' or 'spider' or 'tiff' or 'webp' or 'xbm' or 'xv thumbnails':
            break
            
    

    length = len(images)

    i = 0
    
    while i < int(length):
        name = images[i]
        print str(name)
        img1 = Image.open(str(name))
        nameLength = len(name)
        nameLength = nameLength - int(len(Format))
        name = name[0:int(nameLength)]
        img1.save(str(name) + '.' + str(Format), str(Format))
        i = i + 1
    print "Done!"

Convert()

loop = raw_input("Would you like to convert more (y/n)? ")
loop = loop.lower()
if loop[0] == 'y':
    Convert()
    master.focus_set()
else:
    master.destroy()
    print "Thanks!"
    
