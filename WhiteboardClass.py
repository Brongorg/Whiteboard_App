import tkinter as  tk #import *
from datetime import datetime

window = tk.Tk(className = "Whiteboard App") #Base root window that the whole project relies on. 
window.geometry("500x200")
def createWindow():
    return tk.Toplevel() # creates a top window on top of lower window

def createlabel(input): #Creates a label on the window with the text of the input variable converted to a string
    return tk.Label(window, text = str(input))

def createToolbarButton(buttonName,index): #creates a button with the names stored in an input array
    prog_button = tk.Button(window, text = str(buttonName), padx = 50, pady = 20, command = useButton, bg = "grey")
    prog_button.grid(row = 1, column = index)
    
def createCloseButton(index):
    close_button = tk.Button(window, text = "Close",  padx = 50, pady = 20, bg = "grey", command=closeButton )
    close_button.grid(row = 1, column = index+1)

def useButton(): #Experiemental function to create a label
    return "hi"
    

def closeButton(): #Use if the complete note button is pressed
    window.destroy()

def createTextInput(): #Used to add text to the screen 
    textLine = tk.Entry(window, width = 100, borderwidth=5, bg = "grey", fg = "black")
    textLine.grid(row = 0, column = 0)
    logInstance = datetime.now()
    prt = logInstance.strftime("%m/%d/%y %H:%M:%S") + " : "
    textLine.insert(0,prt)

def textTranslate(entry): #Pulls the string from an entry on the window
    return entry.get()

def textPush(stringArray, entry): ##appends the text from the designated entry to the Master array
    stringArray.append(textTranslate(entry))