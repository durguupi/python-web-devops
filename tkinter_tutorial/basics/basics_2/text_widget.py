from cgitb import text
from tkinter import *
from PIL import Image
from PIL import ImageTk

# text widget = functions like a text area,, you can enter multiple lines of text
def submit():
    input = text.get("1.0",END)
    print(input)
 

window = Tk()
text = Text(window, bg='light yellow',
            font=("Ink Free",25),
            height=8,
            width=25,
            padx=20,
            pady=20,
            fg='purple')
text.pack()

button = Button(window,command=submit,text='SUBMIT', fg='#fc4903', bg='black',width=21,
                font=('Comic Sans',30,'bold'))
button.pack()



window.mainloop()
