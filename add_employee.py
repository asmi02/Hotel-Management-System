from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from search_employee import *
import pymysql as pymysql

from PIL import Image,ImageTk


class add_employee:
    default_image = "Capture.jpg"
    def __init__(self,hwindow,col=None):
        # self.window = Tk()
        self.window=Toplevel(hwindow)
        self.window.title("Add Employee")
        # --------Window settings-----
        h = self.window.winfo_screenwidth()
        w = self.window.winfo_screenheight()

        w1 = 1000
        h1 = 760
        self.window.minsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 300, 20))
        # self.window.state("zoomed")
        self.window.config(background="#69e5f4")

        # --------------------- background image -----------------
        from PIL import Image, ImageTk
        self.bimg1 = Image.open("Project_Pics//add_employee4.webp")
        self.bimg1 = self.bimg1.resize((300, 300))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.window, image=self.bimg2,background="#69e5f4")
        self.bimglbl.place(x=600, y=400)

        #--------------Add employee form-------
        font1=["Candara",40,"bold"]
        font2=["Calibri",14,"bold"]
        font3=["Calibri",12,""]
        bg="#69e5f4"
        fg="white"
        self.hd=Label(self.window,text="Add Employee Details",font=font1,foreground=fg,background=bg)
        self.l1=Label(self.window,text="Name",background=bg,font=font2)
        self.t1=Entry(self.window)
        self.l2=Label(self.window,text="DOB(yy-mm-dd)",background=bg,font=font2)
        self.t2=DateEntry(self.window,width=12, background='darkblue',
                            foreground='white', borderwidth=2,year=2010,date_pattern ="y-mm-dd")
        self.l3=Label(self.window,text="Gender",background=bg,font=font2)
        self.v1=StringVar()
        self.r1=Radiobutton(self.window,text="Male",value="Male",variable=self.v1,background=bg,font=font2)
        self.r2=Radiobutton(self.window,text="Female",value="Female",variable=self.v1,background=bg,font=font2)
        self.v1.set(None)
        self.l4=Label(self.window,text="Job",background=bg,font=font2)
        self.v2=StringVar()
        self.c1=Combobox(self.window,values=["Front Desk Clerks","Housekeeping","Kitchen Staff",
                                             "Room Service","Waiter/Waitress","Manager","Accountant","Chef"]
                         ,textvariable=self.v2,state="readonly",background=bg,font=font3)
        self.v2.set("Choose the job")
        self.l5 = Label(self.window, text="Salary",background=bg,font=font2)
        self.t5 = Entry(self.window)
        self.l6 = Label(self.window, text="Phone",background=bg,font=font2)
        self.t6 = Entry(self.window)
        self.l7 = Label(self.window, text="Aadhar",background=bg,font=font2)
        self.t7 = Entry(self.window)
        self.l8 = Label(self.window, text="Email",background=bg,font=font2)
        self.t8 = Entry(self.window)


        # t1 t2 v1 v2 t5 t6 t7 t8

        # ----------------BUTTONS-----------------
        self.b1=Button(self.window,foreground="white",background="black",height=2,width=13,text="Submit"
                       ,cursor="hand2",command=self.saveData)

        self.b2 = Button(self.window, foreground="white", background="black", height=2, width=21, text="get particular record"
                         ,cursor="hand2", command=self.fetchData)

        self.b3 = Button(self.window, foreground="white", background="black", height=2, width=13, text="Clear Data"
                         ,cursor="hand2", command=self.clearPage)

        self.b4 = Button(self.window, foreground="white", background="black", height=2, width=13, text="Update Data"
                         ,cursor="hand2", command=self.updateData)

        self.b5 = Button(self.window, foreground="white", background="black", height=2, width=13, text="Delete Data"
                         , cursor="hand2" , command=self.deleteData)

        self.b6 = Button(self.window, foreground="white", background="black", height=2, width=13, text="Search Data"
                         ,cursor="hand2", command=lambda :employee_search(self.window,self.t1.get()))

        self.imglbl = Label(self.window, relief="groove", borderwidth=1)

        self.b7 = Button(self.window, text="Upload", background="black", cursor="hand2",
                         foreground='white', height=2, width=20, command=self.selectImage)

        hcolor = "#464744"
        bg2="black"
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
        self.b6.bind("<Enter>", lambda e: self.changeColor(hcolor, "b6"))
        self.b6.bind("<Leave>", lambda e: self.changeColor(bg2, "b6"))
        self.b7.bind("<Enter>", lambda e: self.changeColor(hcolor, "b7"))
        self.b7.bind("<Leave>", lambda e: self.changeColor(bg2, "b7"))


        # -----------------PLACEMENTS-----------------
        x1 = 100
        y1 = 150
        y1_diff = 50
        x1_diff = 200

        self.hd.place(x=50,y=0,width=w1,height=90)

        self.l1.place(x=x1, y=y1)
        self.t1.place(x=x1+x1_diff,y=y1,height=25,width=150)   #,height=2,width=10
        y1 = y1 + y1_diff

        self.l2.place(x=x1, y=y1)
        self.t2.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.l3.place(x=x1, y=y1)
        self.r1.place(x=x1+x1_diff,y=y1)
        self.r2.place(x=x1+x1_diff+80,y=y1)
        y1 = y1 + y1_diff

        self.l4.place(x=x1, y=y1)
        self.c1.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.l5.place(x=x1, y=y1)
        self.t5.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.l6.place(x=x1, y=y1)
        self.t6.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.l7.place(x=x1, y=y1)
        self.t7.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.l8.place(x=x1, y=y1)
        self.t8.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.b1.place(x=x1, y=y1+30)
        self.b2.place(x=x1+110, y=y1+30)
        self.b3.place(x=x1, y=y1+80)
        self.b4.place(x=x1+110, y=y1+80)
        self.b5.place(x=x1+220, y=y1+80)
        self.b6.place(x=x1+330, y=y1+80)
        self.b7.place(x=x1 + 550, y=300)

        self.imglbl.place(x=x1 + 549.5, y=150, width=150, height=150)

        self.clearPage()
        if col!=None:
            self.fetchData(col)
        self.window.mainloop()

        # --------Functions----------

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
        elif name == "b6":
            self.b6.config(background=c)

    def selectImage(self):
        self.filename = askopenfilename(file=[("All Pictures", "*.jpg;*.png;*.jpeg")
            , ("PNG Images", "*.png"), ("Jpg Images", "*.jpg")], parent=self.window)
        print("filename = ", self.filename)
        if self.filename != "":
            # open and resize image
            self.img1 = Image.open(self.filename)
            self.img1 = self.img1.resize((150, 150))

            # converting and adding image to label
            self.img2 = ImageTk.PhotoImage(self.img1)
            self.imglbl.config(image=self.img2)
            # making unique name
            path = self.filename.split("/")
            name = path[-1]
            print("path = ", path)
            print("name = ", name)
            import time
            uniqueness = str(int(time.time()))
            print("uniqueness = ", uniqueness)
            self.actualname = uniqueness + name
            print("actual name = ", self.actualname)



