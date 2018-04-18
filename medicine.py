from tkinter import Entry, Button, Tk, Label, END, Listbox, StringVar, Scrollbar
from backend import Database

database = Database("med.db")



def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in database.search(MedID_text.get(), MedName_text.get(), MedCost_text.get(), MedCompany_text.get()):
        list1.insert(END, row)


def add_command():
    database.insert(MedID_text.get(), MedName_text.get(), MedCost_text.get(), MedCompany_text.get())
    list1.delete(0, END)
    #list1.insert(END, (MedID_text.get(), MedName_text.get(), MedCost_text.get(), MedCompany_text.get()))


def get_select_row(enevt):
    global selected_data
    index = list1.curselection()[0]
    selected_data = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_data[1])
    e2.delete(0, END)
    e2.insert(END, selected_data[2])
    e3.delete(0, END)
    e3.insert(END, selected_data[3])
    e4.delete(0, END)
    e4.insert(END, selected_data[4])


def delete_command():
    id = selected_data[0]
    database.delete(id)


def update_command():
    id = selected_data[0]
    database.update(id, MedID_text.get(), MedName_text.get(), MedCost_text.get(), MedCompany_text.get())


window = Tk()
window.wm_title("MedStore")
window.configure(background="#a1dbcd")

l1 = Label(window, text='MedID')
l1.grid(row=0, column=0)

MedID_text = StringVar()
e1 = Entry(window, textvariable=MedID_text)
e1.grid(row=0, column=1)

l2 = Label(window, text='MedName')
l2.grid(row=0, column=2)

MedName_text = StringVar()
e2 = Entry(window, textvariable=MedName_text)
e2.grid(row=0, column=3)

l3 = Label(window, text='MedCost')
l3.grid(row=1, column=0)

MedCost_text = StringVar()
e3 = Entry(window, textvariable=MedCost_text)
e3.grid(row=1, column=1)

l4 = Label(window, text='MedCompany')
l4.grid(row=1, column=2)

MedCompany_text = StringVar()
e4 = Entry(window, textvariable=MedCompany_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_select_row)

b1 = Button(window, text='View all', width=12, command=view_command, bg="slate blue", fg="black")
b1.grid(row=2, column=3)

b2 = Button(window, text='Search entry', width=12, command=search_command, bg="azure", fg="black")
b2.grid(row=3, column=3)

b3 = Button(window, text='Add entry', width=12, command=add_command, bg="plum2", fg="black")
b3.grid(row=4, column=3)

b4 = Button(window, text='Update entry', width=12, command=update_command, bg="SlateGray2", fg="black")
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete', width=12, command=delete_command, bg="OliveDrab1", fg="black")
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=12, command=window.destroy, bg="SkyBlue3", fg="black")
b6.grid(row=7, column=3)

window.mainloop()
