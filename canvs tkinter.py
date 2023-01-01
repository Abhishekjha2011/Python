import tkinter
from tkinter import*
top=Tk()

top.geometry("400x250")

# CANVAS :- support graphics ,pie chart,gemoetric shape:-
"""c=Canvas(top,bg='Red',height='300',width='200')
arc=c.create_arc((5,10,200,360),start=0,extent=150,fill="white")
c.pack()"""


#checkbutton:-
"""checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
chkbtn1=Checkbutton(top,text="c",variable=checkvar1,onvalue=1,offvalue=0,height=2,width=10)
chkbtn2=Checkbutton(top,text="c++",variable=checkvar2,onvalue=1,offvalue=1,height=2,width=10)
chkbtn3=Checkbutton(top,text="Java",variable=checkvar3,onvalue=1,offvalue=0,height=2,width=10)
chkbtn1.pack()
chkbtn2.pack()
chkbtn3.pack()"""

#Listbox:-
"""lbl=Label(top,text="A list of favourite countries...")
listbox=Listbox(top)
listbox.insert(1,"INDIA")
listbox.insert(2,"RUSSIA")
listbox.insert(3,"JAPAN")
listbox.insert(4,"AUSTRELIA")
lbl.pack()
listbox.pack()
#Delete button:-
btn=Button(top,text="delete",command=lambda listbox=listbox:listbox.delete(ANCHOR))
btn.pack()"""
#Menu box ADD & Quit:-
"""def hello():
    print("Hello")
menubar=Menu(top)
menubar.add_command(label="Hello!",command=hello)
menubar.add_command(label="Quit!",command=top.destroy)
top.config(menu=menubar)"""
#Menubar :-
Menubar=Menu(top)
file=Menu(menubar,tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as..")
file.add_command(label="Close")
file.add_separator()
file.add_command(label="Exit",command=top.quit)
menubar.add_cascade(label="File",menu=File)
edit=Menu(menubar,tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select all")
menubar.add_cascade(label="Edit",Menu=edit)
help=Menu(menubar,tearoff=0)
help.add_command(label="About")
menubar.add_cascade(label="Help",menu=help)
top.config(menu=menubar)
top.mainloop()




top.mainloop()


