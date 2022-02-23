from tkinter import * 
from db import Database
from tkinter import messagebox

db = Database('store.db')

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END,row)

def add_item():
    if part_text.get() == '' or customer_text.get() == '' \
        or retail_text.get()=='' or price_text.get() == '':
        messagebox.showerror(title="Required Fields", message="Please include all fields")
        return
    db.insert(part_text.get(), customer_text.get(), retail_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END,part_text.get(), customer_text.get(), retail_text.get(), price_text.get())
    clear_text()
    populate_list()

def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retail_entry.delete(0, END)
        retail_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], part_text.get(), customer_text.get(),
              retail_text.get(), price_text.get())
    populate_list()


def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retail_entry.delete(0, END)
    price_entry.delete(0, END)

    
    
# create window project
app = Tk()

# Part Name 
part_text = StringVar()
part_label = Label(app, text="Part Name", font=('bold',14), pady=20,padx=5,bg='white')
# Imagine in the form of grid 
part_label.grid(row=0, column=0, sticky=W)
# Entry widget
part_entry = Entry(app, textvariable=part_text,bg="#f7ffde")
part_entry.grid(row=0,column=1)

# Customer
customer_text = StringVar()
customer_label = Label(app, text="Customer", font=('bold',14),bg='white')
# Imagine in the form of grid 
customer_label.grid(row=0, column=2, sticky=W)
# Entry widget
customer_entry = Entry(app, textvariable=customer_text,bg="#f7ffde")
customer_entry.grid(row=0,column=3)

# Retailer
retail_text = StringVar()
retail_label = Label(app, text="Retailer", font=('bold',14),padx=5,bg='white')
# Imagine in the form of grid 
retail_label.grid(row=1, column=0, sticky=W)
# Entry widget
retail_entry = Entry(app, textvariable=retail_text,bg="#f7ffde")
retail_entry.grid(row=1,column=1)

# Price
price_text = StringVar()
price_label = Label(app, text="Price", font=('bold',14),bg='white')
# Imagine in the form of grid 
price_label.grid(row=1, column=2, sticky=W)
# Entry widget
price_entry = Entry(app, textvariable=price_text,bg="#f7ffde")
price_entry.grid(row=1,column=3)

# Parts list (listbox)
parts_list = Listbox(app, height=8, width=70, border=0,bg="#f7ffde",selectbackground='white')
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
parts_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=parts_list.yview)
# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# ADD Buttons
add_button = Button(app, text="Add Part", width=12, command=add_item,bg='white',activebackground='white')
add_button.grid(row=2, column=0, pady=20)
# REMOVE Buttons
remove_button = Button(app, text="Remove Part", width=12, command=remove_item,bg='white',activebackground='white')
remove_button.grid(row=2, column=1)
# Update Buttons
update_button = Button(app, text="Update Part", width=12, command=update_item,bg='white',activebackground='white')
update_button.grid(row=2, column=2)
# CLEAR Buttons
add_button = Button(app, text="Clear Input", width=12, command=clear_text,bg='white',activebackground='white')
add_button.grid(row=2, column=3)


app.title('Part Manager')
app.geometry("700x350")
app.config(background="white")

# Populate data
populate_list()


# Start Program
app.mainloop()

# To make it executable in windows
# pyinstaller main.py --one-file --windowed