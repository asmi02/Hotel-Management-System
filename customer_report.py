from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview, Combobox
# from add_employee import add_employee
import pymysql

# from add_employee import add_employee
from add_room import add_room
from customer_printout import my_cust_PDF


class customer_report:
    def __init__(self,hwindow):
        self.hwindow=hwindow
        # self.window = Tk()
        self.window=Toplevel(hwindow)
        self.window.title("Customer Details")
        # --------Window settings-----
        h = self.window.winfo_screenwidth()
        w = self.window.winfo_screenheight()

        w1 = 1500
        h1 = 760
        self.window.minsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 20, 20))
        # self.window.state("zoomed")
        self.window.config(background="#cbf6f4")

        # ---------widgets-----------


        font1=["Candara",40,"bold"]
        font2=["Calibri",14,"bold"]
        font3=["Calibri",12,""]
        bg="#cbf6f4"
        fg="white"
        self.hd=Label(self.window,text="Customer Details",font=font1,
                      foreground=fg,background=bg)

        self.v1 = StringVar()
        self.c1 = Combobox(self.window, textvariable=self.v1)
        self.c1.bind("<<ComboboxSelected>>", lambda e: self.fetchAllottedRoomData())
        self.v1.set("Choose Room Number")

        self.v2 = StringVar()
        self.c2 = Combobox(self.window, textvariable=self.v2, values=["Passport","Voter Id","Driving License","Aadhar"])
        self.c2.bind("<<ComboboxSelected>>", lambda e: self.fetchIDData())
        self.v2.set("Choose ID")

        self.v3 = StringVar()
        self.c3 = Combobox(self.window, textvariable=self.v3, values=['Single Bed', 'Double Bed'])
        self.c3.bind("<<ComboboxSelected>>", lambda e: self.fetchRoomTypeData())
        self.v3.set("Choose Room Type")

        self.v4 = StringVar()
        self.r1 = Radiobutton(self.window, text="Male", value="Male", variable=self.v4, background=bg,command=self.fetchGenderData)
        self.r2 = Radiobutton(self.window, text="Female", value="Female", variable=self.v4, background=bg,command=self.fetchGenderData)
        self.v4.set(None)

        # -----------BUTTONS-----------
        self.b1 = Button(self.window, text="Print", background="black",
                         foreground='white', command=self.getPrintout)
        self.b5 = Button(self.window, foreground="white", background="black", height=2, width=13, text="All Data"
                         , command=self.fetchAllData, cursor="hand2")

        hcolor = "#464744"
        bg2 = "black"
        self.b1.bind("<Enter>", lambda e: self.changeColor(hcolor, "b1"))
        self.b1.bind("<Leave>", lambda e: self.changeColor(bg2, "b1"))
        self.b5.bind("<Enter>", lambda e: self.changeColor(hcolor, "b5"))
        self.b5.bind("<Leave>", lambda e: self.changeColor(bg2, "b5"))

        #         ---------Creating table------
        # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        self.tablearea = Frame(self.window)
        self.mytable = Treeview(self.tablearea, columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9','c10','c11'])
        self.mytable.heading("c1", text="ID")
        self.mytable.heading("c2", text="ID_number")
        self.mytable.heading("c3", text="Name")
        self.mytable.heading("c4", text="Gender")
        self.mytable.heading("c5", text="Phone Number")
        self.mytable.heading("c6", text="Room Type")
        self.mytable.heading("c7", text="Room Number")
        self.mytable.heading("c8", text="Check in time")
        self.mytable.heading("c9", text="Price")
        self.mytable.heading("c10", text="Amount Deposited")
        self.mytable.heading("c11", text="Customer Pic")
        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=50, anchor='center')
        self.mytable.column("#2", width=100, anchor='center')
        self.mytable.column("#3", width=100, anchor='center')
        self.mytable.column("#4", width=100, anchor='center')
        self.mytable.column("#5", width=100, anchor='center')
        self.mytable.column("#6", width=100, anchor='center')
        self.mytable.column("#7", width=100, anchor='center')
        self.mytable.column("#8", width=200, anchor='center')
        self.mytable.column("#9", width=50, anchor='center')
        self.mytable.column("#10", width=120, anchor='center')
        self.mytable.column("#11", width=120, anchor='center')
        self.mytable.pack()
        self.mytable.bind("<ButtonRelease>", lambda e: self.getSelectedRowData())





        # -----------------PLACEMENTS-----------------
        x1 = 10
        y1 = 150
        y1_diff = 100
        x1_diff = 250

        self.hd.place(x=30, y=0, width=w1, height=90)

        self.c1.place(x=x1 + 70, y=y1)
        self.c2.place(x=x1 + 250, y=y1)
        self.c3.place(x=x1 + 430, y=y1)
        self.r1.place(x=x1 + 600, y=y1)
        self.r2.place(x=x1 + 700, y=y1)
        self.b5.place(x=x1+850,y=y1)

        self.tablearea.place(x=130, y=300)
        self.b1.place(x=600, y=y1 + 400, width=100, height=50)

        self.fetchAllData()
        self.getAvailableRooms()
        self.window, mainloop()

        #         -----------Functions-----------

    def changeColor(self, c, name):
        if name == "b5":
            self.b5.config(background=c)
        if name == "b1":
            self.b1.config(background=c)

