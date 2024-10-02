from tkinter import *
def comp():
	with open(D.get(),'w') as dir:
		dir.write(t.get("1.0","end-1c"))
		
root=Tk()
l=Label(root,text="IDE BY BOOMDAQTW")
l.pack()
D=StringVar()
t=Text(root,bg="black",fg='white')
p=Button(root,text="ENTER",command=comp)
p.pack(side=BOTTOM)
t.pack()
e=Entry(root,textvar=D)
e.pack()
#t.insert(END,k)

root.mainloop()