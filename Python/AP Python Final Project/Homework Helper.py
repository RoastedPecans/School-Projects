#import needed libraries
import Tkinter
from Tkinter import *
from tkFileDialog import *
import math
import PIL
from PIL import Image
from PIL import ImageDraw

#Create Image for Graphing Calculator
img1 = Image.new("RGB", (500, 500), "white") #Create blank white image
draw = ImageDraw.Draw(img1)
draw.line((2, 2, 2, 497), fill=0) #Draw the axis with 2 pixel margin
draw.line((2, 497, 497, 497), fill=0)
j = 2
k = 498
while j < 500:
    draw.line((j, 497, j, 492), fill=0)
    j = j + 10
while k > 0:
    draw.line((2, k, 7, k), fill = 0)
    k = k - 10


def openSorter():
    List = [] # Make a blank list
    Max = raw_input("Enter amount of numbers: ") #Set max length of list
    option = raw_input("Ascending or Descending? ")
    option.lower() #Change to all lower case
    while len(List) < int(Max):
        num = input("Enter a Number: ")
        List.append(num) #add user input to list
        
    if option[0] == "a": #If user chose ascending
        sortedList = sorted(List, key=int)
    elif option[0] == "d": #if user chose descending
        sortedList = sorted(List, key=int, reverse=True)
    else:
        "Input not valid. Check your spelling."
    print sortedList

def openFormula():
    failSafe = False
    while failSafe == False:
        print "Key:"
        print "1 = Linear"
        print "2 = Exponential"

        choice = raw_input("Enter a number: ")

        if int(choice) == 1:
            failSafe = True
            print "\nLinear Chosen"
            print "y = m(x)+b"
            print "Will calculate M (slope)"
            
            M = raw_input("enter your M: ")
            (X,Y) = raw_input("Enter coordinates of a point: X Y ").split()
            

            #Partner One decided to use floats instead of ints
            B = (float(Y)- (float(M)*(float(X))))
            print "Y-Intercept is " + str(B)

        elif int(choice) == 2:
            
            failSafe = True
            print "Exponential Chosen"
            print "y = b^x"
            print "Will calculate Starting Value (a)"

            B2 = raw_input("Enter the Growth Factor: ")
            (X2, Y2) = raw_input("Enter the coordinates of a point: X Y ").split()

            ''' print B2
            print X2
            print Y2'''
            #Start = #starting value (a) of the expenential equ
            #Convert ints to floats to allow for decimals
            B2 = float(B2)
            X2 = float(X2)
            #Calculate the answer. Used pow from the math module
            answer = float(Y2) / pow(B2, X2)
            print "The starting value is: " + str(answer)
        else:
            #keep looping main menu
            failSafe = False
            print "Enter either a 1 or a 2"

def openGraphing():
    def Graph(m, y, save, graph):
        #calculate Points.
        if graph[0] == 'l':
            for i in range(499): #Loop through other X Values
                Y2 = ((m * i) + y) #Get Y value
                X3 = (2 + i)
                print str(X3) + " " + str(Y2) #Print coordinates
                if int(X3) < 497 and int(Y2) < 497:
                    img1.putpixel((int(X3), int(497 - Y2)), 0) #Paint pixel on graph at X3, Y3 
            img1.show() #Show the image
            save.lower()
            if save[0] == 'y':
                img1.save('Graph.jpg')
        if graph[0] == 'e':
            for i in range(499): #Loop through other X Values
                Y2 = (y * (math.pow(m,i))) #Get Y value
                X3 = (2 + i)
                print str(X3) + " " + str(Y2) #Print coordinates
                if int(X3) < 497 and int(Y2) < 497:
                    img1.putpixel((int(X3), int(497 - Y2)), 0) #Paint pixel on graph at X3, Y3 
            img1.show() #Show the image
            save.lower()
            if save[0] == 'y':
                img1.save('Graph.jpg')
        if graph[0] == 's':
            for i in range(499): #Loop through other X Values
                Y2 = (m * math.sqrt(i) + y) #Get Y value
                X3 = (2 + i)
                print str(X3) + " " + str(Y2) #Print coordinates
                if int(X3) < 497 and int(Y2) < 497:
                    img1.putpixel((int(X3), int(497 - Y2)), 0) #Paint pixel on graph at X3, Y3 
            img1.show() #Show the image
            save.lower()
            if save[0] == 'y':
                img1.save('Graph.jpg')

    graph = raw_input("Linear, Exponential, or Square Root?")
    save = raw_input("Do you want the graph saved? ")
    graph = graph.lower()
    graph = graph.strip()
    if graph[0] == 'l':
        m = raw_input("Enter your Positive Slope: ") 
        y = raw_input("Enter your Positive Y-Intercept: ")
    elif graph[0] == 'e':
        m = raw_input("Enter your growth factor: ")
        y = raw_input("Enter your Positive Y-intercept: ")
    elif graph[0] == "s":
        m = raw_input("Enter your positive a: ")
        y = raw_input("Enter your vertical change: ")

    m = float(m) #Convert to floats to support decimals
    y = float(y)

    Graph(m, y, save, graph)