#     ---------Printout---------
    def getPrintout(self):
        pdf = my_cust_PDF()
        headings = ['ID Number','Name','Gender','Phone No','Room','Price','Deposit']
        pdf.print_chapter(self.mypdata,headings)

        pdf.output('pdf_file1.pdf')
        import os
        os.system('explorer.exe "pdf_file1.pdf"')

#         ------fetching data and making connection with the database----

    def databaseConnection(self):
        myhost="localhost"
        mydb="hotelmgmtdb"
        myuser="root"
        mypassword=""
        try:
            self.conn=pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr=self.conn.cursor()

        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting database \n"
                                 +str(e),parent=self.window)

    def fetchAllData(self):
        self.databaseConnection()
        # ID	ID_ number	Name	Gender	Phone Number	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit CustomerPic
        try:
            myqry="select * from customer"
            self.mytable.delete(*self.mytable.get_children())
            rowcount=self.curr.execute(myqry)
            data = self.curr.fetchall()
            self.mypdata = []
            if data:
                for row in data:
                    r1 = [row[1],row[2],row[3],row[4],row[6],row[8],row[9]]
                    self.mypdata.append(r1)
                    self.mytable.insert("", END, values=row)

            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n"
                                 + str(e), parent=self.window)

    def getSelectedRowData(self):
        # ID	ID_ number	Name	Gender	Phone Number	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        id = self.mytable.focus()
        # print("id = ",id)
        data = self.mytable.item(id)
        # print("data = ",data)
        content = data['values']
        # print("Content = ",content)
        col1 = content[1]
        print("col = ", col1)
        self.window.destroy()
        from add_employee import add_employee
        from customer_form import customer_form
        customer_form(self.hwindow, col1)

    # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit

    def fetchAllottedRoomData(self):
        # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        self.databaseConnection()
        try:
            self.mytable.delete(*self.mytable.get_children())
            myqry = "select * from customer where Allocated_Room_Nnumber=%s"
            rowcount = self.curr.execute(myqry,(self.v1.get()))
            data = self.curr.fetchall()
            if data:
                # print(data)
                for row in data:
                    self.mytable.insert("",END,values=row)
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window)


    def fetchGenderData(self):
        # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        self.databaseConnection()
        try:
            self.mytable.delete(*self.mytable.get_children())
            myqry = "select * from customer where Gender=%s"
            rowcount = self.curr.execute(myqry,(self.v4.get()))
            data = self.curr.fetchall()
            if data:
                # print(data)
                for row in data:
                    self.mytable.insert("",END,values=row)
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window)


    def fetchIDData(self):
        # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        self.databaseConnection()
        try:
            self.mytable.delete(*self.mytable.get_children())
            myqry = "select * from customer where ID=%s"
            rowcount = self.curr.execute(myqry,(self.v2.get()))
            data = self.curr.fetchall()
            if data:
                # print(data)
                for row in data:
                    self.mytable.insert("",END,values=row)
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window)


    def fetchRoomTypeData(self):
        # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        self.databaseConnection()
        try:
            self.mytable.delete(*self.mytable.get_children())
            myqry = "select * from customer where Room_Type=%s"
            rowcount = self.curr.execute(myqry,(self.v3.get()))
            data = self.curr.fetchall()
            if data:
                # print(data)
                for row in data:
                    self.mytable.insert("",END,values=row)
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window)


    def getAvailableRooms(self):
        #  ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
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


# if __name__=='__main__':
#     dummy_employee_report=Tk()
#     customer_report(dummy_employee_report)
#     dummy_employee_report.mainloop()