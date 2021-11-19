#Import the libraries
from tkinter import *
from tkcalendar import *
import datetime
import addexp
import viewexp
d=""
today = datetime.date.today()
#Create an instance of tkinter frame or window
def dayis():
   global d
   win= Tk()
   win.title("Expense calender")
   win.geometry("700x600")

   cal= Calendar(win, font="Arial 14", selectmode="day",year= today.year, month=today.month, day=today.day)
   cal.pack(pady=20)
   
   #Define Function to select the date
   def get_date():
      global d
      dt=cal.get_date()
      month, day, year = (int(x) for x in dt.split('/'))  
    #   ans_date = datetime.date(day)
    #   ans_month=datetime.date(month)
    #   ans_year=datetime.date(year)
      print(day)
      print(month)
      print(year)
      print(d)
      label.config(text=dt)
      addexpdate= Button(win, text= "add expense", command= lambda: addexp.add_expense(day,month,year))
      addexpdate.pack(pady=30)
      searchexpdate= Button(win, text= "show expense", command=lambda: viewexp.view_expense(day,month,year))
      searchexpdate.pack(pady=30)
   #Create a button to pick the date from the calendar
   button= Button(win, text= "Select the Date", command= get_date)
   button.pack(pady=20)
   #Create Label for displaying selected Date
   label= Label(win, text="")
   label.pack(pady=20)
   exit_button = Button(win, text="Exit", command=win.destroy)
   exit_button.pack(pady=20)
   win.mainloop()

dayis()
# print(j)