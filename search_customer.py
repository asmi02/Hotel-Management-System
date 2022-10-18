from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql

class search_customer:
    def __init__(self,hwindow,t1):
        self.hwindow = hwindow
        print("---------- t1 = ",t1,"==============")

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
        self.window.config(background="#c28cf5")

        # ---------widgets-----------


        font1=["Candara",40,"bold"]
        font2=["Calibri",14,"bold"]
        font3=["Calibri",12,""]
        bg="#c28cf5"
        fg="white"
        self.hd=Label(self.window,text="Customer Details",font=font1,
                      foreground=fg,background=bg)


        #         ---------Creating table------
        # ID	ID_ number	Name	Gender	Phone Number	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        self.tablearea = Frame(self.window)
        self.mytable = Treeview(self.tablearea, columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9','c10','c11'])
        self.mytable.heading("c1", text="ID")
        self.mytable.heading("c2", text="ID_number")
        self.mytable.heading("c3", text="Name")
        self.mytable.heading("c4", text="Gender")
        self.mytable.heading("c5", text="Phone Number")
        self.mytable.heading("c6", text="Room Type")
        self.mytable.heading("c7", text="Allocated Room Number")
        self.mytable.heading("c8", text="Check in time")
        self.mytable.heading("c9", text="Price")
        self.mytable.heading("c10", text="Amount Deposited")
        self.mytable.heading("c11", text="Profile Pic")
        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=150, anchor='center')
        self.mytable.column("#2", width=100, anchor='center')
        self.mytable.column("#3", width=100, anchor='center')
        self.mytable.column("#4", width=100, anchor='center')
        self.mytable.column("#5", width=100, anchor='center')
        self.mytable.column("#6", width=150, anchor='center')
        self.mytable.column("#7", width=150, anchor='center')
        self.mytable.column("#8", width=150, anchor='center')
        self.mytable.column("#9", width=150, anchor='center')
        self.mytable.column("#9", width=150, anchor='center')
        self.mytable.column("#10", width=150, anchor='center')
        self.mytable.column("#11", width=150, anchor='center')
        self.mytable.pack()
        self.mytable.bind("<ButtonRelease>", lambda e: self.getSelectedRowData())

        # -----------------PLACEMENTS-----------------
        x1 = 150
        y1 = 150
        y1_diff = 50
        x1_diff = 200

        self.hd.place(x=30, y=0, width=w1, height=90)
        self.tablearea.place(x=30,y=y1)

        self.fetchAllData(t1)
        self.window,mainloop()

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

    def fetchAllData(self,t1):

        print("2.---------- t1 = ",t1,"==============")
        self.databaseConnection()
        # ID	ID_ number	Name	Gender	Phone Number	Room_Type	Allocated_Room_Nnumber	Check_in_time	Amount_to_pay	Deposit
        try:
            myqry="select * from customer where Name like %s"
            rowcount=self.curr.execute(myqry,(t1+"%"))
            data = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            print(data)
            if data:
                for row in data:
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
        from add_room import add_room
        from customer_form import customer_form
        customer_form(self.hwindow, col1)


# if __name__=='__main__':
#     dummy_employee_search=Tk()
#     # employee_search(dummy_employee_search)
#     dummy_employee_search.mainloop()

#fn ke ander class name and then provide data