from tkinter import *
from tkinter import messagebox
import pymysql
class MainClass:
    def __init__(self):
        self.databaseConnection()
        try:
            myqry = "select * from usertable"
            rowcount = self.curr.execute(myqry)
            data = self.curr.fetchall()
            if data:
                from LoginPage import LoginClass
                LoginClass()
            else:
                from CreateAdmin import CreateUserClass
                CreateUserClass()
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e))

    def databaseConnection(self):
        myhost="localhost"
        mydb="hotelmgmtdb"
        myuser="root"
        mypassword=""
        try:
            self.conn = pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting database \n"+str(e))

if __name__ == '__main__':
    MainClass()
