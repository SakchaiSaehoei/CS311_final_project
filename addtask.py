from tkinter import*
from tkinter import messagebox
import sqlite3
import datetime

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
    
def import_time() :
    global now_day,now_month,now_year,now_hour,now_min
    now = datetime.datetime.now()
    now_day=now.strftime("%d")
    now_month=now.strftime("%m")
    now_year=now.strftime("%Y")
    now_hour=now.strftime("%H")
    now_min=now.strftime("%M")
    #now.strftime("%Y-%m-%d %H:%M:%S")

def addtaskwindow(root):
    global addtask_frm,inputName,taskday,taskmonth,time_h,time_m
    global radioButtonFrame
    root.config(bg='#ff9933')
    root.rowconfigure((0,1),weight=1)
    root.columnconfigure(0,weight=1)
    
    addtask_frm=Frame(root,bg='#ff9933')
    addtask_frm.columnconfigure((0,1),weight=1)
    addtask_frm.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)

    Label(addtask_frm, text='Add Task', font='None 20', bg='#ff9933').grid(row=0, columnspan=2, sticky='news', pady=(10,0))
    Label(addtask_frm, text='Name', font='None 18', anchor=W, bg='#ff9933').grid(row=1, columnspan=2, sticky=W, padx=80)
    
    inputName = Entry(addtask_frm,textvariable=add_name)
    inputName.grid(row=2, columnspan=2, sticky='news', padx=80)

    Label(addtask_frm, text='Day / Month', font='None 16', bg='#ff9933').grid(row=3, columnspan=2, sticky=W + E)
    
    taskday = Spinbox(addtask_frm, from_=0, to=31, width=10,textvariable=add_day)
    taskday.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    taskmonth = Spinbox(addtask_frm, from_=0, to=12, width=10,textvariable=add_month)
    taskmonth.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    Label(addtask_frm, text='Time', font='None 16', bg='#ff9933').grid(row=5, columnspan=2, sticky='news')

    time_h = Spinbox(addtask_frm, from_=1, to=24, width=10,textvariable=add_hour) 
    time_h.grid(row=6, column=0, padx=5, pady=5, sticky=E)

    time_m = Spinbox(addtask_frm, from_=0, to=59, width=10,textvariable=add_min)
    time_m.grid(row=6, column=1, padx=5, sticky=W)

    Label(addtask_frm, text='Color swatch', font='None 15', anchor=W, bg='#ff9933').grid(row=7, column=0, sticky=W, padx=10)
    Label(addtask_frm, text=
          '''
          User can choose to use color. The selected color represents
          the amount of time User spends each job. As follows
          
          Red : It takes approximately more than 3 days.\nyellow : 24 hours or less\nGreen : 1-5 hours
          '''
          , font='None 14', bg='#ff9933', anchor=W).grid(row=8, padx=(10, 0), columnspan=2, sticky=W)
    
    addtask_frm.grid(row=0,column=0, sticky='news')
    
    radioButtonFrame = Frame(root, bg='#ff9933')
    radioButtonFrame.columnconfigure((0,1,2,3),weight=1)
    radioButtonFrame.rowconfigure((0,1,2,3,4),weight=1)

    radio = StringVar(None, 1)
    
    Frame(radioButtonFrame, width=100, height=70, bg='red').grid(row=0,rowspan=4, column=0, padx=5, pady=5)
    Frame(radioButtonFrame, width=100, height=70, bg='yellow').grid(row=0,rowspan=4, column=1, padx=5, pady=5)
    Frame(radioButtonFrame, width=100, height=70, bg='green').grid(row=0,rowspan=4, column=2, padx=5, pady=5)

    radioButtonRed = Radiobutton(master=radioButtonFrame, text='Red',font='None 15', variable=add_color, value=1, bg='#ff9933')
    radioButtonRed.grid(row=0, column=3, sticky=W)

    radioButtonOrange = Radiobutton(master=radioButtonFrame, text='Orange',font='None 15', variable=add_color, value=2, bg='#ff9933')
    radioButtonOrange.grid(row=1, column=3, sticky=W)

    radioButtonGreen = Radiobutton(master=radioButtonFrame, text='Green',font='None 15', variable=add_color, value=3, bg='#ff9933')
    radioButtonGreen.grid(row=2, column=3, sticky=W)

    radioButtonGreen = Radiobutton(master=radioButtonFrame, text='not add color',font='None 15', variable=add_color, value=4, bg='#ff9933')
    radioButtonGreen.grid(row=3, column=3, sticky=W)

    submitButton = Button(master=radioButtonFrame, text='Submit',command=addtask_click)
    submitButton.grid(row=4, column=0,columnspan=4, pady=5)

    radioButtonFrame.grid(row=1, column=0,sticky='news')
    
def addtask_click() :
    if inputName.get() == "" :
        messagebox.showwarning("Agentask:","Please enter task's name")
        inputName.focus_force()
    else :
        if add_color.get() == 0 :
            messagebox.showwarning("Agentask:","Please choose color")
        else :
            due_date=add_day.get()+'-'+add_month.get()+'-'+now_year
            if add_min.get() == '0' :
                due_time=str(add_hour.get())+':'+'00'
            else :
                due_time=str(add_hour.get())+':'+str(add_min.get())
            sql="insert into homework(name,date,time,color) values (?,?,?,?)"
            cursor.execute(sql,[inputName.get(),due_date,due_time,add_color.get()])
            conn.commit()
            messagebox.showwarning("Agentask:","Add task successfully")
            #addtask_frm.destroy()
            #radioButtonFrame.destroy()
'''
def trydb():
    sql="select date from homework"
    cursor.execute(sql)
    result=cursor.fetchall()
    #print(result)
    now = datetime.datetime.now()
    date=now.strftime("%d")
    print(date)
    for i,data in enumerate(result) :
        due=data[0].split("-")
        #print(due[0]) #0=day 1=month 2=year
        if due[0] > date or due[0] == date :
            print('no')
        if due[0] < date :
            print('yes')
'''

w=600
h=700
root=mainwindow()
createconnection()
import_time()
#img
#addtaskspy
add_name=StringVar()
add_day=StringVar()
add_month=StringVar()
add_hour=StringVar()
add_min=StringVar()
add_color=IntVar()


addtaskwindow(root)
root.mainloop()