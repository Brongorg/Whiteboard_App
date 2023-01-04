import WhiteboardClass as WC

#Build Enviroment
buttonNames = ["Stove", "Sink", "Refrigerator", "Microwave"]

WC.runTextField()

WC.placeButtonsToScreen(buttonNames)

#WC.window.attributes('-fullscreen', True) #Sets window to full screen
WC.window.mainloop()
