from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


from room_search import room_search
from room_search2 import room_search2
import pymysql


class UpdateRoom:
    def __init__(self,hwindow):
        # self.window = Tk()
        self.window = Toplevel(hwindow)
        self.window.title("Update Room details")
        # --------Window settings-----
        h = self.window.winfo_screenwidth()
        w = self.window.winfo_screenheight()

        w1 = 1000
        h1 = 760
        self.window.minsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 300, 20))
        # self.window.state("zoomed")
        self.window.config(background="#f9fbce")

        #--------------Add room details form-------
        font1=["Candara",35,"bold"]
        font2 = ["Calibri", 14, "bold"]
        font3 = ["Calibri", 12, ""]
        bg="#f9fbce"
        self.hd=Label(self.window,text="UPDATE ROOMS"
                      ,font=font1,foreground="white",background=bg)
        self.l1=Label(self.window,text="Room Number",background=bg,font=font2)
        self.t1=Entry(self.window)
        self.l4=Label(self.window,text="Choose Available",background=bg,font=font2)
        self.v1=StringVar()
        self.c1=Combobox(self.window,values=["Available"]
                         ,textvariable=self.v1,state="readonly",font=font3)
        self.v1.set("Availability")
        self.l5 = Label(self.window, text="Cleaning Status",background=bg,font=font2)
        self.v2=StringVar()
        self.c2=Combobox(self.window,values=["Clean","Uncleaned"]
                         ,textvariable=self.v2,state="readonly",font=font3)
        self.v2.set("Cleaning Status")
        self.l6 = Label(self.window, text="Price",background=bg,font=font2)
        self.t6 = Entry(self.window)
        self.l7 = Label(self.window, text="Bed Type",background=bg,font=font2)
        self.v3=StringVar()
        self.c3=Combobox(self.window,values=["Single Bed","Double Bed"],
                         textvariable=self.v3,state="readonly",font=font3)
        self.v3.set("Bed Type")

        #--------------------BUTTONS---------------


        # self.b2=Button(self.window,foreground="white",background="black",height=2,width=11,text="Cancel"
        #                ,command=lambda :Entrypage(self.window))

        self.b3 = Button(self.window, foreground="white", background="black", height=2,
                         width=13, text="Clear Data"
                         , command=self.clearPage)

        self.b4 = Button(self.window, foreground="white", background="black",
                         text="get particular record"
                         , command=self.fetchData)



        self.b7 = Button(self.window, foreground="white", background="black", text="Update Data"
                         , height=2, width=13,command= self.updateData)





        hcolor = "#464744"
        bg2="black"
        self.b3.bind("<Enter>", lambda e: self.changeColor(hcolor, "b3"))
        self.b3.bind("<Leave>", lambda e: self.changeColor(bg2, "b3"))
        self.b4.bind("<Enter>", lambda e: self.changeColor(hcolor, "b4"))
        self.b4.bind("<Leave>", lambda e: self.changeColor(bg2, "b4"))
        self.b7.bind("<Enter>", lambda e: self.changeColor(hcolor, "b7"))
        self.b7.bind("<Leave>", lambda e: self.changeColor(bg2, "b7"))



        #---------------PLACEMENTS---------------
        x1 = 100
        y1 = 150
        y1_diff = 50
        x1_diff = 170

        self.hd.place(x=0,y=0,width=w1,height=90)

        self.l1.place(x=x1, y=y1)
        self.t1.place(x=x1+x1_diff,y=y1+5,height=25,width=150)

        self.b4.place(x=x1_diff+x1_diff+110, y=y1+5)
        y1 = y1 + y1_diff

        self.l4.place(x=x1, y=y1)
        self.c1.place(x=x1+x1_diff,y=y1+5,height=25,width=150)

        y1 = y1 + y1_diff

        self.l5.place(x=x1, y=y1)
        self.c2.place(x=x1+x1_diff,y=y1+5,height=25,width=150)

        y1 = y1 + y1_diff

        self.l6.place(x=x1, y=y1)
        self.t6.place(x=x1+x1_diff,y=y1+5,height=25,width=150)
        y1 = y1 + y1_diff

        self.l7.place(x=x1, y=y1)
        self.c3.place(x=x1+x1_diff,y=y1+5,height=25,width=150)
        y1 = y1 + y1_diff

        # self.b2.place(x=x1+100, y=y1+30)
        self.b3.place(x=x1+120, y=y1+30)
        self.b7.place(x=x1, y=y1+30)

        self.clearPage()
        self.window.mainloop()


    #     --------------Functions--------------

    def changeColor(self,c,name):
        if name=="b4":
            self.b4.config(background=c)
        elif name=="b7":
            self.b7.config(background=c)
        elif name=="b3":
            self.b3.config(background=c)

    #   STEP 1: MAKE DATABASE CONNECTION
    def databaseConnection(self):
        myhost = "localhost"
        mydb = "hotelmgmtdb"
        myuser = "root"
        mypassword = ""
        try:
            self.conn = pymysql.connect(host=myhost, db=mydb, user=myuser, password=mypassword)
            self.curr = self.conn.cursor()

        except Exception as e:
            messagebox.showerror("Database Error", "Error while connecting database \n" + str(e), parent=self.window)


        # STEP 3:  FETCH DATA
        # RoomNumber	Availablity	CleaningStatus	Price	BedType
    def fetchData(self, value=None):
        if value == None:
            Room_no = self.t1.get()
        else:
            Room_no = value
        self.databaseConnection()
        # RoomNumber	Availability	CleaningStatus	Price	BedType
        try:
            myqry = "select * from rooms where RoomNumber=%s"
            rowcount = self.curr.execute(myqry, (Room_no))
            data = self.curr.fetchone()
            self.clearPage()

            if data:
                self.t1.insert(0, data[0])
                self.c1.set(data[1])
                self.c2.set(data[2])
                self.t6.insert(0,data[3])
                self.c3.set(data[4])

                self.b7['state'] = 'normal'

            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n" + str(e), parent=self.window)

    # STEP4:UPDATE DATA
    def updateData(self):
        self.databaseConnection()
        # RoomNumber	Availability	CleaningStatus	Price	BedType
        try:
            myqry = "update rooms set Availability=%s, CleaningStatus=%s,Price=%s, BedType=%s where RoomNumber=%s"
            rowcount = self.curr.execute(myqry,(self.c1.get(), self.c2.get(), self.t6.get(),
                                                self.c3.get(), self.t1.get()))
            self.conn.commit()

            if rowcount == 1:
                messagebox.showinfo("Success", "Room Data Updated successfully", parent=self.window)
                self.clearPage()

            else:
                messagebox.showinfo("Failure", "Check all the fields carefully", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Error while updation \n" + str(e), parent=self.window)


    def clearPage(self):
        # Name DOB Gender Job Salary Phone Aadhar Email
        self.t1.delete(0,END)
        self.v1.set("Choose Availability")
        self.v2.set("Cleaning Status")
        self.t6.delete(0,END)
        self.v3.set("Bed Type")

        self.b7['state']='disabled'

if __name__=='__main__':
    dummy_employee_page=Tk()
    UpdateRoom(dummy_employee_page)
    dummy_employee_page.mainloop()