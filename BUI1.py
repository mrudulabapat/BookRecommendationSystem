from tkinter import *
import sys
import os
import tkinter.messagebox


root=Tk()
root.geometry("500x500")
root.configure(background="#a1dbcd")

root.title("Book Recommendation System")


def retrieve_input():
    inputValue=textBox.get("1.0", "end-1c")

    return inputValue

textBox=Text(root, height=2, width=40)
#textBox.grid(row=2, column=0)
textBox.place(x=170, y=400, anchor="center")

button1 = Button(root, text="Search", fg="white", command=lambda: retrieve_input(), height=2, width=10, bg="blue", font="Arial 9 bold")
button1.place(x=400, y=400, anchor="center")

label_1 = Label(root, text="Book Recommendation System", bd=1, relief="solid", bg="yellow", font="Times 22 bold", width=30, height=2)
label_1.place(x=250, y=0, anchor="center")

photo = PhotoImage(file="book1.gif")
label = Label(root, image=photo, bd=1, relief="solid")
label.place(x=250, y=200, anchor="center")
#label.grid(row=1, columnspan=3)

label_2 = Label(root, text="Enter the book you have read:", font="Arial 18 bold")
label_2.place(x=180, y=350, anchor="center")
button2 = Button(root, text="GO", fg="white", command=root.quit, height=2, width=10, bg="red", font="Arial 9 bold")
button2.place(x=250, y=460, anchor="center")

label_1.grid(row=0)
#label_2.grid(row=2, sticky=W)

#textBox.grid(row=3, column=0)
#button1.grid(row=3, column=1)
#button2.grid(row=6, column=0)


root.mainloop()