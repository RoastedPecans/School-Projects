# NOTE: USES PYTHON 2.7
# Adds text to image using a GUI.
# Used to help me learn to create custom GUI's.
# Written March 2015

import PIL
import PIL.Image
from PIL import ImageDraw
from PIL import ImageFont
import Tkinter,tkFileDialog
from tkFileDialog import askopenfilename
from Tkinter import *
width = 0
height = 0
textWidth = 0
textHeight = 0
def submit():
    top.quit()
    
top = Tk()
textWidget = Entry(top, width=100)
textWidget.grid(row = 1, column = 2)

FileName = Entry(top, width = 100)
FileName.grid(row = 2, column = 2)

label = Label(top, text="Insert Text:")
label.grid(row = 1, column = 1)

label2 = Label(top, text="Enter File Name:")
label2.grid(row = 2, column = 1)

submitButton = Button(top, text="Submit", command = submit)
submitButton.grid(row = 1, column = 3, rowspan=2, columnspan=2)
top.mainloop()

name = tkFileDialog.askopenfile(parent=top,mode='rb',title="Choose a file")

#Get text from widgets
text = textWidget.get()
fileName = FileName.get()
top.destroy()

picture = PIL.Image.open(name)
(width, height) = picture.size #set vars height and width to pic dimensions
draw = ImageDraw.Draw(picture)
(textWidth, textHeight) = draw.textsize(str(text)) #returns the width and height of the text

#Find position for text including text dimensions
width = width - textWidth - 5
height = height - textHeight - 3

#   font = ImageFont.truetype("arial.ttf", 16)
draw.text((width, height), str(text), (255,255,255))
picture.show()
picture.save(fileName  + ".png", "PNG")
#   text = raw_input("Insert Text: ")
