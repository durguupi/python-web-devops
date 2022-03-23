from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk

# filepath = filedialog.askopenfilename(initialdir='', title="Open file OKAY?")

def openfile():
    filepath = filedialog.askopenfilename(title="Open file OKAY?",
                                          filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    # print(filepath)
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(window,command=openfile,text='OPEN', fg='#fc4903', bg='black',width=21,
                font=('Comic Sans',30,'bold'))
button.pack()





window.mainloop()