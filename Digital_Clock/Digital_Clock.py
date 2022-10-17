from tkinter import *
from turtle import width
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')

    date = time.strftime('%d')
    mon = time.strftime('%m')
    yr = time.strftime('%y')
    day = time.strftime('%a')
    
    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)

    lab_date.config(text=date)
    lab_mon.config(text=mon)
    lab_yr.config(text=yr)
    lab_day.config(text=day)

    lab_hr.after(200, date_time)
  


clock = Tk()

clock.title("DIGITAL CLOCK")

clock.geometry('1000x500')

clock.config(bg='red')

#Time Label Section starts.

lab_hr = Label(clock, #Label function. Creating box
               text="00", 
               font=("Times New Roman",60, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_hr.place(x=120,y=40,height=110,width=100)

lab_hr_text = Label(clock, 
               text="Hour", 
               font=("Times New Roman",20, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_hr_text.place(x=120,y=190,height=30,width=100)


lab_min = Label(clock, 
               text="00", 
               font=("Times New Roman",60, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_min.place(x=340,y=40,height=110,width=100)

lab_min_text = Label(clock, 
               text="Minute", 
               font=("Times New Roman",20, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_min_text.place(x=340,y=190,height=30,width=100)


lab_sec = Label(clock, 
               text="00", 
               font=("Times New Roman",60, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_sec.place(x=560,y=40,height=110,width=100)

lab_sec_text = Label(clock, 
               text="Second", 
               font=("Times New Roman",20, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_sec_text.place(x=560,y=190,height=30,width=100)

lab_am = Label(clock, 
               text="00", 
               font=("Times New Roman",50, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_am.place(x=780,y=40,height=110,width=100) 

lab_am_text = Label(clock, 
               text="AM/PM", 
               font=("Times New Roman",20, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_am_text.place(x=780,y=190,height=30,width=100) 

# Time Label Section ends.


#Date Label Section starts.


lab_date = Label(clock, #Label function. Creating box
               text=" ", 
               font=("Times New Roman",30, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_date.place(x=120,y=270,height=110,width=100)

lab_date_text = Label(clock, 
               text="Date", 
               font=("Times New Roman",20, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_date_text.place(x=120,y=410,height=30,width=100)

lab_mon = Label(clock, #Label function. Creating box
               text=" ", 
               font=("Times New Roman",30, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_mon.place(x=340,y=270,height=110,width=100)

lab_mon_text = Label(clock, 
               text="Month", 
               font=("Times New Roman",20, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_mon_text.place(x=340,y=410,height=30,width=100)

lab_yr = Label(clock, #Label function. Creating box
               text=" ", 
               font=("Times New Roman",30, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_yr.place(x=560,y=270,height=110,width=100)

lab_yr_text = Label(clock, 
               text="Year", 
               font=("Times New Roman",20, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_yr_text.place(x=560,y=410,height=30,width=100)

lab_day = Label(clock, #Label function. Creating box
               text=" ", 
               font=("Times New Roman",30, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_day.place(x=780,y=270,height=110,width=100)

lab_day_text = Label(clock, 
               text="Day", 
               font=("Times New Roman",20, "bold"),
               bg="Green",
               fg="White",
               )
#lab_hr box is ready. Now we will give it a placement in the object.

lab_day_text.place(x=780,y=410,height=30,width=100)


date_time()
clock.mainloop()

