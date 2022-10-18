#checkout table
# AllocatedRoomNumber	IDNumber	Name	CheckInTime	CheckOutTime	AmountPaid	AmountLeft	PendingAmountPayment	CheckOutCustomerPic

#rooms table
# RoomNumber	Availability	CleaningStatus	Price	BedType

# customer table
# ID	ID_number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit	CustomerPic

# employee table



from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from PIL import Image,ImageTk
import pymysql as pymysql

# from Entrypage import Entrypage


class CheckOut:
    default_image = "Capture.jpg"
    def __init__(self,hwindow):
        # self.window=Tk()

        self.window = Toplevel(hwindow)

        self.window.title("Check Out")
        #--------Window settings-----
        h=self.window.winfo_screenwidth()
        w=self.window.winfo_screenheight()

        w1=1000
        h1=760
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,300,20))
        # self.window.state("zoomed")

        self.window.config(background="#a4ccd2")

        # --------------------- background image -----------------
        from PIL import Image, ImageTk
        self.bimg1 = Image.open("Project_Pics//checkout2.webp")
        self.bimg1 = self.bimg1.resize((300, 300))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.window, image=self.bimg2,background="#a4ccd2")
        self.bimglbl.place(x=650, y=400)
        # ---------widgets-----------

        font1 = ["Candara", 40, "bold"]
        font2 = ["Calibri", 14, "bold"]
        font3 = ["Calibri", 12, ""]
        bg = "#a4ccd2"
        fg = "black"
        self.hd = Label(self.window, text="Check Out", font=font1,
                        foreground="white", background=bg)
        # v1,t2,t3,t4,t5,t6
        self.l1 = Label(self.window, text="Customer Room Number", background=bg,foreground=fg,font=font3)
        self.v1 = StringVar()
        self.c1 = Combobox(self.window, textvariable=self.v1, state="readonly", font=font3)
        self.v1.set("Choose Room number")
        self.c1.bind("<<ComboboxSelected>>", lambda e: self.getCustomerData())

        self.l2=Label(self.window,text="Id Number",foreground=fg, background=bg,font=font3)
        self.t2 = Label(self.window, background=bg)


        self.l8=Label(self.window,text="Name",foreground=fg, background=bg,font=font3)
        self.t8 = Label(self.window, background=bg)

        self.l3=Label(self.window,text="Check in time",foreground=fg, background=bg,font=font3)
        self.t3 = Label(self.window, background=bg, font=["", 9, "bold"])

        self.l4=Label(self.window,text="Check out time",foreground=fg, background=bg,font=font3)
        import time
        var = time.ctime()
        self.t4 = Label(self.window, text=var, background=bg, font=["", 9, "bold"])

        self.l5=Label(self.window,text="Amount Paid",foreground=fg, background=bg,font=font3)
        self.t5 = Label(self.window, background=bg, font=["", 9, "bold"])

        self.l6=Label(self.window,text="Amount Left",foreground=fg, background=bg,font=font3)
        self.t6 = Label(self.window, background=bg, font=["", 9, "bold"])

        self.l7=Label(self.window,text="Pending Amount Payment",foreground=fg, background=bg,font=font3)
        self.t7 = Entry(self.window)

        self.l9 = Label(self.window, text="Give unique customer hotel Id", foreground=fg, background=bg, font=font3)
        self.t9 = Entry(self.window)

        self.imglbl = Label(self.window, relief="groove", borderwidth=1)
        # v1,t2,t8,t3,t4,t5,t6,t7/,t9

        # ---------------BUTTONS-----------------

        self.b1 = Button(self.window, foreground="white", background="black", height=2, width=13, text="Check Out",cursor="hand2"
                         ,command=self.checkOut)
        self.b3 = Button(self.window, foreground="white", background="black", height=2, width=13, text="Clear Page",cursor="hand2"
                         ,command=self.clearPage)
        # self.b2 = Button(self.window, foreground="white", background="black", height=2, width=13, text="Cancel"
        #                  ,command=lambda :Entrypage(self.window))


        # self.b2 = Button(self.window, text="Upload", background="black",cursor="hand2",
        #                  foreground='white',height=2, width=20,command=self.checkOut)

        hcolor = "#464744"
        bg2="black"
        self.b1.bind("<Enter>", lambda e: self.changeColor(hcolor, "b1"))
        self.b1.bind("<Leave>", lambda e: self.changeColor(bg2, "b1"))
        # self.b2.bind("<Enter>", lambda e: self.changeColor(hcolor, "b2"))
        # self.b2.bind("<Leave>", lambda e: self.changeColor(bg2, "b2"))
        self.b3.bind("<Enter>", lambda e: self.changeColor(hcolor, "b3"))
        self.b3.bind("<Leave>", lambda e: self.changeColor(bg2, "b3"))


        #---------------PLacements-------------

        x1 = 200
        y1 = 150
        y1_diff = 50
        x1_diff = 250

        self.hd.place(x=0, y=0, width=w1, height=90)

        self.l1.place(x=x1, y=y1)
        self.c1.place(x=x1 + x1_diff, y=y1, height=25, width=150)
        y1 = y1 + y1_diff

        self.l2.place(x=x1, y=y1)
        self.t2.place(x=x1 + x1_diff, y=y1, height=25, width=150)
        y1 = y1 + y1_diff

        self.l8.place(x=x1, y=y1)
        self.t8.place(x=x1 + x1_diff, y=y1, height=25, width=150)
        y1 = y1 + y1_diff

        self.l3.place(x=x1, y=y1)
        self.t3.place(x=x1 + x1_diff, y=y1, height=25, width=150)
        y1 = y1 + y1_diff

        self.l4.place(x=x1, y=y1)
        self.t4.place(x=x1 + x1_diff, y=y1, height=25, width=150)
        y1 = y1 + y1_diff


        self.l5.place(x=x1, y=y1)
        self.t5.place(x=x1 + x1_diff, y=y1, height=25, width=150)
        y1 = y1 + y1_diff


        self.l6.place(x=x1, y=y1)
        self.t6.place(x=x1 + x1_diff, y=y1, height=25, width=150)
        y1 = y1 + y1_diff

        self.l7.place(x=x1, y=y1)
        self.t7.place(x=x1 + x1_diff, y=y1, height=25, width=150)
        y1 = y1 + y1_diff

        self.l9.place(x=x1, y=y1)
        self.t9.place(x=x1 + x1_diff, y=y1, height=25, width=150)
        y1 = y1 + y1_diff

        self.b1.place(x=x1, y=y1 + 30)
        self.b3.place(x=x1+120, y=y1+30)
        # self.b2.place(x=x1 + 120, y=y1 + 30)

        # self.b2.place(x=x1 + 550, y=300)

        self.imglbl.place(x=x1 + 549.5, y=150, width=150, height=150)

        self.clearPage()
        self.getOccupiedRooms()
        self.window.mainloop()

