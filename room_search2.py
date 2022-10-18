from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql

class room_search2:
    def __init__(self,hwindow,t1):
        self.hwindow = hwindow
        # self.window = Tk()
        self.window=Toplevel(hwindow)
        self.window.title("Room Details")
        # --------Window settings-----
        h = self.window.winfo_screenwidth()
        w = self.window.winfo_screenheight()

        w1 = 1500
        h1 = 760
        self.window.minsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 20, 20))
        # self.window.state("zoomed")
        self.window.config(background="#91f884")

        # ---------widgets-----------


        font1=["Candara",40,"bold"]
        font2=["Calibri",14,"bold"]
        font3=["Calibri",12,""]
        bg="#91f884"
        fg="white"
        self.hd=Label(self.window,text="Room Details Details",font=font1,
                      foreground=fg,background=bg)


        #         ---------Creating table------
        # Room Number	Availablity	Cleaning Status	Price	Bed Type
        self.tablearea=Frame(self.window)
        self.mytable=Treeview(self.tablearea,columns=['c1','c2','c3','c4','c5'])
        self.mytable.heading("c1",text="Room Number")
        self.mytable.heading("c2",text="Availability")
        self.mytable.heading("c3",text="Cleaning Status")
        self.mytable.heading("c4",text="Price")
        self.mytable.heading("c5",text="Bed Type")
        self.mytable['show'] = 'headings'

        self.mytable.column("#1",width=150,anchor='center')
        self.mytable.column("#2",width=100,anchor='center')
        self.mytable.column("#3",width=100,anchor='center')
        self.mytable.column("#4",width=100,anchor='center')
        self.mytable.column("#5",width=100,anchor='center')
        self.mytable.pack()
        self.mytable.bind("<ButtonRelease>", lambda e: self.getSelectedRowData())

        # -----------------PLACEMENTS-----------------
        x1 = 450
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

    def fetchAllData(self,v1):
        self.databaseConnection()
        # RoomNumber    Availablity	CleaningStatus  	Price	   BedType
        try:
            myqry="select * from rooms where CleaningStatus like %s"
            rowcount=self.curr.execute(myqry,(v1+"%"))
            data = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            if data:
                for row in data:
                    self.mytable.insert("", END, values=row)

            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n"
                                 + str(e), parent=self.window)

    def getSelectedRowData(self):
        # RoomNumber	Availablity	CleaningStatus	Price	BedType
        id = self.mytable.focus()
        # print("id = ",id)
        data = self.mytable.item(id)
        # print("data = ",data)
        content = data['values']
        # print("Content = ",content)
        col1 = content[0]
        print("col = ", col1)
        self.window.destroy()
        from add_employee import add_employee
        from add_room import add_room
        add_room(self.hwindow, col1)

# if __name__=='__main__':
#     dummy_employee_search=Tk()
#     # employee_search(dummy_employee_search)
#     dummy_employee_search.mainloop()