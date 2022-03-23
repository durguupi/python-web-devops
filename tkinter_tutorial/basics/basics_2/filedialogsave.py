from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk

def save():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("Text Files","*.txt"),
                                               ("HTML File",".html"),
                                               ("All Files","*.*")])
    # To avoid exceptions ==> when we don't write anything and then trying to close the file
    if file is None:
        return 
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()


window = Tk()
text = Text(window, bg='light yellow',
            font=("Ink Free",25),
            height=8,
            width=25,
            padx=20,
            pady=20,
            fg='purple')
text.pack()

button = Button(window,command=save,text='SAVE', fg='#fc4903', bg='black',width=21,
                font=('Comic Sans',30,'bold'))
button.pack()
window.mainloop()