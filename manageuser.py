from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql

class UserClass:
    def __init__(self,hwindow):
        self.window=Toplevel(hwindow)  # homepage(hwindow) acts as parent window for student(self.window)
        #--------------- settings ----------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1=w-100
        h1=h-180
        self.window.minsize(1100,500)
        self.window.geometry("%dx%d+%d+%d"%(1100,600,250,100))

        self.window.config(background="#caf7df")
        self.window.title("Manage User")

        # --------------------- background image -----------------
        from PIL import Image, ImageTk
        self.bimg1 = Image.open("Project_Pics//manage_user2.webp")
        self.bimg1 = self.bimg1.resize((200, 200))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.window, image=self.bimg2, background="#caf7df")
        self.bimglbl.place(x=100, y=380)

        #-------------- widgets -----------------------------------

        self.headlbl = Label(self.window,text="User",background="#caf7df",
                             foreground="white",font=("CentSchbkCyrill BT",40,"bold"))

        mycolor1="white"
        myfont1 = ("CentSchbkCyrill BT",10,"bold")
        self.L1 = Label(self.window,text="Username",background=mycolor1,font=myfont1)
        self.L2 = Label(self.window,text="Password",background=mycolor1,font=myfont1)
        self.L3 = Label(self.window,text="User Type",background=mycolor1,font=myfont1)

        self.t1 = Entry(self.window)
        self.t2 = Entry(self.window,show='*')
        self.v1 =  StringVar()
        self.c1 = Combobox(self.window,textvariable=self.v1,values=("Admin","Employee"))
        #------------------ table ---------------------------------------
        self.tablearea = Frame(self.window)
        self.mytable = Treeview(self.tablearea,columns=['c1','c2'],height=10)
        self.mytable.heading("c1",text="User Name")
        self.mytable.heading("c2",text="User Type")
        self.mytable['show']='headings'

        self.mytable.column("#1",width=200,anchor='center')
        self.mytable.column("#2",width=200,anchor='center')
        self.mytable.pack()
        self.mytable.bind("<ButtonRelease-1>",lambda e: self.getSelectedRowData())



        #--------------- buttons ----------------------------------
        self.b1 = Button(self.window,text="Save",background="black",foreground='white',command=self.saveData)
        self.b2 = Button(self.window,text="Update",background="black",foreground='white',command=self.updateData)
        self.b3 = Button(self.window,text="Delete",background="black",foreground='white',command=self.deleteData)
        self.b4 = Button(self.window,text="Fetch",background="black",foreground='white',command=self.fetchData)
        self.b5 = Button(self.window,text="Search",background="black",foreground='white',command=self.fetchAllData)


        #--------- placements ------------------------------------------------

        self.headlbl.place(x=0,y=0,width=w1,height=90)
        x1=100
        y1=100
        x_diff=150
        y_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)
        self.b4.place(x=x1+x_diff+x_diff+50,y=y1)
        self.tablearea.place(x=x1+500,y=y1)
        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)
        self.b5.place(x=x1+x_diff+x_diff+50,y=y1)
        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=100,height=30)
        self.b2.place(x=x1+x_diff,y=y1,width=100,height=30)
        self.b3.place(x=x1+x_diff+x_diff,y=y1,width=100,height=30)

        hcolor = "#464744"
        bg2 = "black"
        self.b1.bind("<Enter>", lambda e: self.changeColor(hcolor, "b1"))
        self.b1.bind("<Leave>", lambda e: self.changeColor(bg2, "b1"))
        self.b2.bind("<Enter>", lambda e: self.changeColor(hcolor, "b2"))
        self.b2.bind("<Leave>", lambda e: self.changeColor(bg2, "b2"))
        self.b3.bind("<Enter>", lambda e: self.changeColor(hcolor, "b3"))
        self.b3.bind("<Leave>", lambda e: self.changeColor(bg2, "b3"))
        self.b4.bind("<Enter>", lambda e: self.changeColor(hcolor, "b4"))
        self.b4.bind("<Leave>", lambda e: self.changeColor(bg2, "b4"))
        self.b5.bind("<Enter>", lambda e: self.changeColor(hcolor, "b5"))
        self.b5.bind("<Leave>", lambda e: self.changeColor(bg2, "b5"))


        self.clearPage()
        self.window.mainloop()

    def changeColor(self, c, name):
        if name == "b1":
            self.b1.config(background=c)
        elif name == "b2":
            self.b2.config(background=c)
        elif name == "b3":
            self.b3.config(background=c)
        elif name == "b4":
            self.b4.config(background=c)
        elif name == "b5":
            self.b5.config(background=c)


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
                messagebox.showinfo("Success","User Data saved successfully",parent=self.window)
                self.clearPage()
            else:
                messagebox.showinfo("Failure","Check all fields carefully",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window)

    def updateData(self):
        if self.validate_check()==False:
            return

        self.databaseConnection()
        try:
            myqry = "update usertable set password=%s,usertype=%s where username=%s"
            rowcount = self.curr.execute(myqry,(self.t2.get(),self.v1.get(),self.t1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","User Data updated successfully",parent=self.window)
                self.clearPage()
            else:
                messagebox.showinfo("Failure","Check all fields carefully",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while updation \n"+str(e),parent=self.window)

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to delete ??",parent=self.window)
        if ans=="yes":

            self.databaseConnection()
            try:
                myqry = "delete from usertable where username=%s"
                rowcount = self.curr.execute(myqry,(self.t1.get()))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success","User Data Deleted successfully",parent=self.window)
                    self.clearPage()
                else:
                    messagebox.showinfo("Failure","Check all fields carefully",parent=self.window)
            except Exception as e:
                messagebox.showerror("Query Error","Error while deletion \n"+str(e),parent=self.window)

    def getSelectedRowData(self):
        id = self.mytable.focus()
        data = self.mytable.item(id)
        content = data['values']
        col1 = content[0]
        self.fetchData(col1)

    def fetchData(self,val=None):
        if val==None:
            un=self.t1.get()
        else:
            un=val
        self.databaseConnection()
        try:
            myqry = "select * from usertable where username=%s"
            rowcount = self.curr.execute(myqry,(un))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                # print(data)
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.v1.set(data[2])
                self.b2['state']='normal'
                self.b3['state']='normal'


            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.c1.set("Choose UserType")
        self.b2['state']='disabled'
        self.b3['state']='disabled'
        self.fetchAllData()

    def fetchAllData(self):
        self.databaseConnection()
        try:
            utype=self.v1.get()
            if utype=="Choose UserType":
                utype=""
            myqry = "select * from usertable where usertype like %s"
            rowcount = self.curr.execute(myqry,(utype+"%"))
            data = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            if data:
                # print(data)
                for row in data:
                    r1=[row[0],row[2]]
                    self.mytable.insert("",END,values=r1)
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window)

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


# if __name__ == '__main__':
#     dummy_homepage=Tk()
#     UserClass(dummy_homepage)
#     dummy_homepage.mainloop()






















