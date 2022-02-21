from optparse import check_builtin
from tkinter import *
from PIL import Image
from PIL import ImageTk

window = Tk() # Instantiate an instance of a window

def display():
    if (x.get() == 1):
        print("You Agree")
    else:
        print("You don't Agree !")

width = 50
height = 50
img = Image.open("tick.png")
img = img.resize((width,height), Image.ANTIALIAS)
photo =  ImageTk.PhotoImage(img)

x = IntVar()

check_button = Checkbutton(window,
                           text = "I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg="#57c96e",
                           bg='black',
                           activeforeground='#57c96e',
                           activebackground='black',
                           padx=25,
                           pady=10,image=photo,compound='left'
                           )

check_button.pack()


window.mainloop() # place window on computer screen, listen for events