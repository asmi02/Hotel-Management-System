from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import pymysql

class CreateUserClass:
    def __init__(self):
        self.window=Tk()
        #--------------- settings ----------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1=800
        h1=400
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,300,200))
        self.window.config(background="#f4b676")
        self.window.title("Create Admin")

        # --------------------- background image -----------------
        from PIL import Image, ImageTk
        self.bimg1 = Image.open("Project_Pics//admin.jpg")
        self.bimg1 = self.bimg1.resize((200, 200))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.window, image=self.bimg2, background="#f4b676")
        self.bimglbl.place(x=500, y=100)

        #-------------- widgets -----------------------------------

        self.headlbl = Label(self.window,text="Welcome to Apna Hotel",background="#f4b676",
                             foreground="white",font=("CentSchbkCyrill BT",25,"bold"))

        mycolor1="white"
        bg="#f4b676"
        myfont1 = ("CentSchbkCyrill BT",12,"bold")

        self.L1 = Label(self.window,text="Username",background=bg,font=myfont1)
        self.L2 = Label(self.window,text="Password",background=bg,font=myfont1)
        self.L3 = Label(self.window,text="User Type",background=bg,font=myfont1)

        self.t1 = Entry(self.window)
        self.t2 = Entry(self.window,show='*')
        self.v1 =  StringVar()
        self.c1 = Combobox(self.window,textvariable=self.v1,values=("Admin","Employee"),state='disabled')
        self.c1.current(0)


        #--------------- buttons ----------------------------------
        self.b1 = Button(self.window,text="Create Admin",background="black",
                         foreground='white',command=self.saveData)


        #--------- placements ------------------------------------------------

        self.headlbl.place(x=0,y=0,width=w1,height=90)
        x1=10
        y1=100
        x_diff=100
        y_diff=50

        self.L1.place(x=x1+100,y=y1)
        self.t1.place(x=x1+x_diff+150,y=y1,height=25,width=120)

        y1+=y_diff
        self.L2.place(x=x1+100,y=y1)
        self.t2.place(x=x1+x_diff+150,y=y1,height=25,width=120)
        y1+=y_diff
        self.L3.place(x=x1+100,y=y1)
        self.c1.place(x=x1+x_diff+150,y=y1,height=25,width=120)

        y1+=y_diff
        self.b1.place(x=x1+150,y=y1+50,width=120,height=40)

        hcolor = "#464744"
        bg2 = "black"
        self.b1.bind("<Enter>", lambda e: self.changeColor(hcolor, "b1"))
        self.b1.bind("<Leave>", lambda e: self.changeColor(bg2, "b1"))

        self.clearPage()
        self.window.mainloop()

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

    def saveData(self):
        if self.validate_check()==False:
            return # stop this function now

        self.databaseConnection()
        try:
            myqry = "insert into usertable values(%s,%s,%s)"
            rowcount = self.curr.execute(myqry,(self.t1.get(),self.t2.get(),self.v1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Admin Created successfully",parent=self.window)
                self.window.destroy()
                from LoginPage import LoginClass
                LoginClass()
            else:
                messagebox.showinfo("Failure","Check all fields carefully",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window)


    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)

    def validate_check(self):
        if len(self.t1.get())<3:
            messagebox.showwarning("Validation Check", "Enter user name", parent=self.window)
            return False
        elif len(self.t2.get())<3:
            messagebox.showwarning("Validation Check", "Enter proper password ", parent=self.window)
            return False
        elif (self.v1.get() == "Choose UserType"):
            messagebox.showwarning("Input Error", "Please Select Usertype ", parent=self.window)
            return False
        return True


if __name__ == '__main__':
    CreateUserClass()
