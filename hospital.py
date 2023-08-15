from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
win = Tk()
win.state('zoomed')
win.config(bg='black')
#---------------------BUTTON FUNCTION----------------------------------------
def pd():
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        con = mysql.connector.connect(host="localhost",username="root",password="123456",database="mydata")    
        my_cursor = con.cursor()
        my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            nameoftablets.get(),
            ref.get(),
            dose.get(),
            nooftablets.get(),
            issuedate.get(),
            expdate.get(),
            dailydose.get(),
            sideeffect.get(), 
            nameofpatient.get(), 
            dob.get(),
            patientaddress.get()
        ))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo("success","Record has been inserted")
def fetch_data():
    con = mysql.connector.connect(host="localhost",username="root",password="123456",database="mydata")    
    my_cursor = con.cursor()
    my_cursor.execute('select * from hospital')
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        table.delete(* table.get_children())
        for items in rows:
            table.insert('',END,values=items)
        con.commit()
    con.close()
def get_data(event=''):
    cursor_row = table.focus()
    data = table.item(cursor_row)
    row = data['values']
    nameoftablets.set(row[0])
    ref.set(row[1])
    dose.set(row[2])
    nooftablets.set(row[3])
    issuedate.set(row[4])
    expdate.set(row[5])
    dailydose.set(row[6])
    sideeffect.set(row[7])
    nameofpatient.set(row[8])
    dob.set(row[9])
    patientaddress.set(row[10])  
#--------------------------------Prescription data-----------------------------------
def pre():
    txt_frme.insert(END,'Name of Tablets:\t\t\t'+nameoftablets.get()+'\n')        
    txt_frme.insert(END,'Reference No:\t\t\t'+ref.get()+'\n')               
    txt_frme.insert(END,'Dose:\t\t\t'+dose.get()+'\n')               
    txt_frme.insert(END,'No of Tablets:\t\t\t'+nooftablets.get()+'\n')               
    txt_frme.insert(END,'Issue date:\t\t\t'+issuedate.get()+'\n')               
    txt_frme.insert(END,'Exp date:\t\t\t'+expdate.get()+'\n')               
    txt_frme.insert(END,'Daily Dose:\t\t\t'+dailydose.get()+'\n')               
    txt_frme.insert(END,'Side Effect:\t\t\t'+sideeffect.get()+'\n')               
    txt_frme.insert(END,'Doctors Name:\t\t\t'+doctorsname.get()+'\n')               
    txt_frme.insert(END,'Specialization:\t\t\t'+specialization.get()+'\n')               
    txt_frme.insert(END,'Patient Age:\t\t\t'+patientage.get()+'\n')  
    txt_frme.insert(END,'Gender:\t\t\t'+gender.get()+'\n')   
    txt_frme.insert(END,'Name of Patient:\t\t\t'+nameofpatient.get()+'\n')  
    txt_frme.insert(END,'DOB:\t\t\t'+dob.get()+'\n')               
    txt_frme.insert(END,'Patient Address:\t\t\t'+patientaddress.get()+'\n')               
#--------------------------------DELETE BUTTON-----------------------------------------------------------
def delete():
    con = mysql.connector.connect(host="localhost",username="root",password="123456",database="mydata")    
    my_cursor = con.cursor()
    querry=('delete from hospital where Reference = %s')  
    value = (ref.get(),)  
    my_cursor.execute(querry,value)
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo('Deleted','Patient Data has been deleted')   
#------------------------------CLEAR BUTTON-------------------------------------------------------------
def clear():
    nameoftablets.set('')  
    ref.set('') 
    dose.set('') 
    nooftablets.set('') 
    issuedate.set('') 
    expdate.set('') 
    dailydose.set('') 
    sideeffect.set('') 
    doctorsname.set('') 
    specialization.set('') 
    patientage.set('') 
    gender.set('') 
    nameofpatient.set('') 
    dob.set('') 
    patientaddress.set('')  
    txt_frme.delete(1.0,END)           
#----------------------------------------EXIT--------------------------------------------------
def exit():
    confirm = messagebox.askyesno('confirmation','Are You Sure You Want To Exit')
    if confirm>0:
        win.destroy()
        return
    #heading
Label(win,text='Hospital Management System',font='impack 31 bold',bg='blue',fg='white').pack(fill=X)

#frame1

