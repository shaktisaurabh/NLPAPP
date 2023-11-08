from tkinter import * 
from tkinter import messagebox
from newdatabase import databses 
from nlpapi import ohmyapi

class nlps:
    def __init__(self):
        self.root=Tk()
        self.db=databses()
        self.ms=ohmyapi() 
        self.root.geometry('340x640')
        self.root.title('Kya ajeeb app hai ye')
        self.root.configure(bg="#010313")
        self.login_gui()
        

        self.root.mainloop()

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy() 

    def login_gui(self):
        self.clear()

        lbl1=Label(self.root,text="NLPAPP",bg="#010313",fg="white")
        lbl1.pack(pady=(30,30))
        lbl1.configure(font=('verdana',24,'bold'))

        lbl2=Label(self.root,text="Enter email")
        lbl2.pack(pady=(10,10)) 

        self.email_ent1=Entry(self.root,width=50)
        self.email_ent1.pack(pady=(10,10),ipady=5) 

        lbl3=Label(self.root,text="Enter Password")
        lbl3.pack(pady=(10,10)) 

        self.password_ent1=Entry(self.root,width=50,show="*")
        self.password_ent1.pack(pady=(10,10),ipady=5) 

        btn1=Button(self.root,text="Login",width=10,height=2,command=self.checker)
        btn1.pack(pady=(10,10)) 

        lbl4=Label(self.root,text="Not a member?",bg="#010313",fg="white") 
        lbl4.pack(pady=(10,10)) 
        lbl4.configure(font=('verdana',10)) 

        btn2=Button(self.root,text="Register Now",width=10,height=2,command=self.reg_gui)
        btn2.pack(pady=(10,10)) 
    
    def reg_gui(self):
        self.clear()

        lbl1=Label(self.root,text="NLPAPP",bg="#010313",fg="white") 
        lbl1.pack(pady=(30,30))
        lbl1.configure(font=('verdana',24,'bold')) 

        lbl2=Label(self.root,text="Enter Name")
        lbl2.pack(pady=(10,10)) 

        self.name_ent=Entry(self.root,width=50)
        self.name_ent.pack(pady=(10,10),ipady=5)

        lbl3=Label(self.root,text="Enter Email")
        lbl3.pack(pady=(10,10)) 

        self.email_ent2=Entry(self.root,width=50)
        self.email_ent2.pack(pady=(10,10),ipady=5) 

        lbl4=Label(self.root,text="Enter Password")
        lbl4.pack(pady=(10,10)) 

        self.pass_ent2=Entry(self.root,width=50)
        self.pass_ent2.pack(pady=(10,10),ipady=5)

        btn1=Button(self.root,text="Register",width=10,height=2,command=self.adding)
        btn1.pack(pady=(10,10))

        lbl5=Label(self.root,text="Already a member?",bg="#010313",fg="white")
        lbl5.pack(pady=(10,10))
        lbl5.configure(font=('verdana',10))  

        btn2=Button(self.root,text="Login Now",width=10,height=2,command=self.login_gui)
        btn2.pack(pady=(10,10)) 
    
    def adding(self):
        name=self.name_ent.get()
        email=self.email_ent2.get()
        password=self.pass_ent2.get()
        c1=self.db.add_new(email,name,password)
        if c1:
            messagebox.showinfo('Success','Registered sucessfully')
        else:
            messagebox.showerror('Error','Member already exists')
    
    def checker(self):
        email=self.email_ent1.get()
        password=self.password_ent1.get()
        c1=self.db.check(email,password)
        if c1:
            messagebox.showinfo('Sucess','Login is sucessfull')
            self.appgui()
        else:
            messagebox.showerror('Error','Wrong credentials')  
    
    def appgui(self):
        self.clear()

        lbl1=Label(self.root,text="NLPAPP",bg="#010313",fg="white")
        lbl1.pack(pady=(30,30)) 
        lbl1.configure(font=('verdana',24,'bold'))

        btn1=Button(self.root,text="Sentiment Analysis",width=50,height=2,command=self.senti)
        btn1.pack(pady=(10,10)) 

        btn2=Button(self.root,text="NER",width=50,height=2,command=self.neri)
        btn2.pack(pady=(10,10))

        btn3=Button(self.root,text="Abuse Check",width=50,height=2,command=self.abusal) 
        btn3.pack(pady=(10,10))

        redirect_btn=Button(self.root,text="Logout",width=50,height=2,command=self.login_gui) 
        redirect_btn.pack(pady=(10,10))

    def senti(self):
        self.clear()

        lbl1=Label(self.root,text="NLPAPP",bg="#010313",fg="white")
        lbl1.pack(pady=(30,30))
        lbl1.configure(font=('verdana',24,'bold'))

        lbl2=Label(self.root,text="Sentiment Analysis",bg='#010313',fg="white") 
        lbl2.pack(pady=(30,30))
        lbl2.configure(font=('verdana',16))

        lbl3=Label(self.root,text="Enter Text")
        lbl3.pack(pady=(10,10))

        self.ghani=Entry(self.root,width=50)
        self.ghani.pack(pady=(10,10),ipady=5)

        an_btn=Button(self.root,text="Analyze Button",width=50,height=2,command=self.senti1)
        an_btn.pack(pady=(10,10))

        self.whatabout=Label(self.root,text='',bg='#010313',fg='white')
        self.whatabout.pack(pady=(20,20))
        self.whatabout.configure(font=('verdana',20))

        go_btn=Button(self.root,text="Go Back",width=50,height=2,command=self.appgui)
        go_btn.pack(pady=(10,10))

    def senti1(self):
        text=self.ghani.get()
        c1=self.ms.get_senti(text)
        txt=''
        for i in c1['sentiment']:
            txt=txt+i+'---->'+str(c1['sentiment'][i])+'\n' 
        self.whatabout['text']=txt 

    def neri(self):
        self.clear()

        lbl1=Label(self.root,text="NLPAPP",bg="#010313",fg="white")
        lbl1.pack(pady=(30,30)) 
        lbl1.configure(font=('verdana',24,'bold')) 

        lbl2=Label(self.root,text="NER",bg="#010313",fg="white") 
        lbl2.pack(pady=(10,10))
        lbl2.configure(font=('verdana',16))

        lbl3=Label(self.root,text="Enter the text") 
        lbl3.pack(pady=(10,10)) 

        self.ent3=Entry(self.root,width=50) 
        self.ent3.pack(pady=(10,10),ipady=5) 

        analyze_btn=Button(self.root,text="Analyze",width=10,height=2,command=self.neri1)
        analyze_btn.pack(pady=(10,10)) 

        self.funny=Label(self.root,text="",bg="#010313",fg="white")
        self.funny.pack(pady=(10,10))
        self.funny.configure(font=('verdana',16))

        go_back_btn=Button(self.root,text="Go Back",width=10,height=2,command=self.appgui)
        go_back_btn.pack(pady=(10,10)) 

    def neri1(self):
        c1=self.ent3.get()
        c2=self.ms.get_neri(c1)
        txt=""
        for i in c2['entities']:
            txt=txt+str(i)+'\n'
        self.funny['text']=txt 

    def abusal(self):
        self.clear()

        lbl1=Label(self.root,text="NLPAPP",bg="#010313",fg="white")
        lbl1.pack(pady=(30,30)) 
        lbl1.configure(font=('verdana',24,'bold'))

        lbl2=Label(self.root,text="Abuse check",bg="#010313",fg="white") 
        lbl2.pack(pady=(10,10))
        lbl2.configure(font=('verdana',16))

        lbl3=Label(self.root,text="Enter the text")
        lbl3.pack(pady=(10,10))

        self.hen1=Entry(self.root,width=50)
        self.hen1.pack(pady=(10,10),ipady=5)

        but1=Button(self.root,text="Analyze",width=10,height=2,command=self.abusal1) 
        but1.pack(pady=(10,10)) 

        self.abuse_txt=Label(self.root,text='',bg="#010313",fg="white")
        self.abuse_txt.pack(pady=(10,10))
        self.abuse_txt.configure(font=('verdana',16))

        go_back=Button(self.root,text="Go back",width=10,height=2,command=self.appgui)
        go_back.pack(pady=(10,10)) 

    def abusal1(self):
        c1=self.hen1.get()
        c2=self.ms.get_abuse(c1)
        txt=''
        for i in c2:
            txt=txt+i+'---->'+str(c2[i])+'\n'
        self.abuse_txt['text']=txt

    
        

        

    

    
    

d=nlps()