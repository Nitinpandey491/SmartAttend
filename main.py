from tkinter import *
import customtkinter as ctk
from PIL import Image,ImageTk 
from PIL.Image import Resampling
from tkinter import messagebox as mb
import os

class Main:
    def __init__(self,root):
        self.root = root

        # logo
        self.icon_image = PhotoImage(file="app_images/logo.png")
        self.root.iconphoto(False, self.icon_image)

        self.root.title("Main")
        self.root.geometry("1550x800+0+0")
        self.root.configure(background="#384959")

        #main label
        logo_lbl = Label(self.root,text="SmartAttend - Face Recognition Based Attendance",font=("new times roman",20,"bold"),fg="#384959",bg="#BDDDFC")
        logo_lbl.place(x=0,y=0,width=1550,height=100)

        img4 = Image.open("app_images/mlogo.png")
        img4 = img4.resize((100,100), Resampling.LANCZOS)
        self.photo4 = ImageTk.PhotoImage(img4)
        lbl_img4 = Label(self.root,image=self.photo4,bg="#BDDDFC")
        lbl_img4.place(width=100,height=100,x=15,y=0)

        img5 = Image.open("app_images/mlogo.png")
        img5 = img5.resize((100,100), Resampling.LANCZOS)
        self.photo5 = ImageTk.PhotoImage(img5)
        lbl_img5 = Label(self.root,image=self.photo5,bg="#BDDDFC")
        lbl_img5.place(width=100,height=100,x=1415,y=0) 

        frame = ctk.CTkFrame(self.root,width=1536,height=100,border_color="light blue",border_width=3,fg_color="#6A89A7")
        frame.place(x=0,y=100)

        # buttons

        # student details

        # student details button
        sd_image = ctk.CTkImage(Image.open("app_images/student_icon.png"))
        sd_btn = ctk.CTkButton(frame,text="STUDENT DETAILS",width=220,height=40,corner_radius=20,
                               text_color="white",font=("new times roman",15,"bold"),border_color="white",hover_color="green",
                               cursor="hand2",border_width=2,image=sd_image,compound="left",command=self.open_student_detail
                               )
                               
        sd_btn.place(x=15,y=30)

        # face recognition

        # face recognition button
        fr_image = ctk.CTkImage(Image.open("app_images/face_icon.png"))
        fr_btn = ctk.CTkButton(frame,text="TAKE ATTENDANCE",width=220,height=40,corner_radius=20,
                               text_color="white",font=("new times roman",15,"bold"),border_color="white",hover_color="green",
                               cursor="hand2",border_width=2,image=fr_image,compound="left",command=self.open_face_recognition
                               )
                               
        fr_btn.place(x=250,y=30)

        # attendance

        # attendance button
        ad_image = ctk.CTkImage(Image.open("app_images/attendance_icon.png"))
        ad_btn = ctk.CTkButton(frame,text="ATTENDANCE",width=220,height=40,corner_radius=20,
                               text_color="white",font=("new times roman",15,"bold"),border_color="white",hover_color="green",
                               cursor="hand2",border_width=2,image=ad_image,compound="left",command=self.open_attendance
                               )
                               
        ad_btn.place(x=485,y=30)

         # train data

        # train data button
        td_image = ctk.CTkImage(Image.open("app_images/train_data_icon.png"))
        td_btn = ctk.CTkButton(frame,text="TRAIN DATA",width=220,height=40,corner_radius=20,
                               text_color="white",font=("new times roman",15,"bold"),border_color="white",hover_color="green",
                               cursor="hand2",border_width=2,image=td_image,compound="left",command=self.open_train_data
                               )
                               
        td_btn.place(x=720,y=30)

        # photos

        # photos button
        p_image = ctk.CTkImage(Image.open("app_images/photos_icon.png"))
        p_btn = ctk.CTkButton(frame,text="PHOTOS",width=220,height=40,corner_radius=20,
                               text_color="white",font=("new times roman",15,"bold"),border_color="white",hover_color="green",
                               cursor="hand2",border_width=2,image=p_image,compound="left",command=self.open_img
                               )
                               
        p_btn.place(x=955,y=30)

        # exit

        # exit button
        e_image = ctk.CTkImage(Image.open("app_images/exit_icon.png"))
        e_btn = ctk.CTkButton(frame,text="EXIT",width=100,height=40,corner_radius=20,
                               text_color="white",font=("new times roman",15,"bold"),border_color="white",hover_color="red",
                               cursor="hand2",border_width=2,image=e_image,compound="left",command=self.exit
                               )
                               
        e_btn.place(x=1410,y=30)

        
        
    def clock(self):
        clock_frame = ctk.CTkFrame(self.root,width=600,height=300,border_color="light blue",border_width=3,fg_color="#2ea9f0")
        clock_frame.place(x=100,y=300)

        self.DIGITAL_FONT = ("DS-Digital", 50, "bold")
        self.DATE_FONT = ("DS-Digital", 20)
        self.DAY_FONT = ("Arial", 12, "bold")

        # --- Days of Week ---
        days_frame = Frame(clock_frame, bg="#2ea9f0")
        days_frame.place(x=23,y=3,width=555,height=40)

        self.days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
        self.day_labels = []
        for day in self.days:
            lbl = Label(days_frame, text=day, font=self.DAY_FONT, fg="white", bg="#2ea9f0")
            lbl.pack(side=LEFT, padx=20) # by default pack() linearly widgets ko pack karta hai line by line ek ke niche ek
            self.day_labels.append(lbl)

        # --- Time Label ---
        self.time_label = Label(clock_frame, font=self.DIGITAL_FONT, fg="#002147", bg="#2ea9f0")
        self.time_label.place(x=200,y=80)

        # --- Date and AM/PM Frame ---
        bottom_frame = Frame(clock_frame, bg="#2ea9f0")
        bottom_frame.place(x=3,y=200,width=594,height=50)

        self.date_label = Label(bottom_frame, font=self.DATE_FONT, fg="#002147", bg="#2ea9f0")
        self.date_label.pack(side=LEFT, padx=20)

        self.ampm_label = Label(bottom_frame, font=self.DATE_FONT, fg="#002147", bg="#2ea9f0")
        self.ampm_label.pack(side=RIGHT, padx=20)

        self.update_time()
        
    def update_time(self):
        import datetime
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M:%S")
        am_pm = now.strftime("%p")
        date_str = now.strftime("%d-%m-%Y")

        self.time_label.config(text=current_time)
        self.date_label.config(text=date_str)
        self.ampm_label.config(text=am_pm)

        current_day = now.strftime("%a").upper()
        for lbl in self.day_labels:
            if lbl.cget("text") == current_day:
                lbl.config(fg="#002147", font=("Arial", 12, "bold", "underline"))
            else:
                lbl.config(fg="white", font=self.DAY_FONT)

        self.root.after(1000, self.update_time)
    # $$$$$$$$$$$$$$$$$$$$$ student_detail.py $$$$$$$$$$$$$$$$$$$$$$ #
    def open_student_detail(self):
        from student_detail import Student_detail
        root4 = Toplevel(self.root)
        s = Student_detail(root4)
    # $$$$$$$$$$$$$$$$$$$$$ face_recognition.py $$$$$$$$$$$$$$$$$$$$$$ #
    def open_face_recognition(self):
        from face_recognition import Face_recognition
        root3 = Toplevel(self.root)
        f = Face_recognition(root3)
    # $$$$$$$$$$$$$$$$$$$$$ open train_data.py $$$$$$$$$$$$$$$$$$$$$$ #
    def open_train_data(self):
        from train_data import Train_data
        root2 = Toplevel(self.root)
        t = Train_data(root2)
    # $$$$$$$$$$$$$$$$$$$$$ open attendance.py $$$$$$$$$$$$$$$$$$$$$$ #
    def open_attendance(self):
        from attendance import Attendance
        root5 = Toplevel(self.root)
        a = Attendance(root5)
    # $$$$$$$$$$$$$$$$$$$$$ Exit $$$$$$$$$$$$$$$$$$$$$$ # os._exit(0)
    def exit(self):
        v = mb.askyesno('EXIT','Do you really want to exit ?',parent=self.root)
        if v:
            os._exit(0)


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Photos $$$$$$$$$$$$$$$$$$$$$$$ #
    def open_img(self):
        os.startfile("data")

if __name__ == '__main__':
    root = Tk()
    m = Main(root)
    m.clock()
    root.mainloop()