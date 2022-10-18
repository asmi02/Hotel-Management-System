from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox
import time

from PIL import Image,ImageTk

import pymysql

from search_customer import search_customer


class customer_form:
    default_image = "Capture.jpg"
    def __init__(self,hwindow,col=None):
        # self.window = Tk()
        self.window=Toplevel(hwindow)
        self.window.title("Add Customer details")
        # --------Window settings-----
        h = self.window.winfo_screenwidth()
        w = self.window.winfo_screenheight()

        w1 = 1200
        h1 = 800
        self.window.minsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 150, 1))
        # self.window.state("zoomed")
        self.window.config(background="#f0c0d6")

        #--------------------- background image -----------------
        from PIL import Image,ImageTk
        self.bimg1 = Image.open("Project_Pics//add_customer.png")
        self.bimg1 = self.bimg1.resize((400,400))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl=Label(self.window,image=self.bimg2,background="#f0c0d6")
        self.bimglbl.place(x=750,y=350)

        #--------------Add customer details form-------
        font1=["Candara",40,"bold"]
        font2 = ["Calibri", 14, "bold"]
        font3 = ["Calibri", 12, ""]
        bg="#f0c0d6"
        self.hd=Label(self.window,text="Add Customer Details",font=font1,
                      background=bg,foreground="White")

        self.l1=Label(self.window,text="ID",background=bg,font=font2)
        self.v1=StringVar()
        self.c1=Combobox(self.window,values=["Passport","Voter Id","Driving License","Aadhar"],
                         textvariable=self.v1,state="readonly",font=font3)
        self.v1.set("Select ID")

        self.l2=Label(self.window,text="Id Number",background=bg,font=font2)
        self.t2=Entry(self.window)

        self.l3=Label(self.window,text="Name",background=bg,font=font2)
        self.t3=Entry(self.window)

        self.l4 = Label(self.window, text="Gender",background=bg,font=font2)
        self.v2 = StringVar()
        self.r1 = Radiobutton(self.window, text="Male", value="Male", variable=self.v2,background=bg,font=font2)
        self.r2 = Radiobutton(self.window, text="Female", value="Female", variable=self.v2,background=bg,font=font2)
        self.v2.set(None)

        self.l5 = Label(self.window, text="Phone Number",background=bg,font=font2)
        self.t5 = Entry(self.window)

        self.l6 = Label(self.window,text="Room Type",background=bg,font=font2)
        self.v3 = StringVar()
        self.c3 = Combobox(self.window, values=["Single Bed","Double Bed"],
                           textvariable=self.v3, state="readonly",font=font3)
        self.v3.set("Select Room Type")
        self.c3.bind("<<ComboboxSelected>>", lambda e: self.getAvailableRooms())


        self.l7 = Label(self.window, text="Allocated Room Number",background=bg,font=font2)
        self.v4 = StringVar()
        self.c4 = Combobox(self.window,textvariable=self.v4, state="readonly",font=font3)
        self.v4.set("Allot Room Number")
        self.c4.bind("<<ComboboxSelected>>", lambda e: self.fetchDataAmount())

        self.l8 = Label(self.window, text="Check-in Time",background=bg,font=font2)
        var=time.ctime()
        self.t8=Label(self.window,text=var,background=bg,font=["",9,"bold"])



        self.l9=Label(self.window,text="Amount To Pay",background=bg,font=font2)
        self.t9=Label(self.window,background=bg,font=["",9,"bold"])


        self.l10=Label(self.window,text="Deposit",background=bg,font=font2)
        self.t10=Entry(self.window)

        # v1 t2 t3 v2 t5 v3 v4 t8 t9 t10

        #-----------BUTTONS--------------
        self.b1=Button(self.window,foreground="white",background="black",height=2,width=13,text="Add Customer",cursor="hand2"
                       ,command=self.saveData)

        self.b2 = Button(self.window, foreground="white", background="black", height=2, width=21,
                         text="get particular record",cursor="hand2"
                         , command=self.fetchData)

        self.b3 = Button(self.window, foreground="white", background="black", height=2, width=13,cursor="hand2", text="Clear Data"
                         , command=self.clearPage)

        self.b4 = Button(self.window, foreground="white", background="black",cursor="hand2", height=2, width=13, text="Update Data"
                         , command=self.updateData)

        self.b5 = Button(self.window, foreground="white",cursor="hand2", background="black", height=2, width=13, text="Delete Data"
                         , command=self.deleteData)

        self.b6 = Button(self.window, foreground="white",cursor="hand2", background="black", height=2, width=13, text="Search Data"
                         , command=lambda: search_customer(self.window, self.t3.get()))

        self.imglbl = Label(self.window, relief="groove", borderwidth=1)

        self.b7 = Button(self.window, text="Upload", background="black",cursor="hand2",
                         foreground='white',height=2, width=20,command=self.selectImage)

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


        #-----------PLACEMENTS-----------
        x1 = 200
        y1 = 150
        y1_diff = 50
        x1_diff = 250

        self.hd.place(x=0,y=0,width=w1,height=90)

        self.l1.place(x=x1, y=y1)
        self.c1.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.l2.place(x=x1,y=y1)
        self.t2.place(x=x1 + x1_diff, y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.l3.place(x=x1,y=y1)
        self.t3.place(x=x1 + x1_diff, y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.l4.place(x=x1, y=y1)
        self.r1.place(x=x1+x1_diff,y=y1)
        self.r2.place(x=x1+x1_diff+100,y=y1)
        y1 = y1 + y1_diff

        self.l5.place(x=x1, y=y1)
        self.t5.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.l6.place(x=x1, y=y1)
        self.c3.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.l7.place(x=x1, y=y1)
        self.c4.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.l8.place(x=x1, y=y1)
        self.t8.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.l9.place(x=x1, y=y1)
        self.t9.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1= y1+y1_diff


        self.l10.place(x=x1, y=y1)
        self.t10.place(x=x1+x1_diff,y=y1,height=25,width=150)
        y1 = y1 + y1_diff

        self.b1.place(x=x1, y=y1+30)
        self.b2.place(x=x1 + 110, y=y1 + 30)
        self.b3.place(x=x1, y=y1 + 80)
        self.b4.place(x=x1 + 110, y=y1 + 80)
        self.b5.place(x=x1 + 220, y=y1 + 80)
        self.b6.place(x=x1 + 330, y=y1 + 80)
        self.b7.place(x=x1 + 550, y=300)

        self.imglbl.place(x=x1 + 549.5, y=150, width=150, height=150)

        self.clearPage()
        if col != None:
            self.fetchData(col)
        self.window.mainloop()

#         ------------Functions----------

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

#   ---------------Queries------------------
    # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit

    # Make connection with database

    def databaseConnection(self):
        myhost="localhost"
        mydb="hotelmgmtdb"
        myuser="root"
        mypassword=""

        try:
            self.conn=pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr=self.conn.cursor()

        except Exception as e:
            messagebox.showerror("Query Error","Error while connecting with database\n"+str(e),parent=self.window)


    def selectImage(self):
        self.filename = askopenfilename(file=[  ("All Pictures","*.jpg;*.png;*.jpeg")
            ,("PNG Images","*.png"),("Jpg Images","*.jpg")      ],parent=self.window)
        print("filename = ",self.filename)
        if self.filename!="":
            #open and resize image
            self.img1 = Image.open(self.filename)
            self.img1 = self.img1.resize((150,150))

            #converting and adding image to label
            self.img2 = ImageTk.PhotoImage(self.img1)
            self.imglbl.config(image=self.img2)
            # making unique name
            path = self.filename.split("/")
            name = path[-1]
            print("path = ",path)
            print("name = ",name)
            import time
            uniqueness = str(int(time.time()))
            print("uniqueness = ",uniqueness)
            self.actualname = uniqueness+name
            print("actual name = ",self.actualname)

    #save data
    def saveData(self):
        if self.validate_check()==False:
            return # stop this function now

        # save image
        if self.actualname == self.default_image:  # no image is selected
            # nothing to save in folder
            pass
        else:
            self.img1.save("customer_images//" + self.actualname)


        self.databaseConnection()
        # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit

        try:
            myqry="insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount=self.curr.execute(myqry,(self.v1.get(),self.t2.get(),self.t3.get(),self.v2.get(),self.t5.get(),self.v3.get(),
                              self.v4.get(),self.t8.cget("text"),self.t9.cget("text"),self.t10.get(),self.actualname))
            myqry2 = "update rooms set Availability=%s where RoomNumber=%s"
            rowcount2=self.curr.execute(myqry2,("Occupied",self.v4.get()))

            self.conn.commit()

            if rowcount==1 and rowcount2==1:
                messagebox.showinfo("Success","Customer Data saved successfully",parent=self.window)
                self.clearPage()
            else:
                messagebox.showinfo("Failure","Check all fields carefully",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window)


    def fetchDataAmount(self):
        # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        self.databaseConnection()
        myqry="select Price from rooms where RoomNumber=%s"
        rowcount=self.curr.execute(myqry,(self.v4.get()))
        data=self.curr.fetchone()

        try:
            if data:
                print(data)
                data2=str(data)
                i=1
                string=""
                while(data2[i]!=','):
                    string+=data2[i]
                    i+=1

                self.t9.config(text=string)

            else:
                self.t9.config(text="")

        except Exception as e:
            messagebox.showerror("Query Error", "Error while fetching amount \n" + str(e), parent=self.window)

    def getAvailableRooms(self):
        # RoomNumber	Availability	CleaningStatus	Price	BedType
        self.databaseConnection()
        try:
            myqry = "select RoomNumber from rooms where Availability=%s and BedType=%s"
            rowcount = self.curr.execute(myqry,("Available",self.v3.get()))
            data = self.curr.fetchall()
            mycomboboxlist=[]
            if data:
                print("Available = ",data)
                for row in data:
                    mycomboboxlist.append(row[0])
            else:
                self.c4.set("No Room Available")
            self.c4.config(values=mycomboboxlist)
        except Exception as e:
            messagebox.showerror("Query Error","Error while checking \n"+str(e),parent=self.window)



    def fetchData(self,value=None):
        # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        if value==None:
            ID_no=self.t2.get()
        else:
            ID_no=value
        self.databaseConnection()
        # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        try:
            myqry="select * from customer where ID_number = %s"
            rowcount=self.curr.execute(myqry,(ID_no))
            data=self.curr.fetchone()
            self.clearPage()

            if data:
                # v1 t2 t3 v2 t5 v3 v4 t8 t9 t10
                self.v1.set(data[0])
                self.t2.insert(0,data[1])
                self.t3.insert(0,data[2])
                self.v2.set(data[3])
                self.t5.insert(0,data[4])
                self.v3.set(data[5])
                self.v4.set(data[6])
                self.t8.config(text=data[7])
                self.t9.config(text=data[8])
                self.t10.insert(0,data[9])
                self.actualname = data[10]
                self.oldname = data[10]
                self.img1 = Image.open("customer_images//" + self.actualname)
                self.img1 = self.img1.resize((150, 150))

                self.oldroomnumber=self.v4.get()

                # converting and adding image to label
                self.img2 = ImageTk.PhotoImage(self.img1)
                self.imglbl.config(image=self.img2)

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
            self.img1.save("customer_images//"+self.actualname)
            if self.oldname==self.default_image: # no image was given in past
                # nothing to delete
                pass
            else:
                import os
                os.remove("customer_images//"+self.oldname)


        self.databaseConnection()
        # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        try:
            myqry= "update customer set ID=%s, Name=%s, Gender=%s,PhoneNumber=%s, Room_Type=%s, Allocated_Room_Nnumber=%s," \
                   " Check_in_time=%s,Amount_to_pay=%s,Deposit=%s,CustomerPic=%s where ID_number=%s"
            rowcount=self.curr.execute(myqry,(self.v1.get(),self.t3.get(),self.v2.get(),self.t5.get(),self.v3.get(),
                                       self.v4.get(),str(self.t8.cget("text")),str(self.t9.cget("text")),self.t10.get(),self.actualname
                                              ,self.t2.get()))
            self.conn.commit()

            if self.v4.get()!=self.oldroomnumber:
                print("old number = ",self.oldroomnumber)
                print("new number = ",self.v4.get())

                # RoomNumber	Availablity	CleaningStatus	Price	BedType
                myqry2 = "update rooms set Availability=%s where RoomNumber=%s"
                rowcount2 = self.curr.execute(myqry2, ("Occupied", self.v4.get().strip()))
                self.conn.commit()

                myqry3 = "update rooms set Availability=%s where RoomNumber=%s"
                rowcount3 = self.curr.execute(myqry3, ("Available", self.oldroomnumber.strip()))
                self.conn.commit()

                if rowcount2 ==1:
                    messagebox.showinfo("Success", "Rooms Data is also updated successfully", parent=self.window)
                else:
                    messagebox.showinfo("Failure", "Error while updating the room availability details rowcount2", parent=self.window)

                if rowcount3==1:
                    messagebox.showinfo("Success", "Rooms Data is also updated successfully", parent=self.window)
                else:
                    messagebox.showinfo("Failure", "Error while updating the room availability details rowcount3", parent=self.window)


            if rowcount==1:
                messagebox.showinfo("Success","Customer Data Updated successfully",parent=self.window)
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
                os.remove("customer_images//"+self.oldname)

            self.databaseConnection()

        # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit

            try:
                myqry="delete from customer where ID_number=%s"
                myqry2 = "update rooms set Availability=%s where RoomNumber=%s"

                rowcount = self.curr.execute(myqry, (self.t2.get()))
                rowcount2 = self.curr.execute(myqry2, ("Available", self.v4.get()))

                self.conn.commit()

                if rowcount==1 and rowcount2==1:
                    messagebox.showinfo("Success","Customer data deleted successfully",parent=self.window)
                    self.clearPage()
                else:
                    messagebox.showinfo("Failure","Check all the fields carefully",parent=self.window)

            except Exception as e:
                messagebox.showerror("Query Error","Error while deletion \n"+str(e),parent=self.window)


    def clearPage(self):
        # Name DOB Gender Job Salary Phone Aadhar Email
        self.v1.set("Select ID")
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.v2.set(None)
        self.t5.delete(0,END)
        self.v3.set("Select Room Type")
        self.v4.set("Allot Room Number")
        # self.t9.after(1000,self.t9.destroy())
        self.t9.config(text="")
        self.t10.delete(0,END)

        self.actualname = self.default_image
        self.img1 = Image.open("customer_images//" + self.actualname)
        self.img1 = self.img1.resize((150, 150))

        # converting and adding image to label
        self.img2 = ImageTk.PhotoImage(self.img1)
        self.imglbl.config(image=self.img2)

        self.b4['state'] = 'disabled'
        self.b5['state'] = 'disabled'


    def validate_check(self):
        # v1 t2 t3 v2 t5 v3 v4 t8 t9 t10
        if (self.v1.get() == "Select ID") or (self.v1.get() == "No Id"):
         messagebox.showwarning("Validation Check", "Enter customer ID Type", parent=self.window)
         return False

        elif len(self.t2.get())<3:
            messagebox.showwarning("Validation Check", "Enter correct id number ", parent=self.window)
            return False

        elif not (self.t3.get().isalpha()) or len(self.t3.get()) < 2:
            messagebox.showwarning("Validation Check", "Enter proper name ", parent=self.window)
            return False

        elif not (self.v2.get() == 'Male' or self.v2.get() == 'Female'):
            messagebox.showwarning("Input Error", "Please Select gender ", parent=self.window)
            return False

        elif not(self.t5.get().isdigit())   or  len(self.t5.get())!=10:
            messagebox.showwarning("Validation Check", "Enter valid phone no \n10 digits only", parent=self.window)
            return False

        elif (self.v3.get() == "Select Room Type") or (self.v3.get() == "No Room Type"):
         messagebox.showwarning("Validation Check", "Enter room type", parent=self.window)
         return False

        elif (self.v4.get() == "Allot Room Number") or (self.v4.get() == "No Allot Room Number"):
         messagebox.showwarning("Validation Check", "Please allot room number", parent=self.window)
         return False

        elif (self.t8.cget("text")==""):
            messagebox.showwarning("Validation Check", "Check in time is not there", parent=self.window)
            return False

        elif (self.t9.cget("text")==""):
            messagebox.showwarning("Validation Check", "Amount To Pay is not there check properly the pending dues", parent=self.window)
            return False

        elif (self.t10.get()=="" or len(self.t10.get())<0):
            messagebox.showwarning("Validation Check", "Deposit is not correct check properly the pending dues", parent=self.window)
            return False

        return True


if __name__=='__main__':
    dummy_customer_form=Tk()
    customer_form(dummy_customer_form)
    dummy_customer_form.mainloop()