import calendar
from operator import ne
from tkinter import *
from tkinter import messagebox
from turtle import left
from PIL import Image
from PIL import ImageTk
import random

window = Tk()
window.title("Calendar")

# Image resizing for the title
width = 50
height = 50
img = Image.open("calendar.png")
img = img.resize((width,height), Image.ANTIALIAS)
calendar_image =  ImageTk.PhotoImage(img)

# Getting the calendar function
def cal():
    # Getting the required details from month and year entry widget
    year = entry_year.get()
    month = entry_month.get()
    # Message Box to raise Error if given month is greater than 12 or less than 0
    if int(month) <= 0 or int(month) > 12: 
        messagebox.showerror(title="ERROR",message="Enter month betwwen 1 to 12")
    # Main logic which displays only the month which we requested     
    cal_x = calendar.month(int(year),int(month),w = 2, l = 1)
    print (cal_x)
    # Declaring as global variable since we require it to delete the output of calendar
    global cal_out
    cal_out = Label(window, text=cal_x, font=('courier', 20, 'bold'), bg='lightblue', justify=LEFT,)
    cal_out.pack(padx=3, pady=10,side=TOP)
    
# Defining clear function to clear all the output and entry widget
def clear():
    cal_out.destroy()
    entry_month.delete(0, 'end')
    entry_year.delete(0, 'end')
    
# Title label 
label_title = Label(window, text="SIMPLE GUI CALENDAR",font=('Comic Sans',20,'bold'),fg='#fc00ca',bg='white',
                    image=calendar_image,compound='left')
label_title.pack(padx=10,pady=5)

# Year Label to display the year
label_year = Label(window, text="Enter a Year:",font=('Arial',20,'bold'),fg='#15eb43',bg='white')
label_year.pack(padx=10,pady=5)
entry_year = Entry(window,bg="#f7ffde",width=15,font=('Arial',20,'bold'))
entry_year.pack(padx=10,pady=5)

# Month Label to display the month
label_month = Label(window, text="Enter a Month:",font=('Arial',20,'bold'),fg='#1519eb',bg='white')
label_month.pack(padx=10,pady=5)
entry_month = Entry(window,bg="#f7ffde",width=15,font=('Arial',20,'bold'))
entry_month.pack(padx=10,pady=10)

# Create a CLEAR Button and attached to clear function
clear_button = Button(window, text="Clear", fg='white',bg = "black",
                      command=clear,width=10,
                      font=('Arial',20,'bold'),)
clear_button.pack(side='left')

# Create a Exit Button and attached to exit function
exit_button = Button(window, text = "Exit", fg='white',bg = "black",
                     font=('Arial',20,'bold'),
                     command = exit,width=10)
exit_button.pack(side='right')

# Create a SHOW Button to display the calendar by calling cal function
show_button = Button(window, text="Show",command=cal,width=15,
                fg='black',bg='red',
                font=('Arial',20,'bold'))
show_button.pack(anchor=CENTER)

window.config(bg='white')
window.mainloop()