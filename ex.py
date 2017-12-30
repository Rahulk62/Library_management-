from Tkinter import*
import sqlite3
from tkMessageBox import*
root3=Tk()
root3.geometry("500x600")
root3.title("rahul_kumar_151362 project")
def login():
    root1=Tk()
    root1.title("LOGIN")
    x = StringVar()
    y = StringVar()
    Label(root1, text = "Username ",font="Arial 10 bold",bd=10).grid(row=1,column=3)
    e6 = Entry(root1,textvariable=x,bd=10)
    Label(root1, text = "Password ",font="Arial 10 bold",bd=10).grid(row=2,column=3)
    e7 = Entry(root1, show='*',bd=10,textvariable=y)
    e6.grid(row=1, column=4)
    e7.grid(row=2,column=4)

    def close():
        us= e6.get()
        ps=e7.get()
        def Error1():
            if(str(e6.get())==''or str(e7.get())==''):
                s=showerror(title="ERROR",message="Fill the entries")
            else:
                 if(us=="rahul" and ps=="yadav02"):
                     con=sqlite3.Connection('library management')
                     cur=con.cursor()
                     root=Tk()
                     #cur.execute("create table rahullib( bname varchar(20),aname varchar(10),pname varchar(11), sub varchar(10),bno number(7),sno number(4))")
                     #cur.execute("create table  rahuliss(bno number(7),id number(10),ddate varchar(15),dd varchar(15),fine number(4))")
                     root.title('r->library management')
                     #root.geometry('1366*768')

                     Label(root,text="BOOK INFORMATION",bd=30,font="Arial 16 bold").grid(row=1,column=0,sticky=W)
                     Label(root,text="WELCOME TO LIBRARY MANAGEMENT",bd=30,font="Arial 24 bold").grid(row=0,column=0,sticky=W,columnspan=20)
                     Label(root,text="ENTER BOOK NAME",font="Arial 10 italic",bd=30 ).grid(row=2,column=0,sticky=W)
                     n=Entry(root,width=19,font="Arial 10 bold",bd=10)
                     n.grid(row=2,column=1,sticky=W,columnspan=10)
                     Label(root,text="ENTER AUTHOR NAME                    :",bd=30,font="Arial 10 italic").grid(row=3,column=0,sticky=W)
                     a=Entry(root,width=19,font="Arial 10 bold",bd=10)
                     a.grid(row=3,column=1,sticky=W)
                     Label(root,text="ENTER THE NAME OF PUBLISHER :",bd=30,font="Arial 10 italic").grid(row=4,column=0,sticky=W)
                     p=Entry(root,width=19,font="Arial 10 bold",bd=10)
                     p.grid(row=4,column=1,sticky=W)
                     Label(root,text="THE BOOK SUBJECT",bd=30,font="Arial 10 italic").grid(row=5,column=0,sticky=W)
                     s=Entry(root,width=19,font="Arial 10 bold",bd=10)
                     s.grid(row=5,column=1,sticky=W)
                     Label(root,text="THE BOOK NUMBER",bd=30,font="Arial 10 italic").grid(row=6,column=0,sticky=W)
                     e=Entry(root,width=19,font="Arial 10 bold",bd=10)
                     e.grid(row=6,column=1,sticky=W)
                     Label(root,text="SHELF NO ",bd=30,font="Arial 10 italic").grid(row=7,column=0,sticky=W)
                     sh=Entry(root,width=19,font="Arial 10 bold",bd=10)
                     sh.grid(row=7 ,column=1,sticky=W)
                     Label(root,text="BOOK ISSUE",bd=30,font="Arial 16 bold").grid(row=1,column=8,sticky=E)
                     Label(root,text="BOOK NO",font="Arial 10 italic",bd=30 ).grid(row=2,column=8,sticky=E)
                     b=Entry(root,width=19,font="Arial 10 bold",bd=10)
                     b.grid(row=2,column=9)
                     Label(root,text="STUDENT ID",bd=30,font="Arial 10 italic",).grid(row=3,column=8,sticky=E)
                     sid=Entry(root,width=19,font="Arial 10 bold",bd=10)
                     sid.grid(row=3,column=9)
                     Label(root,text="RETURN on DATE->DD-MONTH-YEAR",bd=30,font="Arial 10 italic").grid(row=4,column=8,sticky=E)
                     d=Entry(root,width=19,font="Arial 10 bold",bd=10)
                     d.grid(row=4,column=9)
                     Label(root,text="due date",bd=30,font="Arial 10 italic").grid(row=5,column=8,sticky=E)
                     dd=Entry(root,width=19,font="Arial 10 bold",bd=10)
                     dd.grid(row=5,column=9)
                     Label(root,text="FINE",bd=30,font="Arial 10 italic").grid(row=6,column=8,sticky=E)
                     f=Entry(root,font="Arial 10 bold",bd=10)
                     f.grid(row=6,column=9)
                    
                     Label(root,text="     FETCH DATA",font="Arial 14 italic",bg='light slategray').grid(row=7,column=5)
                     #fc=Entry(root,font="Arial 10 bold",bd=10)
                     #fc.grid(row=7,column=6)
                     def insertf() :
                         v=(n.get(),a.get(),p.get(),s.get(),e.get(),sh.get())
                         if(str(n.get())==''):
                             showerror(title="ERROR",message="Fill the entries")
                         else:
                             cur.execute("insert into rahullib values(?,?,?,?,?,?)",v)
                             showinfo("rahullib","BOOK INFORMATION SAVED SUCCESSFULLY !!")
                     def showallf() :
                         cur.execute("select * from rahullib\n")
                         a=cur.fetchall()
                         showinfo("Total Books ",a)
    
                         Label(root4,text=a,bd=10,font='Arial 16 bold').grid(row=1,column=0)
                         
                        
                        
                     def inserti():
                         p=(b.get(),sid.get(),d.get(),dd.get(),f.get())
                         cur.execute("insert into rahuliss values(?,?,?,?,?)",p)
                         showinfo("Issued","BOOK ISSUED SUCCESSFULY !!")
                     def showiss():
                         cur.execute("select * from rahuliss ")
                         b=cur.fetchall()
                         root5=Tk()
                         root5.geometry("500x600")
                         Label(root5,text="Book Isseued By Students Are ",bd=10,font='Arial 16 bold').grid(row=0,column=0)
                         Label(root5,text=b,bd=10,font='Arial 16 bold').grid(row=1,column=0)
    
                         Label(root4,text=a,bd=10,font='Arial 16 bold').grid(row=1,column=0)
                     def done():
                         j=b.get()
                         cur.execute("delete from rahullib where bno=(?)",(j,))
                         showinfo("task completed","issued")
                     def sdt_info():
                         pn=sid.get()
                         #pn=int(p)
                         cur.execute('select * from rahuliss where id=(?)',(pn,))
                         zn=cur.fetchall()
                         showinfo("student book_detail",zn)
                     def aboutus():
                         master=Tk()
                         shortcutbar = Frame(master, height=30, bg='light blue')
                         toolbar = Label(shortcutbar, text='PYTHON PROJECT',bg='light blue',fg='purple',height=2,font='CalibriLight 12 bold')
                         toolbar.pack(side=TOP,fill=X,expand=YES)
                         shortcutbar.pack(expand=NO, fill=X)
                         Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
                         Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
                         Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
                         Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
                         Label(master, text='\n\n\nLibrary management\n\n\nThe project is designed by',fg='black',font='Times 18').pack(side=TOP,anchor=CENTER)
                         Label(master, text='Rahul(151362)',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
                         Label(master, text='rahul.yadav.09839@gmail.com',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
                         Label(master, text='\nUnder the guiadence of',fg='black',font='Times 18').pack(side=TOP,anchor=CENTER)
                         Label(master, text='Dr. Mahesh Kumar',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
                         def sbmt():
                             master.destroy()
                             page2()
                             s = Frame(master, height=30, bg='light green')
                             Button(s, text='EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 12 bold',command=master.destroy).pack(side=LEFT, anchor=SW)
                             s.pack(side=BOTTOM,expand=NO, fill=X)
                             

                         
                     
                     Button(root,text="DONE issue",bd=10,font='Arial 16 bold',command=done).grid(row=7,column=5) 
                     Button(root,text="INSERT INFORMATION",bd=10,font='Arial 16 bold',command=insertf).grid(row=8,column=0)
                     Button(root,text="FETCH book info ",bd=10,font='Arial 16 bold',command=showallf).grid(row=8,column=5)
                     Button(root,text="Book Issued Details",bd=10,font='Arial 16 bold',command=showiss).grid(row=8,column=8)
                     Button(root,text="SAVE",bd=10,font='Arial 16 bold',command=inserti).grid(row=7,column=9)
                     Button(root,text="About us",bd=10,font='Arial 16 bold',command=aboutus).grid(row=8,column=9)
                     Button(root,text="std.detail",bd=10,font='Arial 16 bold',command=sdt_info).grid(row=7,column=8)
                 else:
                     showerror("error","incorrect password see login instruction")
                    
        Error1()
        root1.destroy()
    Button(root1,text='Submit',bg='grey',bd=10,fg='black',height=2,font='CalibriLight 12 bold',command=close).grid(row=6,column=4)
   
       
I1=PhotoImage(file="1.gif",height=200,width=400)
I2=Label(root3,image=I1).pack(side=TOP,fill=X,expand=NO)
shortcutbar = Frame(root3, height=60, bg='gray')
toolbar = Label(shortcutbar, text='PYTHON PROJECT',bg='gray',fg='black',height=2,font='CalibriLight 12 bold')
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar.pack(expand=NO, fill=X)
shortcutbar2 = Frame(root3, height=90, bg='lime')
toolbar = Label(shortcutbar2, text="Welcome To Library",bg='red',fg='black',height=2,font='CalibriLight 12 bold')
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar2.pack(expand=NO, fill=X)
'''toolbar = Label(shortcutbar, text='',bg='lime',fg='black',height=2,font='CalibriLight 12 bold')
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar.pack(expand=NO, fill=X)
shortcutbar2 = Frame(root3, height=60, bg='lime')
toolbar = Label(shortcutbar2, text="",bg='lime',fg='black',height=2,font='CalibriLight 12 bold')
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar2.pack(expand=NO, fill=X)
'''
shortcutbar3 = Frame(root3, height=60, bg='lime')
toolbar2 = Label(shortcutbar3, text="PLEASE login first To Access",bg='cyan',fg='black',height=2,font='CalibriLight 12 bold')
toolbar2.pack(side=TOP,expand=NO)
shortcutbar3.pack(expand=NO, fill=X)
'''
shortcutbar12 = Frame(root3, height=300, bg='lime')
shortcutbar12.pack(expand=NO, fill=X)'''
def exit1():
    root3.destroy()
Button(root3,text="EXIT",bd=10,bg='light blue',fg='black',font='Times 12 bold',command=exit1).pack(side=BOTTOM,fill=X,anchor=W)
def logini():
    root4=Tk()
    #root4.geometry('300*500')
    root4.title("Instruction")
    Label(root4,text="TO LOGIN PLEASE ENTER USERNAME and PASSWORD GIVEN BELOW -:",fg='black',height=2,font='CalibriLight 12 bold').grid(row=0,column=0)
    Label(root4,text="USERNAME = rahul And PASSWORD = yadav02 -:",fg='black',height=2,font='CalibriLight 12 bold').grid(row=1,column=0)
    Label(root4,text="HAVE A NICE DAY !!",fg='black',height=2,font='CalibriLight 12 bold').grid(row=2,column=0)
    Label(root4,text="THANK YOU !!",fg='black',height=2,font='CalibriLight 12 bold').grid(row=3,column=0) 
Button(root3,text="LOGIN ",bd=10,bg='light blue',fg='black',font='Times 12 bold',command=login).pack(side=BOTTOM,fill=X,anchor=NE)
Button(root3,text="LOGIN Instructions",bd=10,bg='light blue',fg='black',font='Times 12 bold',command=logini).pack(side=BOTTOM,fill=X,anchor=W)
                                                                                                    
root3.mainloop()
