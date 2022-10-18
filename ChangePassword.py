from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql

class ChangePasswordClass:
    def __init__(self,hwindow,un):
        self.uname=un
        self.window=Toplevel(hwindow)  # homepage(hwindow) acts as parent window for student(self.window)
        #--------------- settings ----------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1=800
        h1=400
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,400,200))

        # --------------------- background image -----------------
        from PIL import Image, ImageTk
        self.bimg1 = Image.open("Project_Pics//change_password.png")
        self.bimg1 = self.bimg1.resize((200, 200))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.window, image=self.bimg2, background="#ebe7ca")
        self.bimglbl.place(x=500, y=100)

        #-------------- widgets -----------------------------------

        self.headlbl = Label(self.window,text="Change Password",background="#ebe7ca",
                             foreground="black",font=("CentSchbkCyrill BT",40,"bold"))

        mycolor1="#ebe7ca"
        myfont1 = ("CentSchbkCyrill BT",10,"bold")
        self.window.config(background=mycolor1)
        self.L1 = Label(self.window,text="Current Password",background=mycolor1,font=myfont1)
        self.L2 = Label(self.window,text="New Password",background=mycolor1,font=myfont1)
        self.L3 = Label(self.window,text="Confirm Password",background=mycolor1,font=myfont1)

        self.t1 = Entry(self.window,show='*')
        self.t2 = Entry(self.window,show='*')
        self.t3 = Entry(self.window,show='*')


        #--------------- buttons ----------------------------------
        self.b1 = Button(self.window,text="Change",background="black",
                    foreground='white',command=self.updateData)

        #--------- placements ------------------------------------------------

        self.headlbl.place(x=0,y=0,width=w1,height=90)
        x1=10
        y1=120
        x_diff=100
        y_diff=50

        self.L1.place(x=x1+100,y=y1)
        self.t1.place(x=x1+x_diff+200,y=y1,height=30,width=120)
        y1+=y_diff
        self.L2.place(x=x1+100,y=y1)
        self.t2.place(x=x1+x_diff+200,y=y1,height=30,width=120)
        y1+=y_diff
        self.L3.place(x=x1+100,y=y1)
        self.t3.place(x=x1+x_diff+200,y=y1,height=30,width=120)

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

    def updateData(self):
        if self.t2.get() == self.t3.get():
            self.databaseConnection()
            try:
                myqry = "update usertable set password=%s where username=%s and password=%s"
                rowcount = self.curr.execute(myqry, (self.t2.get(), self.uname, self.t1.get()))
                self.conn.commit()
                if rowcount == 1:
                    messagebox.showinfo("Success", "Password Changed successfully", parent=self.window)
                    self.clearPage()
                else:
                    messagebox.showinfo("Failure", "Wrong Password", parent=self.window)
            except Exception as e:
                messagebox.showerror("Query Error", "Error while updation \n" + str(e), parent=self.window)
        else:
            messagebox.showwarning("Warning", "Confirm Password carefully", parent=self.window)

    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)

#
# if __name__=='__main__':
#     dummy_employee_report = Tk()
#     ChangePasswordClass(dummy_employee_report,"ritu")
#     dummy_employee_report.mainloop()