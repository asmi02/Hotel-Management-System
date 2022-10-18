from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview, Combobox
import pymysql

from add_room import add_room


class dynamic_room_search:
    def __init__(self,hwindow):
        self.hwindow = hwindow
        self.window=Toplevel(hwindow)
        #--------------- settings ----------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1=w-100
        h1=h-180
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,50,80))
        self.window.title("Dynamic Room Search")
        #-------------- widgets -----------------------------------
        self.headlbl = Label(self.window,text="Room Search",font=("CentSchbkCyrill BT",40,"bold"))
        mycolor1="white"
        myfont1 = ("CentSchbkCyrill BT",10,"bold")



        self.v1=StringVar()
        self.c1 = Combobox(self.window,textvariable=self.v1,values=['Available','Occupied'])
        self.c1.bind("<<ComboboxSelected>>",lambda e: self.fetchAvailabilityData())
        self.v1.set("Choose Availability")

        self.v2 = StringVar()
        self.c2 = Combobox(self.window, textvariable=self.v2, values=['Clean', 'Uncleaned'])
        self.c2.bind("<<ComboboxSelected>>", lambda e: self.fetchStatusData())
        self.v2.set("Choose Cleaning Status")

        self.v3 = StringVar()
        self.c3 = Combobox(self.window, textvariable=self.v3, values=['Single Bed', 'Double Bed'])
        self.c3.bind("<<ComboboxSelected>>", lambda e: self.fetchBedTypeData())
        self.v3.set("Choose Bed Type")



        #------------------ table ---------------------------------------
        self.tablearea = Frame(self.window)
        self.mytable = Treeview(self.tablearea,columns=['c1','c2','c3','c4','c5'])
        self.mytable.heading("c1",text="Room Number")
        self.mytable.heading("c2",text="Availability")
        self.mytable.heading("c3",text="Cleaning Status")
        self.mytable.heading("c4",text="Price")
        self.mytable.heading("c5",text="Bed Type")
        self.mytable['show']='headings'     #TO REMOVE EXTRA COLUMN

        self.mytable.column("#1",width=100,anchor='n')
        self.mytable.column("#2",width=200,anchor='e')
        self.mytable.column("#3",width=200,anchor='s')
        self.mytable.column("#4",width=100,anchor='w')
        self.mytable.column("#5",width=100,anchor='center')
        self.mytable.pack()
        self.mytable.bind("<ButtonRelease>", lambda e: self.getSelectedRowData())

        #--------------- buttons ----------------------------------
        # self.b1 = Button(self.window,text="Save",background="#8C2AFA",foreground='white',command=self.saveData)
        #--------- placements ------------------------------------------------

        self.headlbl.place(x=0,y=0,width=w1,height=90)
        x1=10
        y1=100
        x_diff=100
        y_diff=50
        self.c1.place(x=x1+70,y=y1)
        self.c2.place(x=x1+250,y=y1)
        self.c3.place(x=x1+430,y=y1)
        self.tablearea.place(x=x1+70,y=y1+50)
        # self.getAvailableRooms()
        self.window.mainloop()
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

    def fetchAvailabilityData(self):
        # RoomNumber	Availability	CleaningStatus	Price	BedType
        self.databaseConnection()
        try:
            self.mytable.delete(*self.mytable.get_children())
            myqry = "select * from rooms where Availability=%s"
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


    def fetchStatusData(self):
        # RoomNumber	Availability	CleaningStatus	Price	BedType
        self.databaseConnection()
        try:
            self.mytable.delete(*self.mytable.get_children())
            myqry = "select * from rooms where CleaningStatus=%s"
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


    def fetchBedTypeData(self):
        # RoomNumber	Availability	CleaningStatus	Price	BedType
        self.databaseConnection()
        try:
            self.mytable.delete(*self.mytable.get_children())
            myqry = "select * from rooms where BedType=%s"
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

    # def getAvailableRooms(self):
    #     # RoomNumber	Availability	CleaningStatus	Price	BedType
    #     self.databaseConnection()
    #     try:
    #         myqry = "select RoomNumber from rooms where Availability=%s"
    #         rowcount = self.curr.execute(myqry, ("Available"))
    #         data = self.curr.fetchall()
    #         mycomboboxlist = []
    #         if data:
    #             for row in data:
    #                 mycomboboxlist.append(row[0])
    #         else:
    #             self.c1.set("No Room Available")
    #         self.c1.config(values=mycomboboxlist)
    #     except Exception as e:
    #         messagebox.showerror("Query Error", "Error while checking \n" + str(e), parent=self.window)

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
        add_room(self.hwindow, col1)

# if __name__ == '__main__':
#     dummy_homepage=Tk()
#     dynamic_room_search(dummy_homepage)
#     dummy_homepage.mainloop()