############Individual Project Addition#############
def openTrigTriCalc():
    pi = math.pi #set pi constant using python math funcion
    cont = 'true'  #set contiue loop to true, break if false

    prevAns = []        #creats list object to hold the stored values from the prev questions

    print "This calculator will calculate the measures of sides C and A" + '\n' + "\n" + 'Geometry Reminder: Angle B (90 degrees) oppisite Hypotenuse, Angle C opposite side C, Angle A opposite side A' + '\n'

    while cont == 'true':          #contiune loop that loops while the user wants to continue use    
        angleA = raw_input("Enter the Measure of Angle A In Degrees: ") #get angle A val
        angleB = 90                                                     #set right angle to 90 deg
        angleC = 180 - (int(angleA)+int(angleB))                        #calculate remaining angle measure

        #take angle meausre and convert form degs to rads
        angA = float(float(angleA)/float(180))*float(pi)
        angB = float(float(angleB)/float(180))*float(pi)
        angC = float(float(angleC)/float(180))*float(pi)


        sideB = raw_input('Enter the Length of the Hypotenuse: ')      #get hypotenuse measure
        print '_________________________________________________'
        sideC = float((float((math.sin(angC)))*float(sideB)))           #calculate sides C and A
        sideA = float((float((math.sin(angA)))*float(sideB)))

        print 'The length of side C is: ' + str(sideC)                  #prints measures
        print 'The length of side A is: ' + str(sideA)
        print '_________________________________________________'
        response = raw_input("Do you want to continue? Y/N ")
        if response == 'Y':
            showPrev = raw_input("Would You Like to See the Previous Answers? Y/N ")
        else:
            showPrev = 'N'
        prevAns.append( sideC )             #adds the sideC length to the answer list
        prevAns.append( sideA )             #adds the sideA length to the answer list


        if showPrev == 'Y':                 #if user input is yes, shows stored answers
            print '_________________________________________________'
            print prevAns
        
        if response == 'Y':
            cont = 'true'
        elif response == 'N':
            cont = 'false'

        else:
            print 'Input a Valid Answer'
            response = raw_input("Do you want to continue? Y/N ")       #if invalid input, re-ask
            if response == 'Y':
                cont = 'true'
                print "\n" +"_____________On to the Next Problem______________" + "\n"
            elif response == 'N':
                cont = 'false'
                

    print '\n' + 'Thank You for using the Trig Calculator'

#############End Individual Project Addition##################


#############Start Of Second Individual Project###############

#############Declare all Variables used and set to zero/blank##############
global entry
entry = ' '
entry2 = ' '
entryBool = False
operation = 0 #1 = add, #2 = subtract, #3 = multiply, #4 = divide, #5 = Equals
counter = 0
answer = 0
answer2 = 0
enterCount = 0
    
