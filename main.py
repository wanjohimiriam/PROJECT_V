from tkinter import *

root=Tk()
root.config(bg="red")
root.title("Welcome to python basics")
root.geometry("800x600+200+100")

Name = Label(root,text="Name:")
Name.grid(row=0, column=0)
Password = Label(root, text="Password:")
Password.grid(row=1, column=0)
Town = Label(root, text="Town:")
Town.grid(row=2, column=0)
Country = Label(root, text="Country:")
Country.grid(row=3, column=0)
Submit = Button(root, text="submit:")
e1 = Entry(root)
e1.grid(row=0, column=1)
e2 = Entry(root)
e2.grid(row=1, column=1)
e3 = Entry(root)
e3.grid(row=2, column=1)
e4 = Entry(root)
e4.grid(row=3, column=1)
Gender = Label(root, text="Gender:")
Gender.grid(row=4, column=0)
M_status = Label(root, text="M.Status:")
M_status.grid(row=5, column=0)
Salary = Label(root, text="Salary:")
Salary.grid(row=6, column=0)
Submit.grid(column=1)
e5 = Entry(root)
e5.grid(row=4, column=1)
e6 = Entry(root)
e6.grid(row=5, column=1)
e7 = Entry(root)
e7.grid(row=6, column=1)








root.mainloop()