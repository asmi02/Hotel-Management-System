from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql

from employee_printout import my_cust_PDF


class employee_report:
    def __init__(self,hwindow):
        self.hwindow=hwindow

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
        self.window.config(background="#f79d6e")

        # ---------widgets-----------


        font1=["Candara",40,"bold"]
        font2=["Calibri",14,"bold"]
        font3=["Calibri",12,""]
        bg="#f79d6e"
        fg="white"
        self.hd=Label(self.window,text="Employee Details",font=font1,
                      foreground=fg,background=bg)

        # --------------- buttons ----------------------------------
        self.b1 = Button(self.window, text="Print", background="black",
                         foreground='white', command=self.getPrintout)

        hcolor = "#464744"
        bg2 = "black"
        self.b1.bind("<Enter>", lambda e: self.changeColor(hcolor, "b1"))
        self.b1.bind("<Leave>", lambda e: self.changeColor(bg2, "b1"))



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
        self.mytable.bind("<ButtonRelease>",lambda e: self.getSelectedRowData())
        # -----------------PLACEMENTS-----------------
        x1 = 150
        y1 = 150
        y1_diff = 50
        x1_diff = 200

        self.hd.place(x=30, y=0, width=w1, height=90)
        self.tablearea.place(x=x1,y=y1)
        self.b1.place(x=600, y=y1 + 400, width=100, height=50)

        self.fetchAllData()
        self.window,mainloop()

#         -----------Hover effect----------

    def changeColor(self,c,name):
        if name=="b1":
            self.b1.config(background=c)


#         ----------Printout---------

    def getPrintout(self):
        pdf = my_cust_PDF()
        headings = ['Name','DOB','Gender','Job','Salary','Phone','Aadhar','Email']
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
        # Name DOB Gender Job Salary	Phone Aadhar Email
        try:
            myqry="select * from employee"
            rowcount=self.curr.execute(myqry)
            data = self.curr.fetchall()
            self.mypdata = []
            if data:
                for row in data:
                    self.mypdata.append(row[:-1])
                    self.mytable.insert("", END, values=row)

            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n"
                                 + str(e), parent=self.window)
    def getSelectedRowData(self):
        id = self.mytable.focus()
        # print("id = ",id)
        data = self.mytable.item(id)
        # print("data = ",data)
        content = data['values']
        # print("Content = ",content)
        col1 = content[6]
        print("col = ",col1)
        self.window.destroy()
        from add_employee import add_employee
        add_employee(self.hwindow,col1)


if __name__=='__main__':
    dummy_employee_report=Tk()
    employee_report(dummy_employee_report)
    dummy_employee_report.mainloop()