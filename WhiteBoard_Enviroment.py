import tkinter as  tk #import *

window = tk.Tk() #Base root window that the whole project relies on. 
def createWindow():
    return tk.Toplevel() # creates a top window on top of lower window

def createlabel(input): #Creates a label on the window with the text of the input variable converted to a string
    return tk.Label(window, text = str(input))

def createToolbarButton(buttonName,index): #creates a button with the names stored in an input array
    prog_button = tk.Button(window, text = str(buttonName), padx = 50, pady = 20, command = useButton, bg = "grey")
    prog_button.grid(row = 0, column = index)

def useButton(): #Experiemental function to create a label
    createlabel("button was clicked")
    

def completeButton(): #Use if the complete note button is pressed
    return " "

def createTextInput(): #Used to add text to the screen 
    textLine = tk.Entry(window, width = 100, bg = "grey", fg = "black")

def textTranslate(entry): #Pulls the string from an entry on the window
    return entry.get()

def textPush(stringArray, entry): ##appends the text from the designated entry to the Master array
    stringArray.append(textTranslate(entry))


#Build Enviroment
buttonNames = ["stove", "sink", "Refrigerator", "Microwave", "Complete Note" ]
textLines = []
#tk.Button(window, text = "Open Note Catagories", command = createWindow).pack()
for i in range(len(buttonNames)):
    createToolbarButton(buttonNames[i],i)

window.mainloop()
#class WBtools