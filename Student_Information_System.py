from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("Department of Information Technology")
w = 900
h = 600
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x_axis = int((ws/2)-(w/2))
y_axis = int((hs/2)-(h/2))
root.geometry(f'{w}x{h}+{x_axis}+{y_axis}')
root.resizable(0,0)

Label(root,text="Name", font=("Comic Sans MS",18)).place(x = 20, y = 20)
name = Entry(root, font = ("Microsoft Himalaya",24,"bold"),width = 22)
name.place(x = 110, y = 20)

Label(root,text="Enroll No",font=("Comic Sans MS",18)).place(x = 450,y = 20)
id = Entry(root,font = ("Microsoft Himalaya", 24,"bold"),width = 22)
id.place(x = 600,y = 20)

Label(root,text = "Batch",font = ("Comic Sans MS",18)).place(x = 20,y = 80)
bth = Entry(root,font = ("Microsoft Himalaya", 24,"bold"),width = 22)
bth.place(x = 110,y = 80)

Label(root,text = "Semester",font = ("Comic Sans MS",18)).place(x = 450,y = 80)
sem = Entry(root,font = ("Microsoft Himalaya", 24,"bold"),width = 22)
sem.place(x = 600,y = 80)

Label(root,text = "Sr.No",font = ("Comic Sans MS",18)).place(x = 20,y = 140)
Label(root,text = "Subject",font = ("Comic Sans MS",18)).place(x = 250,y = 140)
Label(root,text = "Marks Obtained",font = ("Comic Sans MS",18)).place(x = 500,y = 140)

Label(root,text="1",font = ("Comic Sans MS",18)).place(x=40,y=200)
Label(root,text="2",font = ("Comic Sans MS",18)).place(x=40,y=250)
Label(root,text="3",font = ("Comic Sans MS",18)).place(x=40,y=300)
Label(root,text="4",font = ("Comic Sans MS",18)).place(x=40,y=350)
Label(root,text="5",font = ("Comic Sans MS",18)).place(x=40,y=400)
Label(root,text="6",font = ("Comic Sans MS",18)).place(x=40,y=450)

Label(root,text = "Data Structure",font = ("Comic Sans MS",18)).place(x = 200,y = 200)
ds = Entry(root,font = ("Microsoft Himalaya", 24,"bold"),width = 15)
ds.place(x = 514,y = 200)

Label(root, text = "Java Programming",font = ("Comic Sans MS",18)).place(x = 170,y = 250)
java = Entry(root,font = ("Microsoft Himalaya", 24,"bold"),width = 15)
java.place(x = 514,y = 250)

Label(root,text = "Operating System",font = ("Comic Sans MS",18)).place(x = 173,y = 300)
os = Entry(root,font = ("Microsoft Himalaya", 24,"bold"),width = 15)
os.place(x = 514,y = 300)

Label(root,text = "Python Programming",font = ("Comic Sans MS",18)).place(x = 153,y = 350)
python = Entry(root,font = ("Microsoft Himalaya", 24,"bold"),width = 15)
python.place(x = 514,y = 350)

Label(root,text = "SDT",font = ("Comic Sans MS",18)).place(x = 260,y = 400)
sdt = Entry(root,font = ("Microsoft Himalaya", 24,"bold"),width = 15)
sdt.place(x = 514,y = 400)

Label(root,text = "DMS",font = ("Comic Sans MS",18)).place(x = 260,y = 450)
dms = Entry(root,font = ("Microsoft Himalaya", 24,"bold"),width = 15)
dms.place(x = 514,y = 450)

Button(root,text = "Submit",bg = 'deep sky blue',font = 'Jokerman22',bd = "5",width = 12).place(x = 300, y = 540)

root.mainloop()