#         -----------Functions-----------

    def changeColor(self, c, name):
        if name == "b1":
            self.b1.config(background=c)
        elif name == "b2":
            self.b1.config(background=c)


#         --------------Database functions-----------

    def databaseConnection(self):
        myhost="localhost"
        mydb="hotelmgmtdb"
        myuser="root"
        mypassword=""

        try:
            self.conn = pymysql.connect(host=myhost, db=mydb, user=myuser, password=mypassword)
            self.curr = self.conn.cursor()

        except Exception as e:
            messagebox.showerror("Query Error", "Error while connecting with database\n" + str(e), parent=self.window)

    # def getCustomerPendingAmount(self):
    #     self.databaseConnection()
    #     #        ID	ID_ number	Name	Gender	Country	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
    #     try:
    #         myqry2 = "select Price from rooms where RoomNumber=%s"
    #         rowcount2 = self.curr.execute(myqry2, (self.v1.get()))
    #         data2 = self.curr.fetchone()
    #
    #         if data2:
    #             # v1,t2,t3,t4,t5,t6
    #             return data2
    #
    #         else:
    #             messagebox.showinfo("Failure", "No Record Found", parent=self.window)
    #     except Exception as e:
    #         messagebox.showerror("Query Error", "Error while insertion \n" + str(e), parent=self.window)

    def getCustomerData(self):
        self.databaseConnection()
