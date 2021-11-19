
import mysql.connector
db_connect=mysql.connector.connect(host="localhost",user="root",password="maan",database="expense")
db_cursor=db_connect.cursor()
import matplotlib.pyplot as pyplot
import numpy as np
from array import *

def view_expense(day,month,year):
    print("view exp")

    print(day)
    print(month)
    print(year)

    db_cursor.execute(f"select Transport,Food,Home,Entertainment,Utilities,Health,Others from daily where day={day} and month={month} and year={year}")
    data=db_cursor.fetchall()
    k=data[0]
    (Transport,Food,Home,Entertainment,Utilities,Health,Others)=k
 
    dat=np.array([Transport,Food,Home,Entertainment,Utilities,Health,Others])
    print(dat)
    
    labe=['Transport','Food','Home','Entertainment','Utilities','Health','Others']
    pyplot.pie(dat,labels=labe,shadow= True, startangle=90, autopct='%1.0f%%',pctdistance=1.1, labeldistance=1.2, explode=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1))
    pyplot.axis('equal')
    pyplot.show()

#view_expense(16,11,21)
