
from tkinter import *
import sys
# from PIL import ImageTk, Image
import os
import pymysql
db = pymysql.connect("localhost", "root", "rahul", "notetaking")
cursor = db.cursor()
def insert_window():
    root=Tk()
    root.title("Insert Window")
    l1=Label(root,text="Welcome to Note Taking App",fg='blue',font=60)
    l1.place(x=20,y=10)
    root.geometry("800x600")
    lebel1=Label(root,text="Name:-",fg='blue')
    lebel1.place(x=300,y=10)
    lebel2=Label(root,text="Subject:-",fg='blue')
    lebel2.place(x=300,y=45)
    entry=Entry(root,width=55)
    entry.place(x=370,y=10)
    entry1=Entry(root,width=55)
    entry1.place(x=370,y=45)
    t1 = Text(root, width=50)
    t1.place(x=300, y=100)
    lebel3 = Label(root, text="Write Note Below:-", fg='blue')
    lebel3.place(x=300, y=75)

    def notes_insert():
        name=entry.get()
        subject=entry1.get()
        notes=t1.get('1.0','end')
        qr1 = "insert into notetaking values('" + name + "','" + subject + "','" + notes + "');"
        try:
            cursor.execute(qr1)
            db.commit()
        except:
            db.rollback()
    b0 = Button(root, text="Save", bg="green", fg="black", width=15,command=notes_insert)
    b0.place(x=310, y=520)
    b1 = Button(root, text="exit", bg="red", fg="blue", width=15,command=exit)
    b1.place(x=450, y=520)
    root.mainloop()
def update_window():
    root = Tk()
    root.title("Update Window")
    l1 = Label(root, text="Welcome to Note Taking App", fg='blue', font=60)
    l1.place(x=20, y=10)
    root.geometry("800x600")
    l1 = Label(root, text="Search the note by name:-", fg='green', font=20)
    l1.place(x=200,y=50)
    entry = Entry(root, width=50)
    entry.place(x=200, y=80)
    t1 = Text(root, width=50)
    t1.place(x=200, y=120)
    def Search_note():
        name1=entry.get()
        qr1 = "select notes from notetaking where name= \'"+name1+"\'"
        try:
            cursor.execute(qr1)
            p1=cursor.fetchall()
            print(p1[0][0])
            for i in range(0,8):
                t1.insert(END,p1[i][0])
        except:
            db.rollback()
    def update_note():
        note1 = t1.get('1.0', 'end')
        qr1="update notetaking set notes=\'"+note1+"\'"
        try:
            cursor.execute(qr1)
            db.commit()
        except:
            db.rollback()


    b0 = Button(root, text="Search", bg="green", fg="black", width=10,command=Search_note)
    b0.place(x=490, y=80)
    b1 = Button(root, text="Update", bg="green", fg="black", width=10,command=update_note)
    b1.place(x=200, y=520)
    b2 = Button(root, text="Exit", bg="red", fg="black", width=10,command=exit)
    b2.place(x=350, y=520)

    root.mainloop()
def Delete_window():
    root = Tk()
    root.title("Delete Window")
    l1 = Label(root, text="Welcome to Note Taking App", fg='blue', font=60)
    l1.place(x=20, y=10)
    root.geometry("800x600")
    l1 = Label(root, text="Search the note by name:-", fg='green', font=20)
    l1.place(x=200, y=50)
    entry = Entry(root, width=50)
    entry.place(x=200, y=80)
    t1 = Text(root, width=50)
    t1.place(x=200, y=120)
    def search_note():
        name1 = entry.get()
        qr1 = "select notes from notetaking where name= \'" + name1 + "\'"
        try:
            cursor.execute(qr1)
            p1 = cursor.fetchall()
            t1.insert(END, p1[0][0])
        except:
            db.rollback()
    def delete_note():
        name1 = entry.get()
        qr1 = "Delete from notetaking where  name=\'" + name1 + "\'"
        try:
            cursor.execute(qr1)
            db.commit()
        except:
            db.rollback()

    b0 = Button(root, text="Search", bg="green", fg="black", width=10,command=search_note)
    b0.place(x=490, y=80)
    b1 = Button(root, text="Delete", bg="green", fg="black", width=10,command=delete_note)
    b1.place(x=200, y=520)
    b2 = Button(root, text="Exit", bg="red", fg="black", width=10, command=exit)
    b2.place(x=350, y=520)

    root.mainloop()


root=Tk()
root.title("NOTE TAKING")
l1=Label(root,text="Welcome to Note Taking App",fg='blue',font=60)
l1.place(x=100,y=10)
root.geometry("500x500")
b0=Button(root,text="Add Note",bg="red",fg="blue",width=20,command=insert_window)
b0.place(x=150,y=200)
b1=Button(root,text="Update Note",bg="red",fg="blue",width=20,command=update_window)
b1.place(x=150,y=250)
b2=Button(root,text="Delete Note",bg="red",fg="blue",width=20,command=Delete_window)

b2.place(x=150,y=300)
b3=Button(root,text="Exit",bg="red",fg="blue",width=20,command=exit)
b3.place(x=150,y=350)


# img = ImageTk.PhotoImage(Image.open("pic1.jpg"))
# panel = Label(root, image = img,height=200,width=200)
# panel.place(x=50,y=50)

root.mainloop()
