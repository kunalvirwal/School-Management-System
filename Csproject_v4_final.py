import tkinter as TK
import tkinter.ttk
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#GUI setup
window =TK.Tk()
window.title("SMS")
window.configure(bg="#1F1F1F")
window.geometry("1100x800")

#functions-read name to understand the use
def remove(widget):
    widget.grid_forget()

def getname():
    global N,admin,students,teachers,name,password,passcode,state,incorrect,optn
    N=name.get()
    passcode=password.get()
    if N in students.keys() and passcode==students[N][0]:
        state="Student"
        optn=students[N][1]
        rvmintro()
    elif N in teachers.keys() and passcode==teachers[N][0]:
        state="Teacher"
        optn=teachers[N][1]
        rvmintro()
    elif N in admin.keys() and passcode==admin[N][0]:
        state="Admin"
        rvmintro()
    else:
        incorrect.grid(column=2,row=7)

def rvmintro():
    global intro,intro1,sub,name,password,incorrect,state
    remove(sub)
    remove(intro)
    remove(intro1)
    remove(name)
    remove(password)
    remove(incorrect)
    screen1decider(state)

def screen1decider(state):
    if state=="Student":
        Screen1student(N)
    elif state=="Teacher":    
        Screen1teacher(N)
    elif state=="Admin":
        Screen1admin(N)

def Start():
    remove(info1)
    remove(info2)
    remove(start)
    remove(info3)
    remove(ins)
    # Intro screen  
    intro.grid(column=2,row=1,padx=200,pady=70)
    intro1.grid(column=2,row=2)
    name.grid(column=2,row=3,pady=10)
    password.grid(column=2,row=5,pady=10)
    sub.grid(column=2,row=6,pady=15)

#print(students,"\n\n",teachers,"\n\n",admin)
#s=[['Kunal', 'XYZ', 'Student', 'C.S.'], ['Naman', 'WXY', 'Student', 'C.S.'],...
#...['Prashant', 'VWX', 'Teacher', 'Mathematics']]
#students={'Kunal': ['XYZ', 'C.S.', 'XI-A6'], 'Naman': ['WXY', 'C.S.', 'XI-A6']}
#teachers={'Prashant': ['UVW', 'Mathematics', ['XI-A4', 'XI-A6']]}
#subjects={'Prashant': 'Mathematics'}

def filework(cmd,name1,co,c,op=None,standards=None):
    global s,incorrect5
    incorrect5=TK.Label(window,text="No account found with this username!",font=("Arial Bold",30),bg="#1F1F1F",fg="Red")
    name1=name1.title()
    
    if cmd=="add" :
        t=str()
        if c!="Admin":#non admins
            if type(standards)==list:#teacher
                st=''
                for i in standards:
                    st+=(i+' ')
            else:#student
                st=standards
            t='\n'+name1+" "+co+" "+c+" "+op+" "+st
            #updating program records with new info
            dr=dict()
            dr[name1]=([co,op,standards])
            if c=="Student":
                s.append([name1,co,op,standards])
                students.update(dr)
            elif c=="Teachers":
                s.append([name1,co,op].extend(standards))
                teachers.update(dr)
        else:#admins
            t='\n'+name1+' '+co+' '+c
        #database addition
        with open("database.txt",'a') as f1:
            f1.write(t)

    elif cmd=="del":
        k=str()
        found=0
        with open("database.txt",'r') as f2:
            for line in f2:
                m=line.split()
                if m[0]!=name1:
                    k+=line
                else:
                    if m[2]!=c:
                        k+=line
                    else:
                        found+=1
        if found==0:
            incorrect5.grid(column=2,columnspan=5,row=9)
            
        with open("database.txt",'w') as f3:
            f3.write(k)
        
        
