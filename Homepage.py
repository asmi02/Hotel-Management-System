from tkinter import *
from tkinter import messagebox

from UpdateRoom import UpdateRoom
from add_room import add_room
from check_out import CheckOut
from checkout_report import checkout_report
from customer_form import customer_form
from customer_report import customer_report
from dynamic_room_search import dynamic_room_search
from employee_report import employee_report
from manager_info import manager_info
from room_report import room_report


class HomePage:
    def __init__(self,hwindow):

        # self.window=Tk()
        self.window = Toplevel(hwindow)
        self.window.title("Hotel Reception")
        #--------Window settings-----
        h=self.window.winfo_screenwidth()
        w=self.window.winfo_screenheight()

        w1=1000
        h1=760
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,300,20))
        # self.window.state("zoomed")
        self.window.config(background="#6bea8f")

        # --------------------- background image -----------------
        from PIL import Image, ImageTk
        self.bimg1 = Image.open("Project_Pics//reception.jpg")
        self.bimg1 = self.bimg1.resize((h, w))
        self.bimg2 = ImageTk.PhotoImage(self.bimg1)
        self.bimglbl = Label(self.window, image=self.bimg2)
        self.bimglbl.place(x=0, y=0)

        #----Menu------

        # self.window.option_add("*TearOff",False)
        # self.menubar=Menu()
        # self.window.config(menu=self.menubar)
        #
        # self.menu1=Menu()
        # self.menu2=Menu()
        # self.menu3=Menu()
        # self.menu4=Menu()
        # self.menu5=Menu()
        # self.menu6=Menu()
        # self.menu7=Menu()
        # self.menu8=Menu()
        # self.menu9=Menu()
        # self.menu10=Menu()
        # self.menu11=Menu()
        # self.menu12=Menu()
        #
        # self.menubar.add_cascade(menu=self.menu1,
        #                          label="Login")
        # self.menubar.add_cascade(menu=self.menu2,
        #                          label="New customer form")
        # self.menubar.add_cascade(menu=self.menu3,
        #                          label="Department")
        # self.menubar.add_cascade(menu=self.menu4,
        #                          label="Rooms")
        # self.menubar.add_cascade(menu=self.menu5,
        #                          label="Employee Details")
        # self.menubar.add_cascade(menu=self.menu6,
        #                          label="Customer info")
        # self.menubar.add_cascade(menu=self.menu7,
        #                          label="Manager info")
        # self.menubar.add_cascade(menu=self.menu8,
        #                          label="check-in")
        # self.menubar.add_cascade(menu=self.menu9,
        #                          label="check-out")
        # self.menubar.add_cascade(menu=self.menu10,
        #                          label="update room status")
        # self.menubar.add_cascade(menu=self.menu11,
        #                          label="search rooms")
        # self.menubar.add_cascade(menu=self.menu12,
        #                          label="logout")


        font1=["Calibri",12,"bold"]
        font2=["Candara",40,"bold"]
        bg="black"
        fg="white"
        bg2="#6bea8f"
        self.hd = Label(self.window, text="Hotel Reception", font=font2,
                         foreground="Black",padx=590)

        # -------------BUTTONS--------------

        self.btn2=Button(self.window,height=2,width=40,text="New Customer Form",font=font1,background=bg,foreground=fg,
                         cursor="hand2",command=lambda :customer_form(self.window))

        self.btn4=Button(self.window,height=2,width=40,text="Rooms",font=font1,background=bg,foreground=fg,
                         cursor="hand2",command=lambda :room_report(self.window))

        self.btn5=Button(self.window,height=2,width=40,text="All Employee Details",font=font1,
                         background=bg,foreground=fg,cursor="hand2",command=lambda :employee_report(self.window))

        self.btn6=Button(self.window,height=2,width=40,text="Customer Info",font=font1,background=bg
                         ,foreground=fg,cursor="hand2",command=lambda :customer_report(self.window))

        self.btn7=Button(self.window,height=2,width=40,text="Manager Info",font=font1,background=bg,foreground=fg
                         ,cursor="hand2",command=lambda :manager_info(self.window))

        self.btn9=Button(self.window,height=2,width=40,text="Check-Out",font=font1,background=bg,foreground=fg,
                         cursor="hand2",command=lambda :CheckOut(self.window))

        self.btn10=Button(self.window,height=2,width=40,text="Update Room Status",font=font1,background=bg
                          ,foreground=fg,cursor="hand2",command=lambda :UpdateRoom(self.window))

        self.btn11=Button(self.window,height=2,width=40,text="Search Rooms",font=font1,background=bg
                          ,foreground=fg,cursor="hand2",command=lambda :dynamic_room_search(self.window))

        self.btn12=Button(self.window,height=2,width=40,text="Checkout Info",font=font1,background=bg
                          ,foreground=fg,cursor="hand2",command=lambda :checkout_report(self.window))



        hcolor="#464744"
        self.btn2.bind("<Enter>",lambda e:self.changeColor(hcolor,"btn2"))
        self.btn2.bind("<Leave>",lambda e:self.changeColor(bg,"btn2"))
        self.btn4.bind("<Enter>",lambda e:self.changeColor(hcolor,"btn4"))
        self.btn4.bind("<Leave>",lambda e:self.changeColor(bg,"btn4"))
        self.btn5.bind("<Enter>",lambda e:self.changeColor(hcolor,"btn5"))
        self.btn5.bind("<Leave>",lambda e:self.changeColor(bg,"btn5"))
        self.btn6.bind("<Enter>",lambda e:self.changeColor(hcolor,"btn6"))
        self.btn6.bind("<Leave>",lambda e:self.changeColor(bg,"btn6"))
        self.btn7.bind("<Enter>",lambda e:self.changeColor(hcolor,"btn7"))
        self.btn7.bind("<Leave>",lambda e:self.changeColor(bg,"btn7"))
        self.btn9.bind("<Enter>",lambda e:self.changeColor(hcolor,"btn9"))
        self.btn9.bind("<Leave>",lambda e:self.changeColor(bg,"btn9"))
        self.btn10.bind("<Enter>",lambda e:self.changeColor(hcolor,"btn10"))
        self.btn10.bind("<Leave>",lambda e:self.changeColor(bg,"btn10"))
        self.btn11.bind("<Enter>",lambda e:self.changeColor(hcolor,"btn11"))
        self.btn11.bind("<Leave>",lambda e:self.changeColor(bg,"btn11"))
        self.btn12.bind("<Enter>", lambda e: self.changeColor(hcolor, "btn12"))
        self.btn12.bind("<Leave>", lambda e: self.changeColor(bg, "btn12"))