def openCalculator():

    ##Define Functions for each key used##
    def Zero(bind): ##(bind) allows for use of hot keys##
        global entry ##Make variables globals for cross function use##
        global entry2
        print "0"
        entry = str(entry) + '0' ##Add 0 to the end of the entry string
        label.config(text=str(entry)) ##Set the calculator "screen" to entry string

    def One(bind):
        global entry
        global entry2
        print "1"
        entry = str(entry) + '1'
        label.config(text=str(entry))

    def Two(bind):
        global entry
        global entry2
        print "2"
        entry = str(entry) + '2'
        label.config(text=str(entry))

    def Three(bind):
        global entry
        global entry2
        print "3"
        entry = str(entry) + '3'
        label.config(text=str(entry))

    def Four(bind):
        global entry
        global entry2
        print "4"
        entry = str(entry) + '4'
        label.config(text=str(entry))

    def Five(bind):
        global entry
        global entry2
        print "5"
        entry = str(entry) + '5'
        label.config(text=str(entry))

    def Six(bind):
        global entry
        global entry2
        print "6"
        entry = str(entry) + '6'
        label.config(text=str(entry))

    def Seven(bind):
        global entry
        global entry2
        print "7"
        entry = str(entry) + '7'
        label.config(text=str(entry))

    def Eight(bind):
        global entry
        global entry2
        print "8"
        entry = str(entry) + '8'
        label.config(text=str(entry))

    def Nine(bind):
        global entry
        global entry2
        print "9"
        entry = str(entry) + '9'
        label.config(text=str(entry))

    def Add(bind): #Called if user hits add
        global counter
        global entry
        global entry2
        print "Add"
        global operation #Sets operation to 1
        operation = 1
        counter = counter + 1
        entry2 = entry #Set entry2 to first "screen"
        entry = ' '
        entryBool = True
        label.config(text=str(entry)) #Clear calculator screen

    def Subtract(bind):
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

    def Multiply(bind):
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

    def Divide(bind):
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

    def Equals(bind):
        global operation
        global answer
        print "Equals"
        global entry
        global entry2
        global enterCount
        global answer2

        if operation == 1: #If user clicked add
            answer = float(entry) + float(entry2) #Use floats to support decimals
            label.config(text = str(answer))
        if operation == 2: #if user clicked subtract
            answer = float(entry) - float(entry2)
            label.config(text = str(answer))
        if operation == 3: #if user clicked multiply
            answer = float(entry) * float(entry2)
            label.config(text = str(answer))
        if operation == 4: #if user clicked divide
            answer = float(entry2) / float(entry)
            label.config(text = str(answer))

        if enterCount > 0 and operation == 1: #if user clicked add and answer already exists (allows building onto first answer)
            answer = float(answer2) + float(entry)
            label.config(text = str(answer))
        if enterCount > 0 and operation == 2:
            answer = float(answer2) - float(entry)
            label.config(text = str(answer))
        if enterCount > 0 and operation == 3:
            answer = float(answer2) * float(entry)
            label.config(text = str(answer))
        if enterCount > 0 and operation == 4:
            answer = float(answer2) / float(entry)
            label.config(text = str(answer))

        entry = 0
        entry2 = 0
        answer2 = answer
        answer = 0
        enterCount = enterCount + 1

    def Decimal(bind): ##Add . to entry
        global entry
        print "."
        entry = entry + '.'
        label.config(text=str(entry))

    def Clear(bind): ## Clear all variables
        print "Cleared"
        global entry
        global entry2
        global operation
        global answer
        global answer2
        global enterCount
        entry = ' '
        enterCount = 0
        answer2 = 0
        entry2 = ' '
        operation = 0
        answer = 0
        label.config(text=str(entry))

    def Delete(bind):
        global entry
        print "Clear"
        entry = entry[:-1]
        label.config(text=str(entry))

    def Pi(bind):
        global entry
        print "Pi"
        entry = entry + '3.14159'
        label.config(text=str(entry))

    def Ee(bind):
        global entry
        print "e"
        entry = entry + "2.71828"
        label.config(text=str(entry))

    def Graph(bind):
        openGraphing()


    master = Tk() #Create Tkinter Instance
    master.title('Homework Helper Calculator') #Set title of window to Homework helper calculator
    master.focus_set() #Bring window to front

    ##Create keyboard binding##
    master.bind('1', One)
    master.bind('2', Two)
    master.bind('0', Zero)
    master.bind('3', Three)
    master.bind('4', Four)
    master.bind('5', Five)
    master.bind('6', Six)
    master.bind('7', Seven)
    master.bind('8', Eight)
    master.bind('9', Nine)
    master.bind('<.>', Decimal)
    master.bind('+', Add)
    master.bind('-', Subtract)
    master.bind('x', Multiply)
    master.bind('*', Multiply)
    master.bind('/', Divide)
    master.bind("<Return>", Equals)
    master.bind("c", Clear)
    master.bind("<BackSpace>", Delete)
    master.bind("e", Ee)
    master.bind("p", Pi)
    master.bind("g", Graph)
    ##Create all buttons needed##
    oneButton = Button(master, text = "1", command = lambda: One(entry))
    oneButton.grid(row = 4, column = 0, sticky = N+E+S+W)

    twoButton = Button(master, text = "2", command = lambda: Two(entry))
    twoButton.grid(row = 4, column = 1, sticky = N+E+S+W)

    threeButton = Button(master, text = "3", command = lambda: Three(entry))
    threeButton.grid(row = 4, column = 2, sticky = N+E+S+W)

    fourButton = Button(master, text = "4", command = lambda: Four(entry))
    fourButton.grid(row = 3, column = 0, sticky = N+E+S+W)

    fiveButton = Button(master, text = "5", command = lambda: Five(entry))
    fiveButton.grid(row = 3, column = 1, sticky = N+E+S+W)

    sixButton = Button(master, text = "6", command = lambda: Six(entry))
    sixButton.grid(row = 3, column = 2, sticky = N+E+S+W)

    sevenButton = Button(master, text = "7", command = lambda: Seven(entry))
    sevenButton.grid(row = 2, column = 0, sticky = N+E+S+W)

    eightButton = Button(master, text = "8", command = lambda: Eight(entry))
    eightButton.grid(row = 2, column = 1, sticky = N+E+S+W)

    nineButton = Button(master, text = "9", command = lambda: Nine(entry))
    nineButton.grid(row = 2, column = 2, sticky = N+E+S+W)

    zeroButton = Button(master, text = "0", command = lambda: Zero(entry))
    zeroButton.grid(row = 5, column = 0, sticky = N+E+S+W)

    plusButton = Button(master, text = "+", command = lambda: Add(entry))
    plusButton.grid(row = 5, column = 3, sticky = N+E+S+W)

    subtractButton = Button(master, text = "-", command = lambda: Subtract(entry))
    plusButton.grid(row = 4, column = 3, sticky = N+E+S+W)

    multiplyButton = Button(master, text = "X", command = lambda: Multiply(entry))
    multiplyButton.grid(row = 3, column = 3, sticky = N+E+S+W)

    divideButton = Button(master, text = "/", command = lambda: Divide(entry))
    divideButton.grid(row = 2, column = 3, sticky = N+E+S+W)

    equalsButton = Button(master, text = "=", command = lambda: Equals(entry))
    equalsButton.grid(row = 5, column = 3, sticky = N+E+S+W)

    decimalButton = Button(master, text = ".", command = lambda: Decimal(entry))
    decimalButton.grid(row = 5, column = 2, sticky = N+E+S+W)

    clearButton = Button(master, text = "C", command = lambda: Clear(entry))
    clearButton.grid(row = 5, column = 1, sticky = N+E+S+W)

    deleteButton = Button(master, text = "<--", command = lambda: Delete(entry))
    deleteButton.grid(row = 4, column = 4, rowspan = 2, sticky = N+E+S+W)

    piButton = Button(master, text = "Pi", command = lambda: Pi(entry))
    piButton.grid(row = 3, column = 4, sticky = N+E+S+W)

    eButton = Button(master, text = "e", command = lambda: Ee(entry))
    eButton.grid(row = 2, column = 4, sticky = N+E+S+W)

    graphButton = Button(master, text = "Graph", command = lambda: Graph(entry))
    graphButton.grid(row=1, column = 5, rowspan = 5, sticky = N+E+S+W)

    label = Label(master, text = str(entry))
    label.grid(row=0, column = 0, columnspan = 4, sticky = W)

    master.mainloop() #Keep running GUI

##############End of Second Individual Addition###################

##Create GUI and call functions##
master = Tk()
master.title('Homework Helper')
master.focus_set()

Title = Label(master, text="Welcome to Homework Helper!")
Title.pack()

SortingButton = Button(master, text="Sorter", command=openSorter)
SortingButton.pack()

FormulaButton = Button(master, text="Formula Helper", command=openFormula)
FormulaButton.pack()

GraphingCalculator = Button(master, text = "Graphing Calculator", command=openGraphing)
GraphingCalculator.pack()

TrigCalculator = Button(master, text = "Triangle Length Calculator", command = openTrigTriCalc)
TrigCalculator.pack()

CalculatorButton = Button(master, text = "Calculator", command = openCalculator)
CalculatorButton.pack()
mainloop()
