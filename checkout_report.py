from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview, Combobox
# from add_employee import add_employee
import pymysql

# from add_employee import add_employee
from add_room import add_room
from checkout_printout import my_cust_PDF


class checkout_report:
    def __init__(self,hwindow):
        self.hwindow=hwindow
        # self.window = Tk()
        self.window=Toplevel(hwindow)
        self.window.title("Checkout Details")
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
        self.hd=Label(self.window,text="Checked Out Customer Details",font=font1,
                      foreground=fg,background=bg)

        # -----------BUTTONS-----------
        self.b1 = Button(self.window, text="Print", background="black",
                         foreground='white', command=self.getPrintout)

        hcolor = "#464744"
        bg2 = "black"
        self.b1.bind("<Enter>", lambda e: self.changeColor(hcolor, "b1"))
        self.b1.bind("<Leave>", lambda e: self.changeColor(bg2, "b1"))

        #         ---------Creating table------
        # ID	ID_ number	Name	Gender	PhoneNumber	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        # UniqueCustomerHotelID
        self.tablearea = Frame(self.window)
        self.mytable = Treeview(self.tablearea, columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9','c10'])
        self.mytable.heading("c1", text="Room Number")
        self.mytable.heading("c2", text="ID_number")
        self.mytable.heading("c3", text="Name")
        self.mytable.heading("c4", text="check in time")
        self.mytable.heading("c5", text="Check out time")
        self.mytable.heading("c6", text="Amount Paid")
        self.mytable.heading("c7", text="Amount Left")
        self.mytable.heading("c8", text="Pending amount Payment")
        self.mytable.heading("c9", text="Customer Pic")
        self.mytable.heading("c10", text="Hotel Customer ID")
        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=100, anchor='center')
        self.mytable.column("#2", width=100, anchor='center')
        self.mytable.column("#3", width=100, anchor='center')
        self.mytable.column("#4", width=200, anchor='center')
        self.mytable.column("#5", width=200, anchor='center')
        self.mytable.column("#6", width=90, anchor='center')
        self.mytable.column("#7", width=90, anchor='center')
        self.mytable.column("#8", width=200, anchor='center')
        self.mytable.column("#9", width=200, anchor='center')
        self.mytable.column("#10", width=150, anchor='center')
        self.mytable.pack()





        # -----------------PLACEMENTS-----------------
        x1 = 10
        y1 = 150
        y1_diff = 100
        x1_diff = 250

        self.hd.place(x=30, y=0, width=w1, height=90)


        self.tablearea.place(x=30, y=300)
        self.b1.place(x=600, y=y1 + 400, width=100, height=50)

        self.fetchAllData()
        self.window, mainloop()

        #         -----------Functions-----------

    def changeColor(self, c, name):
        if name == "b1":
            self.b1.config(background=c)

#     ---------Printout---------
    def getPrintout(self):
        pdf = my_cust_PDF()
        headings = ['Room No','ID Number','Name','Amount Paid','Amount Left','Pending Dues']
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
        # ID	ID_ number	Name	Gender	Phone Number	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay
        # Deposit CustomerPic UniqueCustomerHotelID
        try:
            myqry="select * from checkout"
            self.mytable.delete(*self.mytable.get_children())
            rowcount=self.curr.execute(myqry)
            data = self.curr.fetchall()
            self.mypdata = []
            if data:
                for row in data:
                    r1 = [row[0],row[1],row[2],row[5],row[6],row[7]]
                    self.mypdata.append(r1)
                    self.mytable.insert("", END, values=row)

            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n"
                                 + str(e), parent=self.window)


# if __name__=='__main__':
#     dummy_employee_report=Tk()
#     checkout_report(dummy_employee_report)
#     dummy_employee_report.mainloop()