from tkinter import *
from tkinter import messagebox
import os
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('pharmacy.db')
c = conn.cursor()

# Create table
c.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        quantity INTEGER,
        category TEXT,
        discount REAL
    )
''')

# Insert a record
def insert_item(name, price, quantity, category, discount):
    c.execute("INSERT INTO items VALUES (NULL, ?, ?, ?, ?, ?)", (name, price, quantity, category, discount))
    conn.commit()

# Example usage
insert_item('Example Item', 10.99, 100, 'Medicine', 0.0)

# Close the connection
conn.close()

# Ensure file name consistency
DATABASE_FILE = "database_proj.txt"

def create_database_file():
    if not os.path.exists(DATABASE_FILE):
        open(DATABASE_FILE, 'w').close()

create_database_file()

root = Tk()
root.title("Pharmacy Management System By - Sagar")
root.configure(width=1500, height=600, bg='BLACK')
var = -1

def additem():
    global var
    num_lines = 0
    with open(DATABASE_FILE, 'r') as f10:
        for line in f10:
            num_lines += 1
    var = num_lines
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    with open(DATABASE_FILE, 'a') as f:
        f.write('{0} {1} {2} {3} {4}\n'.format(str(e1), e2, e3, str(e4), e5))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

def deleteitem():
    e1 = entry1.get()
    with open(DATABASE_FILE) as f, open("temp.txt", "w") as working:
        for line in f:
            if str(e1) not in line:
                working.write(line)
    os.remove(DATABASE_FILE)
    os.rename("temp.txt", DATABASE_FILE)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

def firstitem():
    global var
    var = 0
    with open(DATABASE_FILE, 'r') as f:
        lines = f.readlines()
        if lines:
            v = lines[0].split(" ")
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))

def nextitem():
    global var
    with open(DATABASE_FILE, 'r') as f:
        lines = f.readlines()
        if var + 1 < len(lines):
            var += 1
            v = lines[var].split(" ")
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))
        else:
            messagebox.showinfo("Title", "No more records")

def previousitem():
    global var
    with open(DATABASE_FILE, 'r') as f:
        lines = f.readlines()
        if var > 0:
            var -= 1
            v = lines[var].split(" ")
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))
        else:
            messagebox.showinfo("Title", "No previous records")

def lastitem():
    global var
    with open(DATABASE_FILE, 'r') as f:
        lines = f.readlines()
        if lines:
            var = len(lines) - 1
            v = lines[-1].split(" ")
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))

def updateitem():
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    with open(DATABASE_FILE) as f1, open("temp.txt", "w") as working:
        for line in f1:
            if str(e1) not in line:
                working.write(line)
            else:
                working.write('{0} {1} {2} {3} {4}\n'.format(str(e1), e2, e3, str(e4), e5))
    os.remove(DATABASE_FILE)
    os.rename("temp.txt", DATABASE_FILE)

def searchitem():
    e11 = entry1.get()
    with open(DATABASE_FILE) as working:
        for line in working:
            if str(e11) in line:
                v = line.split(" ")
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)
                entry5.delete(0, END)
                entry1.insert(0, str(v[0]))
                entry2.insert(0, str(v[1]))
                entry3.insert(0, str(v[2]))
                entry4.insert(0, str(v[3]))
                entry5.insert(0, str(v[4]))
                return
        messagebox.showinfo("Title", "Item not found")

def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

label0 = Label(root, text="PHARMACY MANAGEMENT SYSTEM ", bg="black", fg="white", font=("Times", 30))
label1 = Label(root, text="ENTER ITEM NAME", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
entry1 = Entry(root, font=("Times", 12))
label2 = Label(root, text="ENTER ITEM PRICE", bd="2", relief="ridge", height="1", bg="red", fg="white", font=("Times", 12), width=25)
entry2 = Entry(root, font=("Times", 12))
label3 = Label(root, text="ENTER ITEM QUANTITY", bd="2", relief="ridge", bg="red", fg="white", font=("Times", 12), width=25)
entry3 = Entry(root, font=("Times", 12))
label4 = Label(root, text="ENTER ITEM CATEGORY", bd="2", relief="ridge", bg="red", fg="white", font=("Times", 12), width=25)
entry4 = Entry(root, font=("Times", 12))
label5 = Label(root, text="ENTER ITEM DISCOUNT", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
entry5 = Entry(root, font=("Times", 12))
button1 = Button(root, text="ADD ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=additem)
button2 = Button(root, text="DELETE ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=deleteitem)
button3 = Button(root, text="VIEW FIRST ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=firstitem)
button4 = Button(root, text="VIEW NEXT ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=nextitem)
button5 = Button(root, text="VIEW PREVIOUS ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=previousitem)
button6 = Button(root, text="VIEW LAST ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=lastitem)
button7 = Button(root, text="UPDATE ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=updateitem)
button8 = Button(root, text="SEARCH ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=searchitem)
button9 = Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12), command=clearitem)
label0.grid(columnspan=6, padx=10, pady=10)
label1.grid(row=1, column=0, sticky=W, padx=10, pady=10)
label2.grid(row=2, column=0, sticky=W, padx=10, pady=10)
label3.grid(row=3, column=0, sticky=W, padx=10, pady=10)
label4.grid(row=4, column=0, sticky=W, padx=10, pady=10)
label5.grid(row=5, column=0, sticky=W, padx=10, pady=10)
entry1.grid(row=1, column=1, padx=40, pady=10)
entry2.grid(row=2, column=1, padx=10, pady=10)
entry3.grid(row=3, column=1, padx=10, pady=10)
entry4.grid(row=4, column=1, padx=10, pady=10)
entry5.grid(row=5, column=1, padx=10, pady=10)
button1.grid(row=1, column=4, padx=40, pady=10)
button2.grid(row=1, column=5, padx=40, pady=10)
button3.grid(row=2, column=4, padx=40, pady=10)
button4.grid(row=2, column=5, padx=40, pady=10)
button5.grid(row=3, column=4, padx=40, pady=10)
button6.grid(row=3, column=5, padx=40, pady=10)
button7.grid(row=4, column=4, padx=40, pady=10)
button8.grid(row=4, column=5, padx=40, pady=10)
button9.grid(row=5, column=5, padx=40, pady=10)
root.mainloop()
