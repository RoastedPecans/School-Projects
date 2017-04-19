# Note: Uses Python 2.7
# Uses a GUI to create a calculator in Python
# Written May 2015

import Tkinter
from Tkinter import *
import math
global entry
entry = ' '
entry2 = ' '
entryBool = False
operation = 0 #1 = add, #2 = subtract, #3 = multiply, #4 = divide, #5 = Equals
counter = 0
answer = 0
def Zero():
    global entry
    global entry2
    print "0"
    entry = str(entry) + '0'
    label.config(text=str(entry))
    
def One():
    global entry
    global entry2
    print "1"
    entry = str(entry) + '1'
    label.config(text=str(entry))

def Two():
    global entry
    global entry2
    print "2"
    entry = str(entry) + '2'
    label.config(text=str(entry))

def Three():
    global entry
    global entry2
    print "3"
    entry = str(entry) + '3'
    label.config(text=str(entry))

def Four():
    global entry
    global entry2
    print "4"
    entry = str(entry) + '4'
    label.config(text=str(entry))

def Five():
    global entry
    global entry2
    print "5"
    entry = str(entry) + '5'
    label.config(text=str(entry))

def Six():
    global entry
    global entry2
    print "6"
    entry = str(entry) + '6'
    label.config(text=str(entry))

def Seven():
    global entry
    global entry2
    print "7"
    entry = str(entry) + '7'
    label.config(text=str(entry))

def Eight():
    global entry
    global entry2
    print "8"
    entry = str(entry) + '8'
    label.config(text=str(entry))

def Nine():
    global entry
    global entry2
    print "9"
    entry = str(entry) + '9'
    label.config(text=str(entry))

def Add():
    global counter
    global entry
    global entry2
    print "Add"
    global operation
    operation = 1
    counter = counter + 1
    entry2 = entry
    entry = ' '
    entryBool = True
    label.config(text=str(entry))

def Subtract():
    global entry
    global entry2
    global counter
    global operation 
    print "Subtract"
    operation = 2
    entry2 = entry
    counter = counter + 1
    entry = ' '
    entryBool = True
    label.config(text=str(entry))

def Multiply():
    global entry
    global entry2
    global counter
    global operation 
    print "Multiply"
    operation = 3
    entry2 = entry
    counter = counter + 1
    entry = ' '
    entryBool = True
    label.config(text=str(entry))

def Divide():
    global entry
    global entry2
    global counter
    global operation
    print "Divide"
    operation = 4
    entry2 = entry
    counter = counter + 1
    entryBool = True
    entry = ' '
    label.config(text=str(entry))

def Equals():
    global operation
    global answer
    print "Equals"
    global entry
    global entry2
    if operation == 1:
        answer = float(entry) + float(entry2)
        label.config(text = str(answer))
    if operation == 2:
        answer = float(entry) - float(entry2)
        label.config(text = str(answer))
    if operation == 3:
        answer = float(entry) * float(entry2)
        label.config(text = str(answer))
    if operation == 4:
        answer = float(entry) / float(entry2)
        label.config(text = str(answer))
    if str(answer).find('.0') == True:
        answer = int(answer)
        label.config(text = str(answer))
    entry = 0
    entry2 = 0

def Decimal():
    global entry
    entry = entry + '.'
    label.config(text=str(entry))

def Clear():
    global entry
    global entry2
    global operation
    global answer
    entry = ' '
    entry2 = ' '
    operation = 0
    answer = 0
    label.config(text=str(entry))


master = Tk()
master.title('Homework Helper Calculator')

oneButton = Button(master, text = "1", command = One)
oneButton.grid(row = 4, column = 0)

twoButton = Button(master, text = "2", command = Two)
twoButton.grid(row = 4, column = 1)

threeButton = Button(master, text = "3", command = Three)
threeButton.grid(row = 4, column = 2)

fourButton = Button(master, text = "4", command = Four)
fourButton.grid(row = 3, column = 0)

fiveButton = Button(master, text = "5", command = Five)
fiveButton.grid(row = 3, column = 1)

sixButton = Button(master, text = "6", command = Six)
sixButton.grid(row = 3, column = 2)

sevenButton = Button(master, text = "7", command = Seven)
sevenButton.grid(row = 2, column = 0)

eightButton = Button(master, text = "8", command = Eight)
eightButton.grid(row = 2, column = 1)

nineButton = Button(master, text = "9", command = Nine)
nineButton.grid(row = 2, column = 2)
        
zeroButton = Button(master, text = "0", command = Zero)
zeroButton.grid(row = 5, column = 0)

plusButton = Button(master, text = "+", command = Add)
plusButton.grid(row = 5, column = 3)

subtractButton = Button(master, text = "-", command = Subtract)
plusButton.grid(row = 4, column = 3)

multiplyButton = Button(master, text = "X", command = Multiply)
multiplyButton.grid(row = 3, column = 3)

divideButton = Button(master, text = "/", command = Divide)
divideButton.grid(row = 2, column = 3)

equalsButton = Button(master, text = "=", command = Equals)
equalsButton.grid(row = 5, column = 3)

decimalButton = Button(master, text = ".", command = Decimal)
decimalButton.grid(row = 5, column = 2)

clearButton = Button(master, text = "C", command = Clear)
clearButton.grid(row = 5, column = 1)

label = Label(master, text = str(entry))
label.grid(row=0, column = 0, columnspan = 4)

master.mainloop()