#---------------PLACEMENTS---------------
        x1=70
        y1=120
        y1_diff=70
        self.hd.place(x=0, y=0, height=90)

        self.btn2.place(x=x1,y=y1)

        self.btn4.place(x=x1,y=y1+y1_diff)
        y1 = y1 + y1_diff

        self.btn5.place(x=x1,y=y1+y1_diff)
        y1 = y1 + y1_diff

        self.btn6.place(x=x1,y=y1+y1_diff)
        y1 = y1 + y1_diff

        self.btn7.place(x=x1,y=y1+y1_diff)
        y1 = y1 + y1_diff

        self.btn9.place(x=x1,y=y1+y1_diff)
        y1 = y1 + y1_diff

        self.btn10.place(x=x1,y=y1+y1_diff)
        y1 = y1 + y1_diff

        self.btn11.place(x=x1,y=y1+y1_diff)
        y1 = y1 + y1_diff

        self.btn12.place(x=x1,y=y1+y1_diff)






        self.window.mainloop()

    def changeColor(self,c,name):
        if name=="btn2":
            self.btn2.config(background=c)
        elif name=="btn4":
            self.btn4.config(background=c)
        elif name=="btn5":
            self.btn5.config(background=c)
        elif name=="btn6":
            self.btn6.config(background=c)
        elif name=="btn7":
            self.btn7.config(background=c)
        elif name=="btn9":
            self.btn9.config(background=c)
        elif name=="btn10":
            self.btn10.config(background=c)
        elif name=="btn11":
            self.btn11.config(background=c)
        elif name=="btn12":
            self.btn12.config(background=c)


if __name__=='__main__':
    dummy_Homepage=Tk()
    HomePage(dummy_Homepage)
    dummy_Homepage.mainloop()