frame1 = Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1530,height=400)
#labelframe for patient info
lf1 = LabelFrame(frame1,text='Patient Information',font='ariel 10 bold',bd=10,bg='white')
lf1.place(x=10,y=0,width=950,height=360)
#label for patient information
Label(lf1,text='Name of Tablets',bg='white').place(x=10,y=10)
Label(lf1,text='Reference No',bg='white').place(x=10,y=50)
Label(lf1,text='Dose',bg='white').place(x=10,y=90)
Label(lf1,text='No of Tablets',bg='white').place(x=10,y=130)
Label(lf1,text='Issue Date',bg='white').place(x=10,y=170)
Label(lf1,text='Exp Date',bg='white').place(x=10,y=210)
Label(lf1,text='Daily Dose',bg='white').place(x=10,y=250)
Label(lf1,text='Side Effects',bg='white').place(x=10,y=290)
Label(lf1,text='Doctors Name',bg='white').place(x=500,y=10)
Label(lf1,text='Specialization',bg='white').place(x=500,y=50)
Label(lf1,text='Patient Age',bg='white').place(x=500,y=90)
Label(lf1,text='Gender',bg='white').place(x=500,y=130)
Label(lf1,text='Name of Patient',bg='white').place(x=500,y=170)
Label(lf1,text='DOB',bg='white').place(x=500,y=210)
Label(lf1,text='Patient Address',bg='white').place(x=500,y=250)
#TextVariabl  for Every Entry Field
nameoftablets = StringVar()
ref = StringVar()
dose = StringVar()
nooftablets = StringVar()
issuedate = StringVar()
expdate = StringVar()
dailydose = StringVar()
sideeffect = StringVar()
doctorsname = StringVar()
specialization = StringVar()
patientage = StringVar()
gender = StringVar()
nameofpatient = StringVar()
dob = StringVar()
patientaddress = StringVar()
#Entry Field for all Labels
e1 = Entry(lf1,bd=4,textvariable=nameoftablets)
e1.place(x=150,y=10,width=300)
e2 = Entry(lf1,bd=4,textvariable=ref)
e2.place(x=150,y=50,width=300)
e3 = Entry(lf1,bd=4,textvariable=dose)
e3.place(x=150,y=90,width=300)
e4 = Entry(lf1,bd=4,textvariable=nooftablets)
e4.place(x=150,y=130,width=300)
e5 = Entry(lf1,bd=4,textvariable=issuedate)
e5.place(x=150,y=170,width=300)
e6 = Entry(lf1,bd=4,textvariable=expdate)
e6.place(x=150,y=210,width=300)
e7 = Entry(lf1,bd=4,textvariable=dailydose)
e7.place(x=150,y=250,width=300)
e8 = Entry(lf1,bd=4,textvariable=sideeffect)
e8.place(x=150,y=290,width=300)
e9 = Entry(lf1,bd=4,textvariable=doctorsname)
e9.place(x=600,y=10,width=300)
e10 = Entry(lf1,bd=4,textvariable=specialization)
e10.place(x=600,y=50,width=300)
e11 = Entry(lf1,bd=4,textvariable=patientage)
e11.place(x=600,y=90,width=300)
e12 = Entry(lf1,bd=4,textvariable=gender)
e12.place(x=600,y=130,width=300)
e13 = Entry(lf1,bd=4,textvariable=nameofpatient)
e13.place(x=600,y=170,width=300)
e14 = Entry(lf1,bd=4,textvariable=dob)
e14.place(x=600,y=210,width=300)
e15 = Entry(lf1,bd=4,textvariable=patientaddress)
e15.place(x=600,y=250,width=300)
#labelframe for prescription
lf2 = LabelFrame(frame1,text='Prescription',font='ariel 12 bold',bd=10,bg='white')
lf2.place(x=970,y=0,width=520,height=360)
#Textbook for prescription
txt_frme = (Text(lf2,font='impack 10 bold',width=40,height=30,bg='white'))
txt_frme.pack(fill=BOTH)
#frame2
frame2 = Frame(win,bd=15,relief=RIDGE)
frame2.place(x=0,y=450,width=1530,height=300)
#buttons
d_btn = Button(win,text='Delete',font='ariel 15 bold',bg='purple',fg='white',bd=6,cursor='hand2',command=delete)
d_btn.place(x=0,y=750,width=400)
p_btn = Button(win,text='Prescription',font='ariel 15 bold',bg='orange',fg='white',bd=6,cursor='hand2',command=pre)
p_btn.place(x=300,y=750,width=500)
pd_btn = Button(win,text='Save Prescription Data',font='ariel 15 bold',bg='green',fg='white',bd=6,cursor='hand2',command=pd)
pd_btn.place(x=650,y=750,width=550)
c_btn = Button(win,text='Clear',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=clear)
c_btn.place(x=1180,y=750,width=230)
e_btn = Button(win,text='Exit',font='ariel 15 bold',bg='red',fg='white',bd=6,cursor='hand2',command=exit)
e_btn.place(x=1350,y=750,width=180)
#ScrollBar for Prescription Data
scroll_x = ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill='x')
scroll_y = ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill='y')

table = ttk.Treeview(frame2,columns=('not','ref','dose','nots','issd','expd','dd','sd','pn','dob','pa'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x=ttk.Scrollbar(command=table.xview)
scroll_y=ttk.Scrollbar(command=table.yview)
#Heading for prescription data
table.heading('not',text='Name of Tablets')
table.heading('ref',text='Reference No')
table.heading('dose',text='Dose')
table.heading('nots',text='No of Tablets')
table.heading('issd',text='Issue Date')
table.heading('expd',text='Exp Date')
table.heading('dd',text='Daily Dose')
table.heading('sd',text='Side Effects')
table.heading('pn',text='Patient Name')
table.heading('dob',text='DOB')
table.heading('pa',text='Patient Address')
table['show']='headings'
table.pack(fill=BOTH,expand=1)
table.column('not',width=100)
table.column('ref',width=100)
table.column('dose',width=100)
table.column('nots',width=100)
table.column('issd',width=100)
table.column('expd',width=100)
table.column('dd',width=100)
table.column('sd',width=100)
table.column('pn',width=100)
table.column('dob',width=100)
table.column('pa',width=100)
table.bind('<ButtonRelease-1>',get_data)
fetch_data()
mainloop()