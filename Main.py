import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import sqlite3


def submit() :
    #connect DataBse
    conn = sqlite3.connect('database_book.db')
    #create Cursor
    c = conn.cursor()
    
    #insert into Table  

    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name)",
            { 
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                
            })


    #commit changes
    conn.commit()
    #close Connection
    conn.close()

    
    #Clear the Text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)


def query():
    conn = sqlite3.connect('database_book.db')
    #create Cursor
    c = conn.cursor()
    
    #Query Database
    c.execute("SELECT * , oid FROM addresses")
    records= c.fetchall()
    #print(records)
    
    print_records=''
    for record in records :
        print_records += str(record[2]) + "\t " + str(record[0]) +" " + str(record[1])   +"\n"
    
    query_label=Label(jendela,text=print_records)
    query_label.grid(row=15,column=0,columnspan=2)

    #commit changes
    conn.commit()
    #close Connection
    conn.close()

def delete() :

    #create Connection
    conn = sqlite3.connect('database_book.db')
    #create Cursor
    c = conn.cursor()

    #delete Record
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    #commit changes
    conn.commit()

    #close Connection
    conn.close()

#def update():
   
   

# Database
"""
#create a database
conn = sqlite3.connect('database_book.db')
#create Cursor
c = conn.cursor()

#create table
c.execute('''CREATE TABLE addresses (
          Firstname text,
          Last_name text
          )''')

#commit changes
conn.commit()

#close Connection
conn.close()
"""

#inisialisasi Tampilan
jendela=tk.Tk()
jendela.title('Belajar tkinter')
#jendela.iconbitmap=('')
jendela.geometry("400x400")


# Menambahkan Textbox
f_name=Entry(jendela, width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name=Entry(jendela, width=30)
l_name.grid(row=1,column=1)

delete_box=Entry(jendela, width=30)
delete_box.grid(row=8,column=1)

# Menambahkan Label
f_name_label=Label(jendela, text="Firtname")
f_name_label.grid(row=0,column=0,padx=20)
l_name_label=Label(jendela,text="lastname")
l_name_label.grid(row=1,column=0)
delete_box_label=Label(jendela, text="Delete ID")
delete_box_label.grid(row=8,column=0)

# Menambahkan Tombol submit
Submit_btn= tk.Button(jendela,text="Insert record baru",command= submit)
Submit_btn.grid(row=6,column=0, columnspan=2,pady=10,padx=10,ipadx=10)

# Menambahkan Tombol query
query_btn= tk.Button(jendela,text="Show Record",command= query)
query_btn.grid(row=7,column=0, columnspan=2,pady=2,padx=10,ipadx=100)

# Menambahkan Tombol delete
delete_btn= tk.Button(jendela,text="delete",command= delete)
delete_btn.grid(row=9,column=0, columnspan=2,pady=2,padx=10,ipadx=100)

#create update Button
#update_btn= tk.Button(jendela,text="update",command= update)
#update_btn.grid(row=10,column=0, columnspan=2,pady=2,padx=10,ipadx=100)


# Program dijalankan 
jendela.mainloop()


