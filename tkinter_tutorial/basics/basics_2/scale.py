from tkinter import *
from PIL import Image
from PIL import ImageTk

def submit():
    print(f"The Temperature is : {scale.get()} degree C")

window = Tk()

width = 50
height = 50
img = Image.open("fire.png")
img = img.resize((width,height), Image.ANTIALIAS)
fireimage =  ImageTk.PhotoImage(img)
img1 = Image.open("cold.png")
img1 = img1.resize((width,height), Image.ANTIALIAS)
coldimage =  ImageTk.PhotoImage(img1)


firelabel = Label(image=fireimage)
firelabel.pack()


scale = Scale(window, 
              from_=100, 
              to=0,
              length=600,
              orient=VERTICAL, # Orientation of Scale
              font =('Consolas', 20),
              tickinterval= 10, # numeric indicators for value
              showvalue= 0, # hide current value
              resolution= 5, # increment of slider
              troughcolor="#69EAFF",
              fg = "#FF1C00",
              bg = "black"
              
              )
scale.pack()
scale.set(((scale['from'] - scale['to'])/2) + scale['to']) # set current value of slider

coldlabel = Label(image=coldimage)
coldlabel.pack()


button = Button(window,text='SUBMIT',font =('Consolas', 20,'bold'),fg='#22b50b',
                activeforeground='#22b50b',activebackground='black',
                command=submit)
button.pack()

window.mainloop()
