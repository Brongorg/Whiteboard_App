import WhiteboardClass as WC

#Build Enviroment
buttonNames = ["stove", "sink", "Refrigerator", "Microwave"]
textLines = []
#tk.Button(window, text = "Open Note Catagories", command = createWindow).pack()
WC.createTextInput()

for i in range(len(buttonNames)):
    WC.createToolbarButton(buttonNames[i],i)
WC.createCloseButton(i)

#WC.window.attributes('-fullscreen', True) #Sets window to full screen
WC.window.mainloop()
#class WBtools