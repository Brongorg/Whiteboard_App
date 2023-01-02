import WhiteboardClass as WC

#Build Enviroment
buttonNames = ["stove", "sink", "Refrigerator", "Microwave"]
textLines = []

WC.runTextField()

WC.placeButtonsToScreen(buttonNames)



#WC.window.attributes('-fullscreen', True) #Sets window to full screen
WC.window.mainloop()
