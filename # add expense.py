# add expense
from tkinter import *
import date
import mysql.connector
db_connect=mysql.connector.connect(host="localhost",user="root",password="toor",database="expense")
db_cursor=db_connect.cursor()



def add_expense():
    window=Tk()
    window.title("Expense list")   
    l_message=Label(window)
    l_pid=Label(window,text="Patient ID :")
    e_pid=Entry(window)

    
    def patient_search(): 
        day=int(e_day.get())  
        wn=Tk()
        wn.title("Patient Search")
        db_cursor.execute(f"select * from daily where day={pid_s}")
        data=db_cursor.fetchall()
        for pat in data:
            L=Label(wn,width=40, text=pat)
            L.grid(row=1,column=1)
        # l_message.config(text="Found Patient Record !")  
        b3=Button(wn,text="Search",command=date_getter.dayis)
        b3.place(x=80,y=150)
        ##APPOINT

        wn.geometry("300x300")
        wn.mainloop()

    
    b1=Button(window,text="Search",command=lambda:patient_search())# connect to appointment
    b2=Button(window,text="Add Patient +",command=patient_add_32.add_patient)

    l_pid.place(x =20,y=50)
    e_pid.place(x =120,y=50)
    b1.place(x=250,y=50)
    l_message.place(x=50,y=100)
    b2.place(x=80,y=150)

    window.geometry("300x300")
    window.mainloop()

add_expense()
