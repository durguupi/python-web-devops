from tkinter import *
from PIL import Image
from PIL import ImageTk

# Entry widget = textbox that accepts a single line of user input
window = Tk() # Instantiate an instance of a window

def submit():
    username = entry.get()  # Gets the string which we type in entry 
    print(f"Hello {username}")
    
def delete():
    entry.delete(0,END) # This will delete the entry box characters from start to end

def backspace():
    entry.delete(len(entry.get()) -1 ,END) # Getting the postion of string since we have to delete with one space


entry = Entry(window,
              font=('Arial', 50),
              fg= "#bf1932",
              bg='#dbdacc')
entry.pack(side=LEFT)

# Defining submit button
submit_button = Button(window, text="SUBMIT",command=submit)
submit_button.pack(side=RIGHT)
# Defining Delete button
delete_button = Button(window, text="DELETE",command=delete)
delete_button.pack(side=RIGHT)
# Defining backspace button
backspace_button = Button(window, text="BACKSPACE",command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop() # place window on computer screen, listen for events