#1)screen for choosing account type   
def add_account_type():
    global state,acc,combotype,Apply2,back5,incorrect2
    incorrect2=TK.Label(window,text="Incorrect Account Type Entered!",font=("Arial Bold",30),bg="#1F1F1F",fg="Red")
    #heading
    top5=TK.Label(window,text="Add New Account",font=("Arial Bold",30),bg="#1F1F1F",fg="#0AA0EA")
    top5.grid(column=2,row=1,sticky="w",columnspan=2,padx=10,pady=10)
    #Type
    acc=TK.Label(window,text="Type:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
    acc.grid(column=2,row=2,sticky="e",padx=10,pady=10)
    #combo box type
    combotype=TK.ttk.Combobox(window)
    combotype['values']=("Student","Teacher","Admin")
    combotype.grid(column=3,row=2,sticky="w",padx=10,pady=10)
    #Apply
    Apply2=TK.Button(window,text="Apply",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[valid_account_type(combotype.get())])
    Apply2.grid(column=4,row=3)
    #back button
    back5=TK.Button(window,text="<=",font=("Arial",15),relief=TK.FLAT,command=lambda:[screen1decider(state),remove(incorrect2),remove(top5),remove(acc),remove(combotype),remove(back5),remove(Apply2)])
    back5.grid(column=1,row=1,padx=10,sticky='w')

#2)checks for valid account
def valid_account_type(c):
    global acc,combotype , Apply2,back5,incorrect2
    a=["Student","Teacher","Admin"]
    if c in a:
        remove(acc)
        remove(combotype)
        remove(Apply2)
        remove(back5)
        remove(incorrect2)
        add_account(c)
    else:
        incorrect2.grid(column=2,columnspan=3,row=8)

#3)all 3 screens for account addition
def add_account(c): #c is the type of account
    global nam, enteredname,password1,enteredcode,stuclass,combo2,combo21,combo22,combo23,sec,combo3,combo31,combo32,combo33,combo4,apply3,opt,incorrect3
    incorrect3=TK.Label(window,text="Incorrect details entered!",font=("Arial Bold",30),bg="#1F1F1F",fg="Red")
    
    #name entry will be common 
    nam=TK.Label(window,text="Name:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
    nam.grid(column=1,row=2,padx=10,pady=10)
    enteredname=TK.Entry(window,width=25)
    enteredname.grid(column=2,row=2,padx=10,pady=10)
    #password
    password1=TK.Label(window,text="Password:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
    password1.grid(column=1,row=3,padx=10,pady=10)
    enteredcode=TK.Entry(window,width=25)
    enteredcode.grid(column=2,row=3,padx=10,pady=10)
     
    if c=="Student":
        #Class
        stuclass=TK.Label(window,text="Class:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
        stuclass.grid(column=1,row=4,sticky="e",padx=10,pady=10)
        #combo box class
        combo2=TK.ttk.Combobox(window)
        combo2['values']=("I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII")
        combo2.grid(column=2,row=4,sticky="w",padx=10,pady=10)
        #SEC
        sec=TK.Label(window,text="Section:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
        sec.grid(column=1,row=5,sticky="e",padx=10,pady=10)
        #combo box sec
        combo3=TK.ttk.Combobox(window)
        combo3['values']=("A1","A2","A3","A4","A5","A6","B1","B2","D1","D2")
        combo3.grid(column=2,row=5,sticky="w",padx=10,pady=10)
        #opt
        opt=TK.Label(window,text="Opt. Subject",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
        opt.grid(column=1,row=6,sticky="e",padx=10,pady=10)
        #combo box subject
        combo4=TK.ttk.Combobox(window)
        combo4['values']=("C.S.","Geospatial","Music","Art","Dance")
        combo4.grid(column=2,row=6,sticky="w",padx=10,pady=10)
        #apply
        apply3=TK.Button(window,text="Add Account",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[valid_account_stu(enteredname.get(),combo2.get(),combo3.get(),combo4.get(),enteredcode.get(),c)])
        apply3.grid(column=3,row=7)
        #back
        back6=TK.Button(window,text="<=",font=("Arial",15),relief=TK.FLAT,command=lambda:[remove(nam),remove(enteredname),remove(password1),remove(enteredcode),remove(incorrect3),remove(stuclass),remove(combo2),remove(sec),remove(combo3),remove(combo4),remove(apply3),remove(opt),add_account_type()])
        back6.grid(column=1,row=1,padx=10,sticky='w')
    
    elif c=="Teacher":
        #class
        stuclass=TK.Label(window,text="Classes taught:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
        stuclass.grid(column=1,row=4,sticky="e",padx=10,pady=10)
        #SEC
        sec=TK.Label(window,text="Section:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
        sec.grid(column=2,row=4,padx=10,pady=10)
        #combo box class
        combo2=TK.ttk.Combobox(window)
        combo2['values']=("I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII")
        combo2.grid(column=1,row=5,padx=10,pady=10)
        #
        combo21=TK.ttk.Combobox(window)
        combo21['values']=("I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII")
        combo21.grid(column=1,row=6,padx=10,pady=10)
        #
        combo22=TK.ttk.Combobox(window)
        combo22['values']=("I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII")
        combo22.grid(column=1,row=7,padx=10,pady=10)
        #
        combo23=TK.ttk.Combobox(window)
        combo23['values']=("I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII")           
        combo23.grid(column=1,row=8,padx=10,pady=10)
        #combo box sec
        combo3=TK.ttk.Combobox(window)
        combo3['values']=("A1","A2","A3","A4","A5","A6","B1","B2","D1","D2")
        combo3.grid(column=2,row=5,padx=10,pady=10)
        #
        combo31=TK.ttk.Combobox(window)
        combo31['values']=("A1","A2","A3","A4","A5","A6","B1","B2","D1","D2")
        combo31.grid(column=2,row=6,padx=10,pady=10)
        #
        combo32=TK.ttk.Combobox(window)
        combo32['values']=("A1","A2","A3","A4","A5","A6","B1","B2","D1","D2")
        combo32.grid(column=2,row=7,padx=10,pady=10)
        #
        combo33=TK.ttk.Combobox(window)
        combo33['values']=("A1","A2","A3","A4","A5","A6","B1","B2","D1","D2")
        combo33.grid(column=2,row=8,padx=10,pady=10)
        #opt
        opt=TK.Label(window,text="Subject:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
        opt.grid(column=1,row=9,padx=10,pady=10)
        #subjects
        combo4=TK.ttk.Combobox(window)
        combo4['values']=("Mathematics","Physics","Chemistry","English","C.S.","Geospatial","Music","Art","Dance")
        combo4.grid(column=2,row=9,padx=10,pady=10)
        #apply
        apply3=TK.Button(window,text="Add Account",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[valid_account_teach(enteredname.get(),enteredcode.get(),combo2.get(),combo21.get(),combo22.get(),combo23.get(),combo3.get(),combo31.get(),combo32.get(),combo33.get(),combo4.get(),c)])
        apply3.grid(column=3,row=10)
        #back
        back6=TK.Button(window,text="<=",font=("Arial",15),relief=TK.FLAT,command=lambda:[remove(nam),remove(enteredname),remove(password1),remove(enteredcode),remove(incorrect3),remove(stuclass),remove(combo2),remove(combo21),remove(combo22),remove(combo23),remove(sec),remove(combo3),remove(combo31),remove(combo32),remove(combo33),remove(combo4),remove(apply3),remove(opt),add_account_type()])
        back6.grid(column=1,row=1,padx=10,sticky='w')

        
    else:
        apply3=TK.Button(window,text="Add Account",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[valid_account_adm(enteredname.get(),enteredcode.get(),c)])
        apply3.grid(column=3,row=10)
        
def valid_account_adm(namee,co,c):
    if enteredname.get()=='' or enteredcode.get()=='':
        incorrect3.grid(column=2,columnspan=3,row=11)
    else:
        remove(nam)
        remove(enteredname)
        remove(password1)
        remove(enteredcode)
        remove(incorrect3)
        remove(apply3)
        filework("add",namee,co,c)
        
def valid_account_teach(namee,co,cl1,cl2,cl3,cl4,se1,se2,se3,se4,op,c):
    global nam, enteredname,password1,enteredcode,stuclass,combo2,combo21,combo22,combo23,sec,combo3,combo31,combo32,combo33,combo4,apply3,opt,incorrect3
    if enteredname.get()=='' or enteredcode.get()=='' or combo2.get()=='' or combo3.get()=='' or combo4.get()=='':
        incorrect3.grid(column=2,columnspan=3,row=11)
    else:
        sections=["A1","A2","A3","A4","A5","A6","B1","B2","D1","D2"]
        classes=["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"]
        call=[cl1,cl2,cl3,cl4]
        sall=[se1,se2,se3,se4]
        clall=[]
        seall=[]
        for i in call:
            if i!='':
                clall.append(i)
        for j in sall:
            if j!='':
                seall.append(j)
        stn=['','','','']
        for i in range(len(clall)):
            if clall[i] not in classes or seall[i] not in sections:
                print(clall[i],'\n',seall[i])
                incorrect3.grid(column=2,columnspan=3,row=11)
                break
            else:
                stn[i]=str(clall[i]+'-'+seall[i])
        else:
            #remove every thing
            remove(nam)
            remove(enteredname)
            remove(password1)
            remove(enteredcode)
            remove(stuclass)
            remove(combo2)
            remove(combo21)
            remove(combo22)
            remove(combo23)
            remove(sec)
            remove(combo3)
            remove(combo31)
            remove(combo32)
            remove(combo33)
            remove(combo4)
            remove(apply3)
            remove(opt)
            remove(incorrect3)
            for i in stn:
                if i=='':
                    stn.remove(i)
            #filework(cmd,name,password,type,optional,class)
            filework("add",namee,co,c,op,stn)

#4)checks for walid details the enters
def valid_account_stu(namee,cc,se,op,co,c):  #cc is class se is section c is the type of account op is optional subject or subject taught
    global nam, enteredname,password1,enteredcode,stuclass,combo2,sec,combo3,combo4,apply3,opt,incorrect3
    sections=["A1","A2","A3","A4","A5","A6","B1","B2","D1","D2"]
    classes=["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"]
    
    if cc in classes and se in sections:
        remove(nam)
        remove(enteredname)
        remove(password1)
        remove(enteredcode)
        remove(stuclass)
        remove(combo2)
        remove(sec)
        remove(combo3)
        remove(combo4)
        remove(apply3)
        remove(opt)
        remove(incorrect3)
        standards=cc+'-'+se
        # filework(cmd,name,password,type,optional,class)
        filework("add",namee,co,c,op,standards)
    else:
        incorrect3.grid(column=2,columnspan=3,row=11)

def delete_account_type():
    global state,acc2,combotype2,Apply4,back7,incorrect4,nam1,enteredname1,top6
    incorrect4=TK.Label(window,text="Incorrect Account Type Entered!",font=("Arial Bold",30),bg="#1F1F1F",fg="Red")
    #heading
    top6=TK.Label(window,text="Delete Account",font=("Arial Bold",30),bg="#1F1F1F",fg="#0AA0EA")
    top6.grid(column=2,row=1,sticky="w",columnspan=2,padx=10,pady=10)
    #Type
    acc2=TK.Label(window,text="Type:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
    acc2.grid(column=3,row=2,sticky="e",padx=10,pady=20)
    #combo box type
    combotype2=TK.ttk.Combobox(window)
    combotype2['values']=("Student","Teacher","Admin")
    combotype2.grid(column=4,row=2,sticky="w",padx=10,pady=10)
    #name
    nam1=TK.Label(window,text="Name:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
    nam1.grid(column=1,row=2,padx=10,pady=10)
    enteredname1=TK.Entry(window,width=25)
    enteredname1.grid(column=2,row=2,padx=10,pady=10)
    #Apply
    Apply4=TK.Button(window,text="Apply",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[valid_account_del(enteredname1.get(),combotype2.get())])
    Apply4.grid(column=3,row=3,pady=20)
    #back button
    back7=TK.Button(window,text="<=",font=("Arial",15),relief=TK.FLAT,command=lambda:[screen1decider(state),remove(incorrect4),remove(top6),remove(acc2),remove(combotype2),remove(back7),remove(Apply4),remove(nam1),remove(enteredname1)])
    back7.grid(column=1,row=1,padx=10,sticky='w')
    pass#######################add name input in the same slide

def valid_account_del(namee,c):
    global state,acc2,combotype2,Apply4,incorrect4,nam1,enteredname1
    a=["Student","Teacher","Admin"]
    if namee!='' and c in a:
        remove(incorrect4)
        
        remove(acc2)
        remove(combotype2)
        
        remove(Apply4)
        remove(nam1)
        remove(enteredname1)
        filework("del",namee,None,c)
    else:
        incorrect4.grid(column=2,columnspan=3,row=11)
        
def Screen1admin(N):
    #Heading label
    t="Welcome "+N.title()+"! [Admin access]"
    top=TK.Label(window,text=t,font=("Arial Bold",30),bg="#1F1F1F",fg="#0AA0EA")
    top.grid(column=1,row=1,columnspan=4,sticky="w")
    #Add an account
    b1=TK.Button(window,text="Add Account",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[remove(top),remove(b2),remove(b1),remove(creds),add_account_type()])
    b1.grid(column=2,row=2,pady=10,padx=20)
    #remove an account
    b2=TK.Button(window,text="Delete Account",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[remove(top),remove(b1),remove(b2),remove(creds),delete_account_type()])
    b2.grid(column=4,row=2,pady=10,padx=20)
    #credits
    creds=TK.Button(window,text="    Credits    ",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[acknow(),remove(b2),remove(top),remove(b1),remove(creds)])
    creds.grid(column=2,row=3,pady=20,padx=20)

def Screen1student(N):
    global optn
    #Heading label
    t="Welcome "+N.title()+"!"
    top=TK.Label(window,text=t,font=("Arial Bold",30),bg="#1F1F1F",fg="#0AA0EA")
    top.grid(column=1,row=1,sticky="w")
    #Textbox
    T=TK.Text(window,height=7,font=("Arial",14),bg="#1F1F1F",fg="White",relief=TK.FLAT)
    T.grid(column=1,row=3,padx=20,pady=40)
    T.insert(TK.END,"Name : "+N.title()+"\n\n")
    T.insert(TK.END,"Class studing in : XI-A6\n\n")
    T.insert(TK.END,"Scholarship awarded : Not alloted yet\n\n")
    T.insert(TK.END,"Optional Subject : "+optn)
    #Leave button
    b2=TK.Button(window,text="Apply Leave",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[leave(),remove(b2),remove(T),remove(top),remove(fee),remove(performance),remove(creds)])
    b2.grid(column=1,row=5,sticky="w",pady=20,padx=40)
    #fee structure
    fee=TK.Button(window,text="Fee structure",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[Fee(),remove(b2),remove(T),remove(top),remove(fee),remove(performance),remove(creds)])
    fee.grid(column=1,row=5,sticky="e",pady=20,padx=280)
    #performance
    performance=TK.Button(window,text="Performance",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[stats(),remove(b2),remove(T),remove(top),remove(fee),remove(performance),remove(creds)])
    performance.grid(column=1,row=6,sticky="w",padx=40)
    #credits
    creds=TK.Button(window,text="    Credits    ",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[acknow(),remove(b2),remove(T),remove(top),remove(fee),remove(performance),remove(creds)])
    creds.grid(column=1,row=6,sticky="e",pady=20,padx=280)
    
def leave():
    global combo,combo2,enteredreason,top2,date,month,reason,enteredreason,T1,back1,apply,wrong
    top2=TK.Label(window,text="Apply Leave",font=("Arial Bold",30),bg="#1F1F1F",fg="#0AA0EA")
    top2.grid(column=2,row=1,sticky="e",padx=10)
    #date
    date=TK.Label(window,text="Date:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
    date.grid(column=1,row=2,sticky="ne",padx=10,pady=20)
    combo=TK.ttk.Combobox(window)
    combo['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
    combo.grid(column=2,row=2,sticky="w",padx=10,pady=20)
    #month
    month=TK.Label(window,text="Month:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
    month.grid(column=1,row=3,sticky="e",padx=10,pady=20)
    combo2=TK.ttk.Combobox(window)
    combo2['values']=tuple(months)
    combo2.grid(column=2,row=3,sticky="w",padx=10,pady=20)
    #reason
    reason=TK.Label(window,text="Reason:",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
    reason.grid(column=1,row=4,sticky="e",padx=10,pady=20)
    enteredreason=TK.Entry(window,width=30)
    enteredreason.grid(column=2,row=4,sticky="w",padx=10,pady=20)
    #NOTE
    T1=TK.Label(window,text="Note: Leaves are not granted in the last week of any month.\nIf a leave is required then a written letter must be submitted in school 3 days prior. ",font=("Arial Bold",15),justify=TK.LEFT,bg="#1F1F1F",fg="White")
    T1.grid(column=1,row=6,sticky="sw",columnspan=5)
    #Back button
    back1=TK.Button(window,text="<=",font=("Arial",15),relief=TK.FLAT,command=lambda:[screen1decider(state),remove(top2),remove(wrong),remove(date),remove(combo),remove(month),remove(combo2),remove(reason),remove(enteredreason),remove(T1),remove(apply),remove(back1)])
    back1.grid(column=1,row=1,padx=10,sticky='w')
    #APPLY button
    wrong=TK.Label(window,text="Invalid date or month entered",font=("Arial Bold",30),justify=TK.CENTER,bg="#1F1F1F",fg="Red")
    apply=TK.Button(window,text="Apply Leave",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=valid_leave)
    apply.grid(column=3,row=8)

def valid_leave():
    if (combo.get()).isdigit() and (int(combo.get())<=31) and (int(combo.get())>=1) and (combo2.get())in months and (enteredreason.get())!='' :    
        top2.configure(text="Leave applied")
        remove(date)
        remove(combo)
        remove(month)
        remove(combo2)
        remove(reason)
        remove(enteredreason)
        remove(T1)
        remove(apply)
        remove(wrong)
        
    else:
        wrong.grid(column=1,columnspan=5,row=9)
        
def Fee():
    #Heading
    top3=TK.Label(window,text="Fee structure 2021",font=("Arial Bold",30),bg="#1F1F1F",fg="#0AA0EA")
    top3.grid(column=2,row=1,padx=10)
    #Textbox for fees
    T2=TK.Text(window,height=20,font=("Arial",15),bg="#1F1F1F",fg="White",relief=TK.FLAT)
    T2.grid(column=2,row=3,padx=20)
    T2.insert(TK.END,"  Months                     Tuition fees      Status\n\n")
    T2.insert(TK.END,"April-June :                  40000Rs/-        Paid\n")
    T2.insert(TK.END,"July-September :          40000Rs/-        Paid\n")
    T2.insert(TK.END,"October-December :    40000Rs/-        Paid\n")
    T2.insert(TK.END,"January-March :           40000Rs/-        Due\n")
    T2.insert(TK.END,"___________________________\n")
    T2.insert(TK.END,"Net payable :                40000Rs/-\n\n")
    T2.insert(TK.END,"Note:This amount can be paid through offline check deposite or through UPI after\nwhich the class teacher must be informed.")
    #Back button
    back2=TK.Button(window,text="<=",font=("Arial",15),relief=TK.FLAT,command=lambda:[screen1decider(state),remove(top3),remove(T2),remove(back2)])
    back2.grid(column=1,row=1,padx=10,sticky='w')

def stats():
    #Heading
    top4=TK.Label(window,text="Marks Analysis",font=("Arial Bold",30),bg="#1F1F1F",fg="#0AA0EA")
    top4.grid(column=1,columnspan=2,row=1)
    #Textbox
    T3=TK.Text(window,height=7,font=("Arial",15),bg="#1F1F1F",relief=TK.FLAT,fg="White")
    T3.grid(column=2,row=3,sticky="w",padx=20)
    T3.insert(TK.END,"  Subjects       Marks\n\n")
    T3.insert(TK.END,"  Comp.Sci.        \t"+str(marks[0])+"\t\t|\t\t Percentage aquired: "+str(round((percentage*100),2))+"%\n")
    T3.insert(TK.END,"  Chemistry         \t"+str(marks[1])+"\t\t|\t\t Average Marks: "+str(round(avg,2))+"\n")
    T3.insert(TK.END,"  Mathematics     \t"+str(marks[2])+"\t\t|\n")
    T3.insert(TK.END,"  English             \t"+str(marks[3])+"\t\t|\n")
    T3.insert(TK.END,"  Physics            \t"+str(marks[4])+"\t\t|\n")
    #Graph
    canvas.get_tk_widget().grid(column=1,columnspan=2,padx=25,pady=10,sticky="w",row=6)
    #Back
    back3=TK.Button(window,text="<=",font=("Arial",15),relief=TK.FLAT,command=lambda:[screen1decider(state),remove(top4),remove(T3),remove(back3),remove(canvas.get_tk_widget())])
    back3.grid(column=1,row=1,padx=10,sticky='w')

def acknow():
    #Heading
    top5=TK.Label(window,text="Credits",font=("Arial Bold",30),bg="#1F1F1F",fg="#0AA0EA")
    top5.grid(column=1,columnspan=2,row=1)
    #matter
    t="This project based on school management system was developed by combined efforts of:"
    matt=TK.Label(window,text=t,font=("Arial Bold",15),bg="#1F1F1F",fg="White")
    matt.grid(column=1,row=2,padx=20,pady=40)
    na1=TK.Label(window,text=">Kunal",font=("Arial",40),bg="#1F1F1F",fg="#0AA0EA")
    na1.grid(column=1,row=3,sticky='w',columnspan=3)
    #exit button
    exi=TK.Button(window,text="  Exit  ",font=("Arial",20),bg="#0AA0EA",fg="White",relief=TK.FLAT,command=lambda:[window.destroy()])
    exi.grid(column=1,row=5,pady=20)
    #Back button
    back4=TK.Button(window,text="<=",font=("Arial",15),relief=TK.FLAT,command=lambda:[screen1decider(state),remove(exi),remove(top5),remove(matt),remove(na1),remove(back4)])
    back4.grid(column=1,row=1,padx=10,sticky='w')

def Screen1teacher(N):
    #Heading label
    t="Welcome "+N.title()+"!"
    top=TK.Label(window,text=t,font=("Arial Bold",30),bg="#1F1F1F",fg="#0AA0EA")
    top.grid(column=1,row=1,sticky="w")
    #Textbox
    T=TK.Text(window,height=7,font=("Arial",14),bg="#1F1F1F",fg="White",relief=TK.FLAT)
    T.grid(column=1,row=3,padx=20)
    T.insert(TK.END,"Name : "+N.title()+"\n\n")
    T.insert(TK.END,"Subject :"+subjects[N]+"\n\n")
    work=' '
    for i in teachers[N][2]:
        work+=(i+" ")
    T.insert(TK.END,"Classes Taught :"+work+"\n\n")
    #Leave button
    b2=TK.Button(window,text="Apply Leave",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[leave(),remove(b2),remove(T),remove(top),remove(creds)])
    b2.grid(column=1,row=5,sticky="w",pady=10,padx=40)
    #credits button
    creds=TK.Button(window,text="    Credits    ",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=lambda:[acknow(),remove(b2),remove(T),remove(top),remove(creds)])
    creds.grid(column=1,row=6,sticky="e",pady=20,padx=280)

    
#program variables
N=""
students={}
teachers={}
admin={}
subjects={}
classes={}
months=["January","February","March","April","June","July","August","September","October","November","December"]
passcode=""
marks=[]
subs=["Comp. Sci. ","Chemistry","Mathematics","English","Physics"]

#-->file system
#this block gets data from file and seperates each line and word
with open("database.txt",'r') as f:
    s=f.read()
s=s.split('\n')
for i in range(len(s)):
    s[i]=s[i].split()
print(s)
    
#distributes the databse into 3 lists
for i in s:
    
    if i[2]=="Student":
        i.remove("Student")
        students[i[0]]=i[1:]
    elif i[2]=="Teacher":
        i.remove("Teacher")
        teachers[i[0]]=i[1:]
    else:
        i.remove("Admin")
        admin[i[0]]=i[1:]

#subjects is a dictionary which has teacher's name as key and subject taught as value
for i in teachers.keys():
    subjects[i]=teachers[i][1]

#sections taught:this block compiles the classes taught from elements into a list 
for j in teachers.keys():
    l=teachers[j][2:]            # list of classes taught
    k=teachers[j][:2]               # [name,password,subject]
    k.append(l)
    teachers[j]=k

#graphs setup
for i in range(5):
    d=random.randint(25,45)
    marks.append(d)
percentage=sum(marks)/(len(marks)*45)
avg=sum(marks)/len(marks)
fig=Figure(figsize=(10.5,3.80),dpi=100) #object of figure class
plot1=fig.add_subplot(1,2,1)  #(rows,columns,position)
plot2=fig.add_subplot(1,2,2)
plot1.set_ylabel("Marks obtained")
plot2.set_ylabel("Marks obtained")
plot1.set_xlabel("Subjects")
plot2.set_xlabel("Subjects")
rects1=plot1.bar(subs,marks,0.5,color="#0AA0EA")
line1=plot2.plot(subs,marks,marker='o',color="#0AA0EA")
canvas=FigureCanvasTkAgg(fig, master=window)

# Info screen
ins=TK.Label(window,text="Instructions",font=("Arial Bold",30),bg="#1F1F1F",fg="White")
ins.grid(column=1,columnspan=2,row=1)
info1=TK.Label(window,text="1)Welcome to SMS.This program has been devloped by students of class XI-A6.",font=("Arial Bold",20),bg="#1F1F1F",fg="White")
info1.grid(column=1,row=2,sticky="w",pady=30)
info2=TK.Label(window,text="2)To open the program as a student account use the names of group 5.\nTo access as a teacher account use any of the names of subject teachers of 11-A6",justify=TK.LEFT,font=("Arial Bold",20),bg="#1F1F1F",fg="White")
info2.grid(column=1,row=4,sticky="w",pady=30)
info3=TK.Label(window,text="3)To log in enter your first name with first letter in uppercase and in second blank\nenter your valid password",justify=TK.LEFT,font=("Arial Bold",20),bg="#1F1F1F",fg="White")
info3.grid(column=1,row=6,sticky="w",pady=30)
start=TK.Button(window,text="OK",font=("Arial",15),relief=TK.FLAT,bg="#0AA0EA",fg="White",command=Start)
start.grid(column=1,row=8,sticky="e")

#Intro screen
intro=TK.Label(window,text="Welcome to SMS",font=("Arial Bold",60),bg="#1F1F1F",fg="White")
intro1=TK.Label(window,text="Devloped by XI A6",font=("Arial Bold",30),bg="#1F1F1F",fg="White")
name=TK.Entry(window,width=30)
name.insert(0,"Tony")##############
sub=TK.Button(window,text=" Submit ",font=("Arial",15),bg="#0AA0EA",fg="White",relief=TK.FLAT,command=getname)
password=TK.Entry(window,show='*',width=30)
password.insert(0,"T")##############
incorrect=TK.Label(window,text="Incorrect user ID or password",font=("Arial Bold",30),bg="#1F1F1F",fg="Red")

#print(students,"\n\n",teachers,"\n\n",admin)
#s=[['Kunal', 'XYZ', 'Student', 'C.S.'], ['Naman', 'WXY', 'Student', 'C.S.'],...
#...['Prashant', 'VWX', 'Teacher', 'Mathematics']]
#students={'Kunal': ['XYZ', 'C.S.', 'XI-A6'], 'Naman': ['WXY', 'C.S.', 'XI-A6']}
#teachers={'Prashant': ['UVW', 'Mathematics', ['XI-A4', 'XI-A6']]}
#subjects={'Prashant': 'Mathematics'}

"""
Kunal K Student C.S. XI-A6
Prashant P Teacher Mathematics XI-A4 XI-A6
Tony T Admin
"""
#format of add student
window.mainloop()
