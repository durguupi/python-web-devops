from tkinter import *
from PIL import Image
from PIL import ImageTk

# Buttons = You click it, then it does stuff

window = Tk() # Instantiate an instance of a window

count = 0
def click():
    global count
    count+=1
    print(f"You clicked the button {count}")
    
width = 50
height = 50
img = Image.open("like.png")
img = img.resize((width,height), Image.ANTIALIAS)
photo =  ImageTk.PhotoImage(img)
# Instantiate a button
button = Button(window,
                text="Click me !",
                command=click,                      # perform callback function
                font=('Comic Sans',40,'bold'),
                fg='#13bccf',  # color
                bg='black',
                activeforeground='#13bccf',
                activebackground='black',
                image=photo,
                compound='bottom'
                ) 
button.pack()




window.mainloop() # place window on computer screen, listen for events
