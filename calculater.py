import math
from Tkinter import *
root=Tk()
root.title("CALCULATER")
s=Entry()
s.grid(row=0,column=0,columnspan=4)
e=Entry(root,width=16,font="Arial 30 bold",bd=30,bg="pink",justify='right')
e.grid(row=0,column=0,columnspan=4)
def add_Entry(x):
    e.insert(16,x)
def result(y):
    e.delete(0,16)
    e.insert(16,y)
def clear(a):
    e.delete(0,END)
def result1(x,y):
     e.delete(0,END)
     e.insert(16,x)
     e.insert(16,y)
def s1():
    s=float(e.get())
    a=math.radians(s)
    t=math.sin(a)
    result(t)
def c1():
    s=float(e.get())
    a=math.radians(s)
    t=math.cos(a)
    result(t)
def t1():
    s=float(e.get())
    a=math.radians(s)
    t=math.tan(a)
    result(t)    
def sqr():
    s=float(e.get())
    ans=s*s
    result(ans)
def p1():
    t=math.pi
    result(t)
def l1():
    s=float(e.get())
    t=math.log10(s)
    result(t)
def q():
    s=float(e.get())
    ans=s*s*s
    result(ans)    
  
Button(root,text="7",height=2,width=1,command=lambda:add_Entry('7'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=1,column=0,sticky=E+W+N+S)
Button(root,text="8",height=2,width=1,command=lambda:add_Entry('8'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=1,column=1,sticky=E+W+N+S)
Button(root,text="9",height=2,width=1,command=lambda:add_Entry('9'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=1,column=2,sticky=E+W+N+S)
Button(root,text="+",height=2,width=1,command=lambda:add_Entry('+'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=1,column=3,sticky=E+W+N+S)
Button(root,text="4",height=2,width=1,command=lambda:add_Entry('4'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=2,column=0,sticky=E+W+N+S)
Button(root,text="5",height=2,width=1,command=lambda:add_Entry('5'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=2,column=1,sticky=E+W+N+S)
Button(root,text="6",height=2,width=1,command=lambda:add_Entry('6'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=2,column=2,sticky=E+W+N+S)
Button(root,text="-",height=2,width=1,command=lambda:add_Entry('-'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=2,column=3,sticky=E+W+N+S)
Button(root,text="1",height=2,width=1,command=lambda:add_Entry('1'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=3,column=0,sticky=E+W+N+S)
Button(root,text="2",height=2,width=1,command=lambda:add_Entry('2'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=3,column=1,sticky=E+W+N+S)
Button(root,text="3",height=2,width=1,command=lambda:add_Entry('3'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=3,column=2,sticky=E+W+N+S)
Button(root,text="*",height=2,width=1,command=lambda:add_Entry('*'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=3,column=3,sticky=E+W+N+S)
Button(root,text="0",height=2,width=1,command=lambda:add_Entry('0'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=4,column=0,sticky=E+W+N+S)
Button(root,text="c",height=2,width=1,command=lambda:clear('c'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=4,column=1,sticky=E+W+N+S)
Button(root,text="/",height=2,width=1,command=lambda:add_Entry('/'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=4,column=2,sticky=E+W+N+S)
Button(root,text=".",height=2,width=1,command=lambda:add_Entry('.'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=4,column=3,sticky=E+W+N+S)
Button(root,text="(",height=2,width=1,command=lambda:add_Entry('('),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=5,column=0,sticky=E+W+N+S)
Button(root,text=")",height=2,width=1,command=lambda:add_Entry(')'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=5,column=1,sticky=E+W+N+S)
Button(root,text="%",height=2,width=1,command=lambda:add_Entry('%'),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=5,column=2,sticky=E+W+N+S)
Button(root,text="=",height=2,width=1,command=lambda:result(eval(e.get())),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=5,column=3,sticky=E+W+N+S)
Button(root,text="sin",height=2,width=1,command=lambda:s1(),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=6,column=0,sticky=E+W+N+S)
Button(root,text="cos",height=2,width=1,command=lambda:c1(),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=6,column=1,sticky=E+W+N+S)
Button(root,text="tan",height=2,width=1,command=lambda:t1(),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=6,column=2,sticky=E+W+N+S)
Button(root,text="x^2",height=2,width=1,command=lambda:sqr(),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=6,column=3,sticky=E+W+N+S)
Button(root,text="pi",height=2,width=1,command=lambda:p1(),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=7,column=0,sticky=E+W+N+S)
Button(root,text="log10",height=2,width=1,command=lambda:l1(),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=7,column=1,sticky=E+W+N+S)
Button(root,text="x^3",height=2,width=1,command=lambda:q(),bg="yellow",bd=7,fg="black",font="Arial 15 bold").grid(row=7,column=2,sticky=E+W+N+S)
Button(root,text="x^2",height=9,width=1,command=lambda:sqr(),bg="red",bd=7,fg="black",font="Arial 15 bold").grid(row=6,column=3,sticky=E+W+N+S)
root.mainloop()
