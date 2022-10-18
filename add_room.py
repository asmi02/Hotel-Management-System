from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


from room_search import room_search
from room_search2 import room_search2
import pymysql


class add_room:
    def __init__(self,hwindow,col=None):
        # self.window = Tk()
        self.window = Toplevel(hwindow)
        self.window.title("Add Room details")
        # --------Window settings-----
        h = self.window.winfo_screenwidth()
        w = self.window.winfo_screenheight()

        w1 = 1000
        h1 = 760
        self.window.minsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 300, 20))
        # self.window.state("zoomed")
        self.window.config(background="#f9fbce")

        # --------------------- background image -----------------
        from PIL import Image, ImageTk
        self.bimg1 = Image.open("Project_Pics//add_room.jpg")
        self.bimg1 = self.bimg1.resize((h, w))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.window, image=self.bimg2)
        self.bimglbl.place(x=0, y=0)

        #--------------Add room details form-------
        font1=["Candara",35,"bold"]
        font2 = ["Calibri", 14, "bold"]
        font3 = ["Calibri", 12, ""]
        bg="#f9fbce"
        self.hd=Label(self.window,text="Rooms (ADD , DELETE , GET INFO , UPDATE)"
                      ,font=font1,foreground="black",background=bg)
        self.l1=Label(self.window,text="Room Number",background=bg,font=font2)
        self.t1=Entry(self.window)
        self.l4=Label(self.window,text="Choose Availablity",background=bg,font=font2)
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

        # t1 v1 v2 t6 v3

        #--------------------BUTTONS---------------
        self.b1=Button(self.window,foreground="white",background="black",height=2,width=11,text="Add Room"
                       ,command=self.saveData)


        # self.b2=Button(self.window,foreground="white",background="black",height=2,width=11,text="Cancel"
        #                ,command=lambda :Entrypage(self.window))

        self.b3 = Button(self.window, foreground="white", background="black", height=2,
                         width=13, text="Clear Data"
                         , command=self.clearPage)

        self.b4 = Button(self.window, foreground="white", background="black",
                         text="get particular record"
                         , command=self.fetchData)

        self.b5 = Button(self.window, foreground="white", background="black", height=2, width=13
                         , text="Delete Data"
                         , command=self.deleteData)

        self.b6 = Button(self.window, foreground="white", background="black", text="Search Data"
                         , command=lambda: room_search(self.window, self.v1.get()))

        self.b7 = Button(self.window, foreground="white", background="black", text="Update Data"
                         , height=2, width=13,command= self.updateData)

        self.b8 = Button(self.window, foreground="white", background="black", text="Search Data"
                         , command=lambda: room_search2(self.window, self.v2.get()))




        hcolor = "#464744"
        bg2="black"
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
        self.b8.bind("<Enter>", lambda e: self.changeColor(hcolor, "b8"))
        self.b8.bind("<Leave>", lambda e: self.changeColor(bg2, "b8"))



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

        self.b6.place(x=x1+x1_diff+180, y=y1+5)
        y1 = y1 + y1_diff

        self.l5.place(x=x1, y=y1)
        self.c2.place(x=x1+x1_diff,y=y1+5,height=25,width=150)

        self.b8.place(x=x1 + x1_diff + 180, y=y1 + 5)
        y1 = y1 + y1_diff

        self.l6.place(x=x1, y=y1)
        self.t6.place(x=x1+x1_diff,y=y1+5,height=25,width=150)
        y1 = y1 + y1_diff

        self.l7.place(x=x1, y=y1)
        self.c3.place(x=x1+x1_diff,y=y1+5,height=25,width=150)
        y1 = y1 + y1_diff

        self.b1.place(x=x1, y=y1+30)
        # self.b2.place(x=x1+100, y=y1+30)
        self.b3.place(x=x1+100, y=y1+30)
        self.b5.place(x=x1, y=y1+80)
        self.b7.place(x=x1+110, y=y1+80)

        self.clearPage()
        if col != None:
            self.fetchData(col)
        self.window.mainloop()


    #     --------------Functions--------------

    def changeColor(self,c,name):
        if name=="b1":
            self.b1.config(background=c)
        elif name=="b4":
            self.b4.config(background=c)
        elif name=="b5":
            self.b5.config(background=c)
        elif name=="b6":
            self.b6.config(background=c)
        elif name=="b7":
            self.b7.config(background=c)
        elif name=="b8":
            self.b8.config(background=c)

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

    # STEP 2 : MAKE SAVE DATA QUERY
    def saveData(self):
        if self.validate_check()==False:
            return # stop this function now
        self.databaseConnection()
        # RoomNumber	Availablity	CleaningStatus	Price	BedType
        try:
            myqry = "insert into rooms values(%s,%s,%s,%s,%s)"
            rowcount = self.curr.execute(myqry,
                                         (self.t1.get(), self.v1.get(), self.v2.get(), self.t6.get(),
                                          self.v3.get()))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Success", "Room Details saved successfully", parent=self.window)
                self.clearPage()
            else:
                messagebox.showinfo("Failure", "Check all fields carefully", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n" + str(e), parent=self.window)

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

                self.b5['state'] = 'normal'
                self.b7['state'] = 'normal'

            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n" + str(e), parent=self.window)

    # STEP4:UPDATE DATA
    def updateData(self):
        if self.validate_check()==False:
            return # stop this function now
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

    # STEP5:DELETE DATA

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure you want to delete this entry ?")
        if ans == 'yes':
            self.databaseConnection()

            # RoomNumber	Availablity	CleaningStatus	Price	BedType
            try:
                myqry = "delete from rooms where RoomNumber=%s"
                rowcount = self.curr.execute(myqry, (self.t1.get()))
                self.conn.commit()

                if rowcount == 1:
                    messagebox.showinfo("Success", "Room data deleted successfully", parent=self.window)
                    self.clearPage()
                    self.clearPage()
                else:
                    messagebox.showinfo("Failure", "Check all the fields carefully", parent=self.window)

            except Exception as e:
                messagebox.showerror("Query Error", "Error while deletion \n" + str(e), parent=self.window)
    # STEP6: SEARCH DATA
    # in another file

    def clearPage(self):
        # Name DOB Gender Job Salary Phone Aadhar Email
        self.t1.delete(0,END)
        self.v1.set("Choose Availability")
        self.v2.set("Cleaning Status")
        self.t6.delete(0,END)
        self.v3.set("Bed Type")

        self.b5['state']='disabled'
        self.b7['state']='disabled'


    def validate_check(self):
        # t1 v1 v2 t6 v3
        if not(self.t1.get().isdigit())   or  len(self.t1.get())<3:
            messagebox.showwarning("Validation Check", "Enter proper Room Number ", parent=self.window)
            return False

        elif (self.v1.get() == "Choose Availability") or (self.v1.get() == "No Availability"):
         messagebox.showwarning("Validation Check", "Enter availability of the room", parent=self.window)
         return False

        elif (self.v2.get() == "Cleaning Status") or (self.v2.get() == "No Cleaning Status"):
         messagebox.showwarning("Validation Check", "Enter Cleaning Status of the room", parent=self.window)
         return False

        elif not(self.t6.get().isdigit())   or  len(self.t6.get())<4:
            messagebox.showwarning("Input Error", "Please Enter Correct Price of the room", parent=self.window)
            return False

        elif (self.v3.get() == "Bed Type") or (self.v3.get() == "Bed Type"):
            messagebox.showwarning("Validation Check", "Enter Type of bed in the room", parent=self.window)
            return False

        return True

if __name__=='__main__':
    dummy_employee_page=Tk()
    add_room(dummy_employee_page)
    dummy_employee_page.mainloop()