from tkinter import *
from PIL import Image
from PIL import ImageTk

# Radio Button ==> Smilar to checkbox,but you can only select one from a group

window = Tk() # Instantiate an instance of a window

food =["Pizza","Burger","Salad","Sandwich"]
images = ['pizza.png','burger.png','salad.png','sandwich.png']
foodimage = []

for image in images:
    width = 50
    height = 50
    img = Image.open(image)
    img = img.resize((width,height), Image.ANTIALIAS)
    photo =  ImageTk.PhotoImage(img)
    foodimage.append(photo)

def order():
    if (x.get() == 0):
        print("You ordered Pizza !")
    elif (x.get() == 1):
        print("You ordered Burger! ")
    elif (x.get() == 2):
        print("You ordered Salad !")
    elif (x.get() == 3):
        print("You ordered Sandwich !")
    else:
        print('huh ?')   
        
x = IntVar()
frame = LabelFrame(window, text='Select Any one !',font=("roman", 50), padx=50, bg= '#aed6ba')
frame.pack()
for index in range(len(food)):
    # Creating mutiple instance of radio button using for loop
    radio_button = Radiobutton(frame,
                               text=food[index],  # Adds text to radio_buttons
                               variable=x, # Groups radio button togther if they share the same variable
                               value=index, # Asssigns each radiobutton a different value
                               padx= 25, # Padding on X axis
                               font=("roman", 50),  # Specifying the font value
                               image= foodimage[index], # Adds image to radiobutton
                               compound='right', # Adds image and text (right-side)
                               indicatoron=0, # Eleimate circle indicators
                               width= 280, # Windth of radio button
                               command = order, # Set command of radiobuttion to function
                               background = "pink"
                               )
    # radio_button.grid(column=0, row=index, sticky="W")
    radio_button.pack(fill = X,ipady = 5,side='top')











window.mainloop() # place window on computer screen, listen for events