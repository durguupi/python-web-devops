from tkinter import *

# widgtes = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # Instantiate an instance of a window
window.geometry("420x420") # windth and height
window.title("Python first GUI Program") # title of GUI

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

window.config(background='#7cdee6') # Hex color

window.mainloop() # place window on computer screen, listen for events


