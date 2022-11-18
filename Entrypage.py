from tkinter import *
from tkinter import messagebox

from ChangePassword import ChangePasswordClass
from Homepage import HomePage
from add_room import add_room
from add_employee import add_employee
from checkout_report import checkout_report
from customer_report import customer_report
from employee_report import employee_report
from manageuser import UserClass


class Entrypage:
    def __init__(self,uname,utype):
        self.window=Tk()

        # self.window = Toplevel(hwindow)

        self.window.title("Entry Page")




        #--------Window settings-----
        h=self.window.winfo_screenwidth()
        w=self.window.winfo_screenheight()

        w1=1000
        h1=500
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,300,100))
        self.window.state("zoomed")

        # --------------------- background image -----------------
        from PIL import Image, ImageTk
        self.bimg1 = Image.open("Project_Pics//ApnaHotel.jpg")
        self.bimg1 = self.bimg1.resize((h,w))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.window, image=self.bimg2)
        self.bimglbl.place(x=0, y=0)

        #----Menu------

        self.window.option_add("*TearOff",False)
        self.menubar=Menu()
        self.window.config(menu=self.menubar)

        font1 = ["Candara", 35, "bold"]
        self.hd = Label(self.window, text="WELCOME TO APNA HOTEL"
                        , font=font1, foreground="Black",padx=500)

        self.menu1=Menu()
        self.menu2=Menu()
        self.menu3=Menu()
        self.menu4=Menu()

        self.menubar.add_cascade(menu=self.menu1,label="Hotel management")
        self.menubar.add_cascade(menu=self.menu2,label="Admin")
        self.menubar.add_cascade(menu=self.menu3,label="Reports")
        self.menubar.add_cascade(menu=self.menu4,label="Account")


        # -----adding fields in submenu

        self.report_icon = Image.open("Project_Pics//report.webp")
        self.report_icon = self.report_icon.resize((10, 10))
        self.report_icon2 = ImageTk.PhotoImage(self.report_icon)

        self.menu1.add_command(label="Reception",command=lambda : HomePage(self.window),accelerator="ctrl+r")
        self.window.bind("<Control-r>", lambda e: HomePage(self.window))
        self.menu2.add_command(label="Add Employee",command=lambda :add_employee(self.window))
        self.menu2.add_command(label="Add Room",command=lambda :add_room(self.window))
        self.menu3.add_command(label="Print Customer Report",command=lambda :customer_report(self.window)
                               ,image=self.report_icon2,compound=LEFT)
        self.menu3.add_command(label="Print Employee Report",command=lambda :employee_report(self.window)
                               ,image=self.report_icon2,compound=LEFT)
        self.menu3.add_command(label="Print Checkout Report",command=lambda :checkout_report(self.window)
                               ,image=self.report_icon2,compound=LEFT)


        self.pswd_icon=Image.open("Project_Pics//password.png")
        self.pswd_icon=self.pswd_icon.resize((10,10))
        self.pswd_icon2=ImageTk.PhotoImage(self.pswd_icon)

        self.user_icon = Image.open("Project_Pics//user.webp")
        self.user_icon = self.user_icon.resize((10, 10))
        self.user_icon2 = ImageTk.PhotoImage(self.user_icon)

        self.menu4.add_command(label="Manage User", command=lambda: UserClass(self.window),accelerator="ctrl+u"
                               ,image=self.user_icon2,compound=LEFT)
        self.window.bind("<Control-u>", lambda e: UserClass(self.window))
        self.menu4.add_command(label="Change Password", command=lambda: ChangePasswordClass(self.window, uname)
                               ,image=self.pswd_icon2,compound=LEFT)
        self.menu4.add_command(label="Logout", command=lambda: self.quitter())

        if (utype == "Employee"):
            self.menubar.entryconfig(2, state='disabled')
            self.menubar.delete(1)
            self.menu4.entryconfig(0, state='disabled')
            self.window.unbind("<Control-u>")

        # --------PLACEMENTS---------

        x1 = 100
        y1 = 150
        y1_diff = 50
        x1_diff = 170

        self.hd.place(x=0, y=0,  height=90)
        self.window.mainloop()

    def quitter(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to Logout ??", parent=self.window)
        if ans == "yes":
            self.window.destroy()
            from LoginPage import LoginClass
            LoginClass()





# if __name__ == '__main__':
#     Entrypage("ritu","Admin")