#   STEP 1: MAKE DATABASE CONNECTION
    def databaseConnection(self):
        myhost="localhost"
        mydb="hotelmgmtdb"
        myuser="root"
        mypassword=""
        try:
            self.conn=pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr=self.conn.cursor()

        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting database \n"+str(e),parent=self.window)

    # STEP 2 : MAKE SAVE DATA QUERY
    def saveData(self):
        if self.validate_check()==False:
            return # stop this function now

        # save image
        if self.actualname == self.default_image:  # no image is selected
            # nothing to save in folder
            pass
        else:
            self.img1.save("employee_images//" + self.actualname)

        self.databaseConnection()
            #Name DOB Gender Job Salary	Phone Aadhar Email
        try:
            myqry = "insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount=self.curr.execute(myqry,(self.t1.get(),self.t2.get(),self.v1.get(),self.v2.get(),self.t5.get(),
                                              self.t6.get(),self.t7.get(),self.t8.get(),self.actualname))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Employee Data saved successfully",parent=self.window)
                self.clearPage()
            else:
                messagebox.showinfo("Failure","Check all fields carefully",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window)


    #STEP 3:  FETCH DATA
    # Name DOB Gender Job Salary Phone Aadhar Email
    def fetchData(self,value=None):
        if value==None:
            Aadhar=self.t7.get()
        else:
            Aadhar=value
        self.databaseConnection()
        # Name DOB Gender Job Salary Phone Aadhar Email
        try:
            myqry="select * from employee where aadhar=%s"
            rowcount=self.curr.execute(myqry,(Aadhar))
            data=self.curr.fetchone()
            self.clearPage()

            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.v1.set(data[2])
                self.v2.set(data[3])
                self.t5.insert(0,data[4])
                self.t5.insert(0,data[4])
                self.t6.insert(0,data[5])
                self.t7.insert(0,data[6])
                self.t8.insert(0,data[7])
                self.actualname = data[8]
                self.oldname = data[8]
                self.img1 = Image.open("employee_images//" + self.actualname)
                self.img1 = self.img1.resize((150, 150))

                self.b4['state']='normal'
                self.b5['state']='normal'

            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window)
        except Exception as e:
                messagebox.showerror("Query Error", "Error while fetching data \n" + str(e), parent=self.window)

    #STEP4:UPDATE DATA
    def updateData(self):
        if self.validate_check()==False:
            return # stop this function now

        if self.actualname==self.oldname: #no new image is selected
            #nothing to save or delete from folder
            pass
        else:  # new image is selected
            self.img1.save("employee_images//"+self.actualname)
            if self.oldname==self.default_image: # no image was given in past
                # nothing to delete
                pass
            else:
                import os
                os.remove("employee_images//"+self.oldname)

        self.databaseConnection()
        #Name	DOB	Gender	Job	Salary	Phone	Aadhar	Email
        try:
            myqry= "update employee set Name=%s, DOB=%s, Gender=%s,Job=%s, Salary=%s, Phone=%s, Email=%s, ProfilePic=%s where Aadhar=%s"
            rowcount=self.curr.execute(myqry,(self.t1.get(),self.t2.get(),self.v1.get(),self.v2.get(),self.t5.get(),
                                       self.t6.get(),self.t8.get(),self.actualname,self.t7.get()))
            self.conn.commit()

            if rowcount==1:
                messagebox.showinfo("Success","Employee Data Updated successfully",parent=self.window)
                self.clearPage()

            else:
                messagebox.showinfo("Failure","Check all the fields carefully",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error","Error while updation \n"+str(e),parent=self.window)

    #STEP5:DELETE DATA
    def deleteData(self):
        ans=messagebox.askquestion("Confirmation","Are you sure you want to delete this entry ?")
        if ans=='yes':

            if self.oldname==self.default_image: # no image was given in past
                # nothing to delete
                pass
            else:
                import os
                os.remove("employee_images//"+self.oldname)


            self.databaseConnection()

            # Name	DOB	Gender	Job	Salary	Phone	Aadhar	Email

            try:
                myqry="delete from employee where Aadhar=%s"
                rowcount=self.curr.execute(myqry,(self.t7.get()))
                self.conn.commit()

                if rowcount==1:
                    messagebox.showinfo("Success","Employee data deleted successfully",parent=self.window)
                    self.clearPage()
                else:
                    messagebox.showinfo("Failure","Check all the fields carefully",parent=self.window)

            except Exception as e:
                messagebox.showerror("Query Error","Error while deletion \n"+str(e),parent=self.window)
    #STEP6: SEARCH DATA
    #in another file

    def clearPage(self):
        # Name DOB Gender Job Salary Phone Aadhar Email
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.v1.set(None)
        self.v2.set("Choose the job")
        self.t5.delete(0,END)
        self.t6.delete(0,END)
        self.t7.delete(0,END)
        self.t8.delete(0,END)
        self.actualname = self.default_image
        self.img1 = Image.open("customer_images//" + self.actualname)
        self.img1 = self.img1.resize((150, 150))

        # converting and adding image to label
        self.img2 = ImageTk.PhotoImage(self.img1)
        self.imglbl.config(image=self.img2)

        self.b4['state'] = 'disabled'
        self.b5['state'] = 'disabled'


    def validate_check(self):
        # t1 t2 v1 v2 t5 t6 t7 t8
        if not(self.t1.get().isalpha())   or  len(self.t1.get())<2:
            messagebox.showwarning("Validation Check", "Enter proper name ", parent=self.window)
            return False

        elif self.t2.get()=="":
            messagebox.showwarning("Validation Check", "Enter your DOB", parent=self.window)
            return False


        elif not (self.v1.get() == 'Male' or self.v1.get() == 'Female'):
            messagebox.showwarning("Input Error", "Please Select gender ", parent=self.window)
            return False

        elif (self.v2.get() == "Choose the job")or (self.v2.get() == "No Job"):
            messagebox.showwarning("Input Error", "Please Select Employee Job ", parent=self.window)
            return False

        elif not(self.t5.get().isdigit())   or  len(self.t5.get())<4:
            messagebox.showwarning("Input Error", "Please Enter Correct Salary ", parent=self.window)
            return False

        elif not(self.t6.get().isdigit())   or  len(self.t6.get())!=10:
            messagebox.showwarning("Validation Check", "Enter valid phone no \n10 digits only", parent=self.window)
            return False


        elif not(self.t7.get().isdigit())   or  len(self.t7.get())!=12:
            messagebox.showwarning("Validation Check", "Enter valid Aadhar Number", parent=self.window)
            return False


        elif (self.t8.get().find("@")==-1)   :
            messagebox.showwarning("Input Error", "Please corect Email Address ", parent=self.window)
            return False
        return True

if __name__=='__main__':
    dummy_add_employee=Tk()
    add_employee(dummy_add_employee)
    dummy_add_employee.mainloop()