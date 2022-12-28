import WhiteboardClass as WC

#Build Enviroment
buttonNames = ["stove", "sink", "Refrigerator", "Microwave"]
textLines = []
#tk.Button(window, text = "Open Note Catagories", command = createWindow).pack()
WC.createTextInput(len(buttonNames))

WC.placeButtonsToScreen(buttonNames)
#WC.window.attributes('-fullscreen', True) #Sets window to full screen
WC.window.mainloop()
#class WBtools