from tkinter import*
from tkinter import messagebox

def mainwindow() :
    root=Tk()
    root.geometry('%dx%d'%(w,h))
    root.config(bg='orange')
    root.title("Change Pin")
    root.option_add('*font','Garamond 20 bold')
    return root

def changepin(root) :
    root.title("Change Pin")
    changepin_frm=Frame(root,bg='orange')
    changepin_frm.pack()
    changepin_frm.columnconfigure((0,1),weight=1)
    changepin_frm.rowconfigure((0,8),weight=2)
    changepin_frm.rowconfigure((1,2,3,4,5,6,7),weight=1)
    
    Label(changepin_frm,text="Old Pin :",bg='orange',).grid(row=1,column=0,sticky='w',padx=10,pady=10)
    oldp_ent=Entry(changepin_frm,width=20)
    oldp_ent.grid(row=2,column=0,columnspan=2,pady=10)
    Label(changepin_frm,text="New Pin :",bg='orange',).grid(row=3,column=0,sticky='w',padx=10,pady=10)
    newp_ent=Entry(changepin_frm,width=20,show='*')
    newp_ent.grid(row=4,column=0,columnspan=2,pady=10)
    Label(changepin_frm,text="Confirm the Pin :",bg='orange',).grid(row=5,column=0,sticky='w',padx=10,pady=10)
    cfnewp_ent=Entry(changepin_frm,width=20,show='*')
    cfnewp_ent.grid(row=6,column=0,columnspan=2,pady=10)
    
    Button(changepin_frm,text="Apply",width=10,font='Garamond 16 bold').grid(row=7,column=0,columnspan=2,pady=10)
    
def forgetpin(root) :
    root.title("Forget Pin")
    changepin_frm=Frame(root,bg='orange')
    changepin_frm.pack()
    changepin_frm.columnconfigure((0,1),weight=1)
    changepin_frm.rowconfigure((0,8),weight=2)
    changepin_frm.rowconfigure((1,2,3,4,5,6,7),weight=1)
    
    Label(changepin_frm,text="Old Pin :",bg='orange',).grid(row=1,column=0,sticky='w',padx=10,pady=10)
    oldp_ent=Entry(changepin_frm,width=20)
    oldp_ent.grid(row=2,column=0,columnspan=2,pady=10)
    Label(changepin_frm,text="New Pin :",bg='orange',).grid(row=3,column=0,sticky='w',padx=10,pady=10)
    newp_ent=Entry(changepin_frm,width=20,show='*')
    newp_ent.grid(row=4,column=0,columnspan=2,pady=10)
    Label(changepin_frm,text="Confirm the Pin :",bg='orange',).grid(row=5,column=0,sticky='w',padx=10,pady=10)
    cfnewp_ent=Entry(changepin_frm,width=20,show='*')
    cfnewp_ent.grid(row=6,column=0,columnspan=2,pady=10)
    
    Button(changepin_frm,text="Apply",width=10,font='Garamond 16 bold').grid(row=7,column=0,columnspan=2,pady=10)
        
w=600
h=800
root=mainwindow()
changepin(root)

root.mainloop()