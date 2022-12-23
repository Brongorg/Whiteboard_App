import tkinter as  tk #import *
from datetime import datetime

#Window Size variables

#Global Variables
fileName = "WhiteboardLog.txt"
txtRow = 0
recentEntries = []

window = tk.Tk(className = "Whiteboard App") #Base root window that the whole project relies on. 
window.geometry("500x200")
def createWindow():
    return tk.Toplevel() # creates a top window on top of lower window

def createTextlabel(input): #Creates a label on the window with the text of the input variable converted to a string
    txtLabel = tk.Label(window, text = str(input))
    txtLabel.grid(row = txtRow, column = 0)
    txtRow = txtRow+1

def createToolbarButton(buttonName,index): #creates a button with the names stored in an input array
    prog_button = tk.Button(window, text = str(buttonName), padx = 50, pady = 20, command = useButton, bg = "grey")
    prog_button.grid(row = 1, column = index) 

def useButton(): #Experiemental function to create a label
    return "hi"
    
def createFunctionButtons(index):
    save_Button = tk.Button(window, text = "Save",  padx = 50, pady = 20, bg = "grey", command=saveButton ) #still closes the window needs to be changed
    save_Button.grid(row = 1, column = index + 1)
    close_button = tk.Button(window, text = "Close",  padx = 50, pady = 20, bg = "grey", command=closeButton )
    close_button.grid(row = 1, column = index+2)


def saveButton():

    file = str(fileName)
    fileWrite = open(file, "r+")
    for i in range(len(recentEntries)):
        fileWrite.write(recentEntries[i] + " \n")
    fileWrite.close()
        
    
def closeButton(): #Use if the complete note button is pressed
    window.destroy()

def createTextInput(): #Used to add text to the screen 
    textLine = tk.Entry(window, width = 100, borderwidth=5, bg = "grey", fg = "black")
    textLine.grid(row = txtRow, column = 0)
    logInstance = datetime.now()
    prt = logInstance.strftime("%m/%d/%y %H:%M:%S") + " : "
    textLine.insert(0,prt)

def saveEntry(entry): #Pulls the string from an entry on the window
    return entry.get()

def entryFieldtoLabel(en): ##appends the text from the designated entry to the Master array
    currentEntry = saveEntry(en)
    createTextlabel(currentEntry)