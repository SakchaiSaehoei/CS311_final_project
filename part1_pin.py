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
    
def first_time_use(root) :
    global first_frame
    first_frame=Frame(root,bg='#a90432')
    first_frame.columnconfigure(0,weight=1)
    first_frame.rowconfigure((0,1),weight=1)
    
    Label(first_frame,bg='#a90432',image=logo).grid(row=0,column=0,sticky='news',pady=(50,20))
    Button(first_frame,text='Create Pin',command=createpin).grid(row=1,column=0,sticky='news',pady=50)
    first_frame.pack()
    
def createpin() :
    global creatpin_frm,create_pin_ent,create_cfpin_ent,bday_spin,bmonth_spin,byear_spin
    first_frame.destroy()
    
    creatpin_frm=Frame(root,bg='#a90432')
    creatpin_frm.columnconfigure((0,1,2),weight=1)
    creatpin_frm.rowconfigure((0,1,2,3,4,5,6),weight=1)
    
    Label(creatpin_frm,text="Pin :",bg='#a90432',fg='#fdb912').grid(row=0,column=0,columnspan=3,sticky='w',padx=10,pady=(30,10))
    create_pin_ent=Entry(creatpin_frm,width=20)
    create_pin_ent.grid(row=1,column=0,columnspan=3,pady=10)
    Label(creatpin_frm,text="Confirm Pin :",bg='#a90432',fg='#fdb912').grid(row=2,column=0,columnspan=3,sticky='w',padx=10,pady=10)
    create_cfpin_ent=Entry(creatpin_frm,width=20,show='*')
    create_cfpin_ent.grid(row=3,column=0,columnspan=3,pady=10)
    
    Label(creatpin_frm,text="Enter your birth day",bg='#a90432',fg='#fdb912').grid(row=4,column=0,columnspan=3,padx=10,pady=20)
    bday_spin=Spinbox(creatpin_frm,width=10,from_=1,to=31,textvariable=bdayspy)
    bday_spin.grid(row=5,column=0,sticky='e',padx=10)
    bmonth_spin=Spinbox(creatpin_frm,width=10,from_=1,to=12,textvariable=bmonthspy)
    bmonth_spin.grid(row=5,column=1,padx=10)
    byear_spin=Spinbox(creatpin_frm,width=10,from_=1951,to=2021,textvariable=yearspy)
    byear_spin.grid(row=5,column=2,sticky='w',padx=10)
    
    Button(creatpin_frm,text="Apply",width=10,font='Garamond 16 bold',command=applypin).grid(row=6,column=0,columnspan=3,pady=30)
    creatpin_frm.pack()
    
def applypin():
    if create_pin_ent.get() == "" :
        messagebox.showwarning("Agentask:","Pleas enter pin")
        create_pin_ent.focus_force()
    else :
        if create_cfpin_ent.get() == "" :
            messagebox.showwarning("Agentask:","Please confirm pin")
            create_cfpin_ent.focus_force()
        else :
            if create_pin_ent.get() == create_cfpin_ent.get() :
                birthday=str(bdayspy.get())+'-'+str(bmonthspy.get())+'-'+str(yearspy.get())
                sql="insert into pin (pin,birthday) values (?,?)"
                cursor.execute(sql,[create_cfpin_ent.get(),birthday])
                conn.commit()
                messagebox.showinfo("Agentask:","Create pin successfully")
            else :
                messagebox.showwarning("Agentask:","pin and confirm pin are not match")
                
def loginwindow(root) :
    global login_frm
    login_frm=Frame(root,bg='#a90432')
    login_frm.columnconfigure((0,1,2),weight=1)
    login_frm.rowconfigure((0,1,2),weight=1)
    
    Label(login_frm,bg='#a90432',image=logo).grid(row=0,column=0,columnspan=3,sticky='news',pady=(50,20))
    Entry(login_frm,width=20,textvariable=loginspy,justify='center').grid(row=1,column=0,columnspan=3,sticky='news',pady=20)
    Button(login_frm,bg='#a90432',fg='skyblue',text='Change pin',font='Garamond 15',borderwidth = 0,command=changepin).grid(row=2,column=0,sticky='e',pady=20)
    Button(login_frm,bg='#a90432',fg='skyblue',text='|',font='Garamond 15',borderwidth = 0).grid(row=2,column=1,sticky='news',pady=20)
    Button(login_frm,bg='#a90432',fg='skyblue',text='Forget pin',font='Garamond 15',borderwidth = 0,command=forgetpin).grid(row=2,column=2,sticky='w',pady=20)
    login_frm.pack()

