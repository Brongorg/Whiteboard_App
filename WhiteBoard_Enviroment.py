import WhiteboardClass as WC

#Build Enviroment
buttonNames = ["stove", "sink", "Refrigerator", "Microwave", "Complete Note" ]
textLines = []
#tk.Button(window, text = "Open Note Catagories", command = createWindow).pack()
WC.createTextInput()
for i in range(len(buttonNames)):
    WC.createToolbarButton(buttonNames[i],i)

WC.window.mainloop()
#class WBtools