import tkinter as  tk #import *
from datetime import datetime

#Global Variables
fileName = "WhiteboardLog.txt" #Default text file to read and write to

height = 1080 #Default height of the window
width = 1920  #default width of the window

txtheight, lastRow, count  = 20, 0, 0 #Count is used to track how many elements are in the recent arrays and create evenly spaced labels
recentEntries = []

button_width = width/12.5
inputLine = None

window = tk.Tk(className = "Whiteboard App") #Base root window that the whole project relies on. 
window.geometry(str(width)+ 'x'+ str(height)) #Takes the preset variables for size and creates the window
file = str(fileName)  #Guarentees that the file name is in a string format  
fileRead = open(file, "r+") #Opens the designated file for log entry or creates one if it doesnt exist
                            #Need to add a block that verifys that the file opened or othewrwises throws back an error



def createWindow():
    return tk.Toplevel() # creates a top window on top of lower window

#Button Functions

def createToolbarButton(buttonName,index, tl): #creates a button with the names stored in an input array
    
    prog_button = tk.Button(window, text = str(buttonName), padx = button_width, pady = 30, command = lambda: useButton(buttonName, tl), bg = "grey")
    prog_button.place( x = 0 + (button_width*2.1*index) , y = height - 150)
    
def useButton(name, entry): #Experiemental function to create a label
    
    name = str(name) + " Observation, " #Convert this to an Fstring
    entry.insert(30,name)
    
def createFunctionButtons(index, length): #Creates buttons that allow the window to be closed as well as save all entries to the txt file
    
    save_Button = tk.Button(window, text = "Save",  padx = button_width, pady = 30, bg = "grey", command=saveButton ) #Should save what ever is in the recent entires array
    close_button = tk.Button(window, text = "Close",  padx = button_width, pady = 30, bg = "grey", command=closeButton )
    
    save_Button.place(x = 0 + (button_width*2.1*(index+1)) , y = height - 150)
    close_button.place(x = 0 + (button_width*2.1*(index+2)) , y = height - 150)
    
def placeButtonsToScreen(buttonNames): #Centralized function for creating all buttons on the window 
    
    for i in range(len(buttonNames)):
        createToolbarButton(buttonNames[i],i,inputLine)
    createFunctionButtons(i, len(buttonNames))

def saveButton(): #saves all elements of the global recent entries array to the txt file 
    
    file = str(fileName)
    fileWrite = open(file, "r+")
    for i in (recentEntries):
        fileWrite.write(i+'\n')
    fileWrite.close()
        
    
def closeButton(): #Use if the complete note button is pressed
    window.destroy()


#Entry Functions

def createTextInput(): #Used to add the entry field to the screen 
    
    textLine = tk.Entry(window, width = 100, borderwidth=5, bg = "grey", fg = "black")
    textLine.place(y = height - 200, x = 0)
    logInstance = datetime.now()
    prt = logInstance.strftime("%m/%d/%y %H:%M:%S") + ", "
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
    
def createAddEntryButton(en): # Places the add button behind the field and ties it to entryFieldtLabel
    
    addButton = tk.Button(text = "Add", padx = 5, pady = 2, command=lambda: entryFieldtoLabel(en), bg = "grey")
    addButton.place(x = 610, y = height - 200)

def runTextField(): #Centralized Function for the entry functions accessed in the enviroment
    
    global inputLine
    inputLine = createTextInput()
    createAddEntryButton(inputLine)
    

while True: #Used in initialization to write all entries in the white board to the label field
    
    line = fileRead.readline()
    line.replace("\n", "") # If this works it should remove any newline stored in the variable
    if len(line)>1: #Verifies that the current line is worth writing to screen
        recentEntries.append(line) #Appends the current line in the file to the recent entry arrays
        createTextlabel(recentEntries[count], len(recentEntries))
        count += 1
        
    if not line:
        break
fileRead.close() #Ensures that the txt file is clsoed after initialization  
    
    
    
    
    