def changepin() :
    global oldp_ent,newp_ent,cfnewp_ent,changepin_frm
    login_frm.destroy()
    root.title("Change Pin")
    changepin_frm=Frame(root,bg='#a90432')
    changepin_frm.pack()
    changepin_frm.columnconfigure(0,weight=1)
    changepin_frm.rowconfigure((0,8),weight=2)
    changepin_frm.rowconfigure((1,2,3,4,5,6,7),weight=1)
    
    Label(changepin_frm,text="Old Pin :",bg='#a90432',).grid(row=1,column=0,sticky='w',padx=10,pady=(50,10))
    oldp_ent=Entry(changepin_frm,width=20)
    oldp_ent.grid(row=2,column=0,columnspan=2,pady=10)
    Label(changepin_frm,text="New Pin :",bg='#a90432',).grid(row=3,column=0,sticky='w',padx=10,pady=10)
    newp_ent=Entry(changepin_frm,width=20,show='*')
    newp_ent.grid(row=4,column=0,columnspan=2,pady=10)
    Label(changepin_frm,text="Confirm Pin :",bg='#a90432',).grid(row=5,column=0,sticky='w',padx=10,pady=10)
    cfnewp_ent=Entry(changepin_frm,width=20,show='*')
    cfnewp_ent.grid(row=6,column=0,columnspan=2,pady=10)
    
    Button(changepin_frm,text="Apply",width=10,font='Garamond 16 bold').grid(row=7,column=0,sticky='e',pady=30)
    Button(changepin_frm,text="Cancel",width=10,font='Garamond 16 bold',command=backtologin_change).grid(row=7,column=0,sticky='w',pady=30)

def forgetpin() :
    global forget_frm
    login_frm.destroy()
    root.title("Forget Pin")
    forget_frm=Frame(root,bg='#a90432')
    forget_frm.pack()
    forget_frm.columnconfigure((0,1,2),weight=1)
    forget_frm.rowconfigure((0,1,2,3),weight=1)
    
    Label(forget_frm,text="Forget your pin?",bg='#a90432',).grid(row=0,column=0,columnspan=3,padx=10,pady=20)
    Label(forget_frm,text="Enter your birth day to recieve new password",font='Garamond 15',bg='#a90432',).grid(row=1,column=0,columnspan=3,padx=10,pady=20)
    bday_spin=Spinbox(forget_frm,width=10,from_=1,to=31,textvariable=bdayspy)
    bday_spin.grid(row=2,column=0,sticky='e',padx=10)
    bmonth_spin=Spinbox(forget_frm,width=10,from_=1,to=12,textvariable=bmonthspy)
    bmonth_spin.grid(row=2,column=1,padx=10)
    byear_spin=Spinbox(forget_frm,width=10,from_=1951,to=2021,textvariable=yearspy)
    byear_spin.grid(row=2,column=2,sticky='w',padx=10)
    
    Button(forget_frm,text="Apply",width=10,font='Garamond 16 bold',command=randompin).grid(row=3,column=0,columnspan=3,pady=30)

def randompin() :
    birthday=str(bdayspy.get())+'-'+str(bmonthspy.get())+'-'+str(yearspy.get())
    sql="select birthday from pin"
    cursor.execute(sql)
    result=cursor.fetchone()
    if result[0] == birthday :
        resultpin()
    else :
        messagebox.showwarning("Agentask :","birthday is not correct")
 
def resultpin() :
    global random_frm
    forget_frm.destroy()
    
    random_frm=Frame(root,bg='#a90432')
    random_frm.pack()
    random_frm.columnconfigure(0,weight=1)
    random_frm.rowconfigure(0,weight=2)
    random_frm.rowconfigure((1,2),weight=1)
    
    Label(random_frm,text="Here's your temporary pin!",bg='#a90432').grid(row=0,column=0,sticky='news',pady=30)
    random_pin= ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(6))
    Label(random_frm,text=random_pin,bg='#a90432',font='Garamond 30 bold').grid(row=1,column=0,sticky='news',pady=30)
    Button(random_frm,text="OK",width=10,font='Garamond 16 bold',command=backtologin_ran).grid(row=2,column=0,sticky='news',pady=30)
    
def backtologin_change() :
    changepin_frm.destroy()
    loginwindow(root)

def backtologin_ran() :
    bdayspy.set(1)
    bmonthspy.set(1)
    yearspy.set(2021)
    random_frm.destroy()
    loginwindow(root)

w=600
h=700
root=mainwindow()
createconnection()
#img
logo=PhotoImage(file='agentask.png').subsample(2,2)
#pinspy
bdayspy=IntVar()
bmonthspy=IntVar()
yearspy=IntVar()
yearspy.set(2021)
loginspy=StringVar()

sql_login="SELECT * FROM pin"
cursor.execute(sql_login)
result_login=cursor.fetchone()
if result_login :
    loginwindow(root)
else :
    first_time_use(root)

root.mainloop()