#        ID	ID_number	Name	Gender	PhoneNumber 	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
#         AllocatedRoomNumber	IDNumber	Name	CheckInTime	CheckOutTime	AmountPaid	AmountLeft	PendingAmountPayment
        try:
            myqry="select * from customer where Allocated_Room_Nnumber = %s"
            rowcount=self.curr.execute(myqry,(self.v1.get()))
            data1=self.curr.fetchone()
            # data2= self.getCustomerPendingAmount()

            if data1:
                # v1,t2,t3,t4,t5,t6
                self.t2.config(text=data1[1])
                self.t3.config(text=data1[7])
                self.t5.config(text=str(data1[9]))
                self.t8.config(text=str(data1[2]))
                data3=(int(data1[8]))-(int(data1[9]))
                print(data3)
                self.t6.config(text=str(data3))
                self.actualname = data1[10]
                self.oldname= data1[10]
                self.img1 = Image.open("customer_images//" + self.actualname)
                self.img1 = self.img1.resize((150, 150))

                # converting and adding image to label
                from PIL import ImageTk
                self.img2 = ImageTk.PhotoImage(self.img1)
                self.imglbl.config(image=self.img2)

            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n" + str(e), parent=self.window)



    def getOccupiedRooms(self):
        # RoomNumber	Availability	CleaningStatus	Price	BedType
        self.databaseConnection()
        try:
            myqry = "select RoomNumber from rooms where Availability=%s"
            rowcount = self.curr.execute(myqry, ("Occupied"))
            data = self.curr.fetchall()
            mycomboboxlist = []
            if data:
                for row in data:
                    mycomboboxlist.append(row[0])
            else:
                self.c1.set("No Room Occupied")
            self.c1.config(values=mycomboboxlist)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while checking \n" + str(e), parent=self.window)

    def checkOut(self):
        print("actual",self.actualname)
        print("old",self.oldname)



        self.databaseConnection()
        try:
            print("t7 = ",self.t7.get())
            print("t6 = ",self.t6['text'])
            print("t2 = ",self.t2['text'])
            print("t3 = ",self.t3['text'])
            print("t4 = ",self.t4['text'])
            print("t5 = ",self.t5['text'])
            print("t8 = ",self.t8['text'])
            print("v1 = ",self.v1.get())
            if self.t7.get() == (self.t6['text']):
                myqry="delete from customer where ID_number=%s"
                rowcount1 = self.curr.execute(myqry, (self.t2.cget("text")))

                myqry2 = "update rooms set Availability=%s where RoomNumber=%s"
                rowcount2=self.curr.execute(myqry2,("Available",self.v1.get()))

                # AllocatedRoomNumber	IDNumber	Name	CheckInTime	CheckOutTime	AmountPaid	AmountLeft	PendingAmountPayment	CheckOutCustomerPic	UniqueCustomerHotelID
                myqry3="insert into checkout values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                rowcount3=self.curr.execute(myqry3,(self.v1.get(),self.t2.cget("text"),self.t8.cget("text"),self.t3.cget("text"),
                                                    self.t4.cget("text"),self.t5.cget("text"),self.t6.cget("text")
                                                    ,self.t7.get(),self.actualname,self.t9.get()))

                self.conn.commit()


                if rowcount1==1 and rowcount2==1 and rowcount3==1:
                    messagebox.showinfo("Success", "Checked Out successfully", parent=self.window)
                    # save image
                    if self.actualname == self.default_image:  # no image is selected
                        # nothing to save in folder
                        pass
                    else:
                        self.img1.save("checkout_customer_images//" + self.actualname)

                        import os
                        os.remove("customer_images//" + self.oldname)
                    self.clearPage()

                else:
                    messagebox.showinfo("Failure", "Check all the fields carefully", parent=self.window)

            else:
                messagebox.showinfo("Failure","Please Pay your Pendng dues",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error","Error while Checking Out \n"+str(e),parent=self.window)


    def clearPage(self):
        #  v1,t2,t3,t4,t5,t6
        self.v1.set("Choose Room number")
        self.t2.config(text="")
        self.t3.config(text="")
        import time
        var = time.ctime()
        self.t4.config(text=var)
        self.t5.config(text="")
        self.t6.config(text="")
        self.t8.config(text="")
        self.t7.delete(0,END)
        self.t9.delete(0,END)
        self.getOccupiedRooms()
        self.actualname = self.default_image
        self.img1 = Image.open("checkout_customer_images//" + self.actualname)
        self.img1 = self.img1.resize((150, 150))
        self.img2 = ImageTk.PhotoImage(self.img1)
        self.imglbl.config(image=self.img2)

    def validate_check(self):
        # v1,t2,t8,t3,t4,t5,t6,t7
        if (self.v1.get() == "Choose Room Number") or (self.v1.get() == "No Room Number"):
            messagebox.showwarning("Validation Check", "Enter Alloted room number of the customer", parent=self.window)
            return False

        elif (self.t2.cget("text")==""):
            messagebox.showwarning("Validation Check", "ID number of customer is not there check properly", parent=self.window)
            return False

        elif (self.t8.cget("text")==""):
            messagebox.showwarning("Validation Check", "Name of the customer is not there check properly", parent=self.window)
            return False

        elif (self.t3.cget("text")==""):
            messagebox.showwarning("Validation Check", "Check in time is not there check properly", parent=self.window)
            return False

        elif (self.t4.cget("text")==""):
            messagebox.showwarning("Validation Check", "Check out time is not there check properly", parent=self.window)
            return False

        elif (self.t5.cget("text") == "" or len(self.t5.cget("text")) < 0):
            messagebox.showwarning("Validation Check", "Amount Paid is not correct check properly the pending dues",
                                   parent=self.window)
            return False

        elif (self.t6.cget("text") == "" or len(self.t6.cget("text")) < 0):
            messagebox.showwarning("Validation Check", "Amount Left is not correct check properly the pending dues",
                                   parent=self.window)
            return False

        elif (self.t7.get() == "" or len(self.t7.get()) < 0):
            messagebox.showwarning("Validation Check", "Amount Pending is not correct check properly the pending dues",
                                   parent=self.window)
            return False


        elif (int(self.t9.get()) < 0):
            messagebox.showwarning("Validation Check", "Please enter correct hotel customer id",
                                   parent=self.window)
            return False
        return True


if __name__ == '__main__':
    dummy_customer_form = Tk()
    CheckOut(dummy_customer_form)
    dummy_customer_form.mainloop()





