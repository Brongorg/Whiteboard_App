import tkinter as  tk #import *
from datetime import datetime

#Window Size variables

#Global Variables
fileName = "WhiteboardLog.txt" #Default text file to read and write to
height = 1080 #Default height of the window
width = 1920  #default width of the window
txtheight = 15
lastRow = 0
recentEntries = []
button_width = width/12.5
inputLine = None
count = 0

window = tk.Tk(className = "Whiteboard App") #Base root window that the whole project relies on. 
window.geometry(str(width)+ 'x'+ str(height))
file = str(fileName)
fileRead = open(file, "r+")



def createWindow():
    return tk.Toplevel() # creates a top window on top of lower window

#Button Functions

def createToolbarButton(buttonName,index, tl): #creates a button with the names stored in an input array
    prog_button = tk.Button(window, text = str(buttonName), padx = button_width, pady = 30, command = lambda: useButton(buttonName, tl), bg = "grey")
    prog_button.place( x = 0 + (button_width*2.1*index) , y = height - 150)
     

def useButton(name, entry): #Experiemental function to create a label
    name = str(name) + " Observation"
    entry.insert(30,name)
    
    
def createFunctionButtons(index, length):
    save_Button = tk.Button(window, text = "Save",  padx = button_width, pady = 30, bg = "grey", command=saveButton ) #Should save what ever is in the recent entires array
    close_button = tk.Button(window, text = "Close",  padx = button_width, pady = 30, bg = "grey", command=closeButton )
    save_Button.place(x = 0 + (button_width*2.1*(index+1)) , y = height - 150)
    close_button.place(x = 0 + (button_width*2.1*(index+2)) , y = height - 150)
    
def placeButtonsToScreen(buttonNames):
    for i in range(len(buttonNames)):
        createToolbarButton(buttonNames[i],i,inputLine)
    createFunctionButtons(i, len(buttonNames))



def saveButton():

    file = str(fileName)
    fileWrite = open(file, "r+")
    for i in range(len(recentEntries)):
        currentLine = recentEntries[i]
        fileWrite.write(currentLine)
    fileWrite.close()
        
    
def closeButton(): #Use if the complete note button is pressed
    window.destroy()



#Entry Functions


def createTextInput(): #Used to add text to the screen 
    textLine = tk.Entry(window, width = 100, borderwidth=5, bg = "grey", fg = "black")
    textLine.place(y = height - 200, x = 0)
    logInstance = datetime.now()
    prt = logInstance.strftime("%m/%d/%y %H:%M:%S") + " : "
    textLine.insert(0,prt)
    return textLine

def createTextlabel(input, num): #Creates a label on the window with the text of the input variable converted to a string, and places based on number of entries created
    txtLabel = tk.Label(window, text = str(input))
    global lastRow
    if num < 2:
          txtLabel.place(x = 0, y = 0)
    else:
         txtLabel.place(x = 0, y = lastRow + txtheight )
         lastRow = lastRow + txtheight
   

def entryFieldtoLabel(en): ##appends the text from the designated entry to the Master array, 
    currentEntry = en.get()
    recentEntries.append(currentEntry)
    createTextlabel(currentEntry, len(recentEntries))
    
def createAddEntryButton(en): 
    addButton = tk.Button(text = "Add", padx = 5, pady = 2, command=lambda: addEntryFunction(en), bg = "grey")
    addButton.place(x = 610, y = height - 200)
    
def addEntryFunction(en):
    entryFieldtoLabel(en)

def runTextField():
    global inputLine
    inputLine = createTextInput()
    createAddEntryButton(inputLine)
    

while True:
    line = fileRead.readline()
    line.strip() # If this works it should remove any newline stored in the variable
    recentEntries.append(line)
    
    if not line:
        break
    
    createTextlabel(recentEntries[count], len(recentEntries))
    count += 1
    
    
    