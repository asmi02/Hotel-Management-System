from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql

class employee_search:
    def __init__(self,hwindow,t1):
        print("---------- t1 = ",t1,"==============")

        # self.window = Tk()
        self.window=Toplevel(hwindow)
        self.window.title("Employee Details")
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
        self.hd=Label(self.window,text="Employee Details",font=font1,
                      foreground=fg,background=bg)


        #         ---------Creating table------
        # Name DOB Gender Job Salary Phone Aadhar Email
        self.tablearea=Frame(self.window)
        self.mytable=Treeview(self.tablearea,columns=['c1','c2','c3','c4','c5','c6','c7','c8'])
        self.mytable.heading("c1",text="Name")
        self.mytable.heading("c2",text="DOB")
        self.mytable.heading("c3",text="Gender")
        self.mytable.heading("c4",text="Job")
        self.mytable.heading("c5",text="Salary")
        self.mytable.heading("c6",text="Phone")
        self.mytable.heading("c7",text="Aadhar")
        self.mytable.heading("c8",text="Email")
        self.mytable['show'] = 'headings'

        self.mytable.column("#1",width=150,anchor='center')
        self.mytable.column("#2",width=100,anchor='center')
        self.mytable.column("#3",width=100,anchor='center')
        self.mytable.column("#4",width=100,anchor='center')
        self.mytable.column("#5",width=100,anchor='center')
        self.mytable.column("#6",width=100,anchor='center')
        self.mytable.column("#7",width=150,anchor='center')
        self.mytable.column("#8",width=200,anchor='center')
        self.mytable.pack()

        # -----------------PLACEMENTS-----------------
        x1 = 150
        y1 = 150
        y1_diff = 50
        x1_diff = 200

        self.hd.place(x=30, y=0, width=w1, height=90)
        self.tablearea.place(x=x1,y=y1)

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
        # Name DOB Gender Job Salary Phone Aadhar Email
        try:
            myqry="select * from employee where Name like %s"
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


# if __name__=='__main__':
#     dummy_employee_search=Tk()
#     employee_search(dummy_employee_search)
#     dummy_employee_search.mainloop()

# fn ke ander class name and then provide data