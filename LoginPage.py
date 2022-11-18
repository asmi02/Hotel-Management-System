from tkinter import *
from tkinter import messagebox
# from tkinter.ttk import Combobox

import pymysql

class LoginClass:
    def __init__(self):
        self.window=Tk()
        #--------------- settings ----------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1=800
        h1=400
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,400,200))
        self.window.config(background="#cadaf7")
        self.window.title("Login Page")

        # --------------------- background image -----------------
        from PIL import Image, ImageTk
        self.bimg1 = Image.open("Project_Pics//login.png")
        self.bimg1 = self.bimg1.resize((200, 200))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.window, image=self.bimg2,background="#cadaf7")
        self.bimglbl.place(x=500, y=100)

        #---------------------------------------------------------

        #-------------- widgets -----------------------------------

        self.headlbl = Label(self.window,text="Welcome to Apna Hotel",background="#cadaf7",
                             foreground="white",font=("CentSchbkCyrill BT",25,"bold"))

        mycolor1="white"
        myfont1 = ("CentSchbkCyrill BT",15,"bold")
        self.L1 = Label(self.window,text="Username",background="#cadaf7",font=myfont1)
        self.L2 = Label(self.window,text="Password",background="#cadaf7",font=myfont1)

        self.t1 = Entry(self.window)
        self.t2 = Entry(self.window,show='*')


        #--------------- buttons ----------------------------------
        self.b1 = Button(self.window,text="Let me in!!!",background="black",
                         foreground='white',command=self.fetchData,height=2,width=100)

        self.window.bind("<Key>",self.show)


        #--------- placements ------------------------------------------------

        self.headlbl.place(x=0,y=0,width=w1,height=90)
        x1=10
        y1=100
        x_diff=200
        y_diff=50

        self.L1.place(x=x1+100,y=y1)
        self.t1.place(x=x1+x_diff+50,y=y1,height=30,width=120)

        y1+=y_diff
        self.L2.place(x=x1+100,y=y1+5)
        self.t2.place(x=x1+x_diff+50,y=y1,height=30,width=120)

        y1+=y_diff
        self.b1.place(x=x1+150,y=y1+50,width=120,height=40)

        hcolor = "#464744"
        bg2 = "black"
        self.b1.bind("<Enter>", lambda e: self.changeColor(hcolor, "b1"))
        self.b1.bind("<Leave>", lambda e: self.changeColor(bg2, "b1"))

        self.window.mainloop()

    def show(self,evt):
        if evt.keysym == 'Return':
            self.fetchData()

    def changeColor(self, c, name):
        if name == "b1":
            self.b1.config(background=c)

    def databaseConnection(self):
        myhost="localhost"
        mydb="hotelmgmtdb"
        myuser="root"
        mypassword=""
        try:
            self.conn = pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting database \n"+str(e),parent=self.window)

    def fetchData(self):
        self.databaseConnection()
        try:
            myqry = "select * from usertable where username=%s and password=%s"
            rowcount = self.curr.execute(myqry,(self.t1.get(),self.t2.get()))
            data = self.curr.fetchone()
            if data:
                uname=data[0]
                utype=data[2]
                messagebox.showinfo("Success","Welcome"+utype,parent=self.window)
                self.window.destroy()
                from Entrypage import Entrypage
                Entrypage(uname,utype)
            else:
                messagebox.showinfo("Failure","Wrong username or password",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window)



if __name__ == '__main__':
    LoginClass()

