from tkinter import *
import mysql.connector
db_connect=mysql.connector.connect(host="localhost",user="root",password="maan",database="expense")
db_cursor=db_connect.cursor()
import matplotlib.pyplot as pyplot
import numpy as np
from array import *

def view_expense(day,month,year):
    print("view exp")
    window=Tk()
    window.title("View Expense list")   
    # l_message=Label(window)
    print(day)
    print(month)
    print(year)

    db_cursor.execute(f"select Transport,Food,Home,Entertainment,Utilities,Health,Others from daily where day={day} and month={month} and year={year}")
    data=db_cursor.fetchall()
    k=data[0]
    (Transport,Food,Home,Entertainment,Utilities,Health,Others)=k
    wn=Tk()
    dat=np.array([Transport,Food,Home,Entertainment,Utilities,Health,Others])
    print(dat)
    
    labe=['Transport','Food','Home','Entertainment','Utilities','Health','Others']
    pyplot.pie(dat,labels=labe,shadow= True)
    pyplot.show()
    exit_button = Button(wn, text="Exit2", command=wn.destroy)
    exit_button.pack(pady=200)
    wn.geometry("300x300")
    wn.mainloop()

    exit_button = Button(window, text="Exit1", command=window.destroy)
    exit_button.pack(pady=200)
    window.geometry("300x300")
    window.mainloop()    

# view_expense(15,11,21)