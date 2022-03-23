from http.client import FOUND
from tkinter import *
from PIL import Image
from PIL import ImageTk
from click import command

# Listbox ==> A list of selectable text items within its own container
def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You have ordered: ")
    for index in food:
        print(index)
    # print(listbox.get(listbox.curselection()))
    
def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())
 
def delete():
    # listbox.delete(listbox.curselection())
    # Using reversed to allow index start from reverse
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window, 
                  bg = "#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE    # This is used for selecting multiple items in listbox
                  )
listbox.pack()
# Adding a list of items in listbox
listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Salad")
listbox.insert(5, "Soup")

# Adjusts listbox item size dynamically based on values
listbox.config(height=listbox.size())

# Adding an entry widget for the items that can be added
entrybox = Entry(window, font=('Constantia', 35),fg= "#bf1932",bg='#f7ffde' )
entrybox.pack()

# Adding a submit button
submit_button = Button(window, text="SUBMIT", command=submit, fg='#1fe02c', bg='black',width=20,
                       font=('Comic Sans',30,'bold'))
submit_button.pack()
# Adding a ADD button
add_button = Button(window, text="ADD", command=add, fg='#1f8de0', bg='black',width=20,
                    font=('Comic Sans',30,'bold'))
add_button.pack()
# Adding a DELETE button
delete_button = Button(window, text="DELETE", command=delete, fg='#fc4903', bg='black',width=20,
                       font=('Comic Sans',30,'bold'))
delete_button.pack()

window.mainloop()