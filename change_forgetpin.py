from tkinter import*
from tkinter import messagebox
import sqlite3
import random
import string

def mainwindow() :
    root=Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#a90432')
    root.title("Agentask")
    root.option_add('*font','Garamond 20 bold')
    return root

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('agentask.db')
    cursor = conn.cursor()

def changepin(root) :
    global oldp_ent,newp_ent,cfnewp_ent
    root.title("Change Pin")
    changepin_frm=Frame(root,bg='#a90432')
    changepin_frm.pack()
    changepin_frm.columnconfigure((0,1),weight=1)
    changepin_frm.rowconfigure((0,8),weight=2)
    changepin_frm.rowconfigure((1,2,3,4,5,6,7),weight=1)
    
    Label(changepin_frm,text="Old Pin :",bg='#a90432',).grid(row=1,column=0,sticky='w',padx=10,pady=10)
    oldp_ent=Entry(changepin_frm,width=20)
    oldp_ent.grid(row=2,column=0,columnspan=2,pady=10)
    Label(changepin_frm,text="New Pin :",bg='#a90432',).grid(row=3,column=0,sticky='w',padx=10,pady=10)
    newp_ent=Entry(changepin_frm,width=20,show='*')
    newp_ent.grid(row=4,column=0,columnspan=2,pady=10)
    Label(changepin_frm,text="Confirm Pin :",bg='#a90432',).grid(row=5,column=0,sticky='w',padx=10,pady=10)
    cfnewp_ent=Entry(changepin_frm,width=20,show='*')
    cfnewp_ent.grid(row=6,column=0,columnspan=2,pady=10)
    
    Button(changepin_frm,text="Apply",width=10,font='Garamond 16 bold').grid(row=7,column=0,columnspan=2,pady=10)
    
def forgetpin(root) :
    global forget_frm
    root.title("Forget Pin")
    forget_frm=Frame(root,bg='#a90432')
    forget_frm.pack()
    forget_frm.columnconfigure((0,1,2),weight=1)
    forget_frm.rowconfigure((0,1,2,3),weight=1)
    
    Label(forget_frm,text="Forget your pin?",bg='#a90432',).grid(row=0,column=0,columnspan=3,padx=10,pady=20)
    Label(forget_frm,text="Enter your birth day to recieve new password",font='Garamond 15',bg='#a90432',).grid(row=1,column=0,columnspan=3,padx=10,pady=20)
    bday_spin=Spinbox(forget_frm,width=10,from_=1,to=31)
    bday_spin.grid(row=2,column=0,sticky='e',padx=10)
    bmonth_spin=Spinbox(forget_frm,width=10,from_=1,to=12)
    bmonth_spin.grid(row=2,column=1,padx=10)
    byear_spin=Spinbox(forget_frm,width=10,from_=1951,to=2021,textvariable=yearspy)
    byear_spin.grid(row=2,column=2,sticky='w',padx=10)
    
    Button(forget_frm,text="Apply",width=10,font='Garamond 16 bold',command=randompin).grid(row=3,column=0,columnspan=3,pady=30)
    
def randompin() :
    forget_frm.destroy()
    
    random_frm=Frame(root,bg='#a90432')
    random_frm.pack()
    random_frm.columnconfigure(0,weight=1)
    random_frm.rowconfigure(0,weight=2)
    random_frm.rowconfigure((1,2),weight=1)
    
    Label(random_frm,text="Here's your temporary pin!",bg='#a90432').grid(row=0,column=0,sticky='news',pady=30)
    random_pin= ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(6))
    Label(random_frm,text=random_pin,bg='#a90432',font='Garamond 30 bold').grid(row=1,column=0,sticky='news',pady=30)
    Button(random_frm,text="OK",width=10,font='Garamond 16 bold').grid(row=2,column=0,sticky='news',pady=30)
        
w=600
h=700
root=mainwindow()
#changepin(root)
yearspy=IntVar()
yearspy.set(2021)
#forgetpin(root)

root.mainloop()
