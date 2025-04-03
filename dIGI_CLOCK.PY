from tkinter import *
import datetime
def date_time():
    time=datetime.datetime.now()
    hr=time.strftime("%I")
    min=time.strftime("%M")
    sec=time.strftime("%S")
    am=time.strftime("%p")
    date=time.strftime("%d")
    month=time.strftime("%m")
    yr=time.strftime("%y")
    day=time.strftime("%a")
    
    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_yr.config(text=yr)
    lab_day.config(text=day)
    
    lab_hr.after(100,date_time)
    





clock=Tk()
clock.geometry("1000x500")
clock.config(bg="#CC7722")
clock.title("_#Supratik's digi clocky_#")

lab_hr=Label(clock,text="00",font=("Times New Roman",40,"bold"),bg="red",fg="white")
lab_hr.place(x=120,y=55,height=110,width=100)
lab_hr_txt=Label(clock,text="Hour",font=("Times New Roman",20,"bold"),bg="black",fg="white")
lab_hr_txt.place(x=120,y=195,height=40,width=100)

lab_min=Label(clock,text="00",font=("Times New Roman",40,"bold"),bg="red",fg="white")
lab_min.place(x=340,y=55,height=110,width=100)
lab_min_txt=Label(clock,text="Min.",font=("Times New Roman",20,"bold"),bg="black",fg="white")
lab_min_txt.place(x=340,y=195,height=40,width=100)

lab_sec=Label(clock,text="00",font=("Times New Roman",40,"bold"),bg="red",fg="white")
lab_sec.place(x=560,y=55,height=110,width=100)
lab_sec_txt=Label(clock,text="Sec.",font=("Times New Roman",20,"bold"),bg="black",fg="white")
lab_sec_txt.place(x=560,y=195,height=40,width=100)


lab_am=Label(clock,text="00",font=("Times New Roman",35,"bold"),bg="red",fg="white")
lab_am.place(x=780,y=55,height=110,width=100)
lab_am_txt=Label(clock,text="AM/PM",font=("Times New Roman",19,"bold"),bg="black",fg="white")
lab_am_txt.place(x=780,y=195,height=40,width=100)

lab_date=Label(clock,text="00",font=("Times New Roman",40,"bold"),bg="red",fg="white")
lab_date.place(x=120,y=265,height=110,width=100)
lab_date_txt=Label(clock,text="Date",font=("Times New Roman",20,"bold"),bg="black",fg="white")
lab_date_txt.place(x=120,y=405,height=40,width=100)

lab_month=Label(clock,text="00",font=("Times New Roman",40,"bold"),bg="red",fg="white")
lab_month.place(x=340,y=265,height=110,width=100)
lab_month_txt=Label(clock,text="Month",font=("Times New Roman",20,"bold"),bg="black",fg="white")
lab_month_txt.place(x=340,y=405,height=40,width=100)

lab_yr=Label(clock,text="00",font=("Times New Roman",40,"bold"),bg="red",fg="white")
lab_yr.place(x=560,y=265,height=110,width=100)
lab_yr_txt=Label(clock,text="Yr",font=("Times New Roman",20,"bold"),bg="black",fg="white")
lab_yr_txt.place(x=560,y=405,height=40,width=100)

lab_day=Label(clock,text="00",font=("Times New Roman",40,"bold"),bg="red",fg="white")
lab_day.place(x=780,y=265,height=110,width=100)
lab_day_txt=Label(clock,text="Day",font=("Times New Roman",20,"bold"),bg="black",fg="white")
lab_day_txt.place(x=780,y=405,height=40,width=100)







date_time()
clock.mainloop()