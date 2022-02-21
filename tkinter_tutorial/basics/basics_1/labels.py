from cProfile import label
from tkinter import *

# labels = an area widget that holds text and/or image within a window

window = Tk() # Instantiate an instance of a window
# window.geometry("420x420") # windth and height
window.title("Python first GUI LABEL Program") # title of GUI


photo = PhotoImage(file='logo.png')

# instantiate an label
label = Label(window,
              text="Hello World Linux",
              font=('Arial',40,'bold'),
              fg='#13cf45',  # color
              bg='black',
              relief=RAISED,
              bd=10, # border 
              padx=20,
              pady=20,# space between text and border both on x and y axis 
              image= photo,
              compound='bottom'
              ) 
label.pack() # plave widget at top center of window
# label.place(x=0,y=0) # place the label in postion of window



window.mainloop() # place window on computer screen, listen for events