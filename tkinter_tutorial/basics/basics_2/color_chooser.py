from tkinter import *
from tkinter import colorchooser # This is submodule so we have to import it
from PIL import Image
from PIL import ImageTk

def click():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex) # This will change background color
    # window.config(bg=colorchooser.askcolor()[1]) # one line of code

window = Tk()

window.geometry("420x420")
button = Button(window,command=click,text='CHOOSE A COLOR', fg='#fc4903', bg='black',width=20,
                font=('Comic Sans',30,'bold'))
button.pack()



window.mainloop()

