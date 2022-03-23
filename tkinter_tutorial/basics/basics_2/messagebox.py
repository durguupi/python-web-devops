from email import message
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

def click():
    # messagebox.showinfo(title="INFO BOX", message="You are awesome")
    # messagebox.showwarning(title='WARNING!',message="System has a Virus!!")
    # messagebox.showerror(title="ERROR",message="Something went Wrong")
    
    # if messagebox.askokcancel(title="ASK OK CANCEL", message="Do you want to do thing"):
    #     print("You did the thing !")
    # else:
    #     print("You cancelled a thing !")
    if messagebox.askyesno(title="Ask Yes or No", message="Do you like cake ?",icon='warning'):
        print("I like cake too !")
    else:
        print("Why do you not like cake ?")
        
    

window = Tk()

button = Button(window,command=click,text='CLICK ME', fg='#fc4903', bg='black',width=20,
                font=('Comic Sans',30,'bold'))
button.pack()

window.mainloop()