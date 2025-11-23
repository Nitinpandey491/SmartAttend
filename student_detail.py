from tkinter import *
import customtkinter as ctk
from tkinter import ttk
from PIL import Image,ImageTk
from PIL.Image import Resampling
from tkinter import messagebox as mb
import re
import mysql.connector
import cv2
import numpy as np

class Student_detail:
    def __init__(self,root):
        self.root = root

        # variables 

        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_std_div = StringVar()
        self.var_rollno = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phoneno = StringVar()
        self.var_radio = StringVar()
        self.var_search = StringVar()
        self.var_search_item = StringVar()

    



        # logo
        self.icon_image = PhotoImage(file="app_images/logo.png")
        self.root.iconphoto(False, self.icon_image)

        # geometry
        self.root.title("Student Details")
        self.root.geometry("1550x800+0+0")
        self.root.configure(background="#384959")

         # main logo

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

        # student management frame
        sm_frame = ctk.CTkFrame(self.root,width=1536,height=80,border_color="light blue",border_width=3,fg_color="#6A89A7")
        sm_frame.place(x=0,y=100)
        sm_frame.pack_propagate(False)

        self.sm_img = ctk.CTkImage(Image.open("app_images/sm_icon.png"), size=(40,40))

        sm_lbl = ctk.CTkLabel(sm_frame,text="STUDENT MANAGEMENT",font=("new times roman",25,"bold"),text_color="white",
                              fg_color="#6A89A7",image=self.sm_img,compound="left",padx=10)
        sm_lbl.pack(pady=25,anchor='center')

        # student information frame ............................................................................................. #

        si_frame = ctk.CTkScrollableFrame(self.root,width=700,height=470,corner_radius=20,fg_color="#6bb5e0",
                                          label_text="Student Information",label_font=("new times roman",20,"bold"),
                                          label_text_color="white",label_fg_color="blue",scrollbar_button_color="blue",
                                          scrollbar_button_hover_color="light blue")
        si_frame.place(x=15,y=200)

        # student info img
        si_img = Image.open("app_images/si_icon.png")
        si_img = si_img.resize((20,20), Resampling.LANCZOS)
        self.si_img1 = ImageTk.PhotoImage(si_img)
        lbl_si_img = Label(self.root,image=self.si_img1,bg="blue")
        lbl_si_img.place(width=20,height=20,x=257,y=224)

        # current course information 

        cci_img = ctk.CTkImage(Image.open("app_images/cci_icon.png"))
        cci_lbl = ctk.CTkLabel(si_frame,text="Current Course Information",text_color="white",font=("new times roman",20,"bold"),
                               fg_color="#6bb5e0",image=cci_img,compound="left",padx=10)
        cci_lbl.pack()

        # current course informataion ........................................#
        cci_frame1 = Frame(si_frame, width=650, height=30,bg="#6bb5e0")
        cci_frame1.pack(pady=20)   
        cci_frame1.pack_propagate(False)     
        # form 
        dept_lbl = Label(cci_frame1,text="Department:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        dept_lbl.pack(side="left",anchor="n",padx=10)

        dept_entry = ttk.Combobox(cci_frame1,textvariable=self.var_dept,font=("new times roman",12,"bold"))
        dept_entry["values"] = ("Computer Science","Information Technology","Data Scidence","Physics","Math")
        dept_entry.pack(side="left",anchor="n")

        course_lbl = Label(cci_frame1,text="Course:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        course_lbl.pack(side="left",anchor="n",padx=10)

        course_entry = ttk.Combobox(cci_frame1,textvariable=self.var_course,font=("new times roman",12,"bold"))
        course_entry["values"] = ("B.Tech","M.Tech","BCA","MCA","Diploma","BSc-CS","BSC-IT")
        course_entry.pack(side="left",anchor="n")
        
        # cci_frame2 for further fields
        cci_frame2 = Frame(si_frame, width=650, height=30,bg="#6bb5e0")
        cci_frame2.pack(pady=10)   
        cci_frame2.pack_propagate(False) 

        # form
        year_lbl = Label(cci_frame2,text="Year:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        year_lbl.pack(side="left",anchor="n",padx=10)

        year_entry = ttk.Combobox(cci_frame2,textvariable=self.var_year,font=("new times roman",12,"bold"))
        year_entry["values"] = ("2024-2025","2023-2024","2022-2023","2021-2022")
        year_entry.pack(side="left",anchor="n")

        sem_lbl = Label(cci_frame2,text="Semester:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        sem_lbl.pack(side="left",anchor="n",padx=10)

        sem_entry = ttk.Combobox(cci_frame2,textvariable=self.var_sem,font=("new times roman",12,"bold"))
        sem_entry["values"] = ("Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6")
        sem_entry.pack(side="left",anchor="n")

        # student class information .................................................................................. #

        sci_img = ctk.CTkImage(Image.open("app_images/sci_icon.png"))
        sci_lbl = ctk.CTkLabel(si_frame,text="Student Class Information",text_color="white",font=("new times roman",20,"bold"),
                               fg_color="#6bb5e0",image=sci_img,compound="left",padx=10)
        sci_lbl.pack(pady=30)
        # form 

        # sci_frame1
        sci_frame1 = Frame(si_frame, width=650, height=30,bg="#6bb5e0")
        sci_frame1.pack(padx=50,pady=10)   
        sci_frame1.pack_propagate(False)
        # field_1
        std_id_lbl = Label(sci_frame1,text="Student ID:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        std_id_lbl.pack(side="left",anchor="n",padx=60)

        std_id_entry = ttk.Entry(sci_frame1,textvariable=self.var_std_id,font=("new times roman",12,"bold"),width=30)
        std_id_entry.pack(side="left",anchor="n") 

        # sci_frame2
        sci_frame2 = Frame(si_frame, width=650, height=30,bg="#6bb5e0")
        sci_frame2.pack(padx=50,pady=10)   
        sci_frame2.pack_propagate(False)
        # field_2
        std_name_lbl = Label(sci_frame2,text="Student Name:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        std_name_lbl.pack(side="left",anchor="n",padx=45)

        std_name_entry = ttk.Entry(sci_frame2,textvariable=self.var_std_name,font=("new times roman",12,"bold"),width=30)
        std_name_entry.pack(side="left",anchor="n")

        # sci_frame3
        sci_frame3 = Frame(si_frame, width=650, height=30,bg="#6bb5e0")
        sci_frame3.pack(padx=50,pady=3)   
        sci_frame3.pack_propagate(False)
        # field_3
        std_cd_lbl = Label(sci_frame3,text="Class Division:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        std_cd_lbl.pack(side="left",anchor="n",padx=45)

        std_cd_entry = ttk.Combobox(sci_frame3,textvariable=self.var_std_div,font=("new times roman",12,"bold"),width=28)
        std_cd_entry["values"] = ("A","B","C","D","E")
        std_cd_entry.pack(side="left",anchor="n")

        # sci_frame4
        sci_frame4 = Frame(si_frame, width=650, height=30,bg="#6bb5e0")
        sci_frame4.pack(padx=50,pady=10)   
        sci_frame4.pack_propagate(False)
        # field_4
        std_rn_lbl = Label(sci_frame4,text="Roll No:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        std_rn_lbl.pack(side="left",anchor="n",padx=70)

        std_rn_entry = ttk.Entry(sci_frame4,textvariable=self.var_rollno,font=("new times roman",12,"bold"),width=30)
        std_rn_entry.pack(side="left",anchor="n")

        # sci_frame5
        sci_frame5 = Frame(si_frame, width=650, height=30,bg="#6bb5e0")
        sci_frame5.pack(padx=50,pady=3)   
        sci_frame5.pack_propagate(False)
        # field_5
        std_rn_lbl = Label(sci_frame5,text="Gender:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        std_rn_lbl.pack(side="left",anchor="n",padx=70)

        std_g_entry = ttk.Combobox(sci_frame5,textvariable=self.var_gender,font=("new times roman",12,"bold"),width=28,state="readonly")
        std_g_entry["values"] = ("Select Gender","Male","Female","Others")
        std_g_entry.pack(side="left",anchor="n")
        std_g_entry.current(0)

        # sci_frame6
        sci_frame6 = Frame(si_frame, width=650, height=30,bg="#6bb5e0")
        sci_frame6.pack(padx=50,pady=10)   
        sci_frame6.pack_propagate(False)
        # field_6
        std_dob_lbl = Label(sci_frame6,text="Date Of Birth:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        std_dob_lbl.pack(side="left",anchor="n",padx=50)

        std_dob_entry = ttk.Entry(sci_frame6,textvariable=self.var_dob,font=("new times roman",12,"bold"),width=30)
        std_dob_entry.pack(side="left",anchor="n")

        # sci_frame7
        sci_frame7 = Frame(si_frame, width=650, height=30,bg="#6bb5e0")
        sci_frame7.pack(padx=50,pady=5)   
        sci_frame7.pack_propagate(False)
        # field_7
        std_em_lbl = Label(sci_frame7,text="Email:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        std_em_lbl.pack(side="left",anchor="n",padx=77)

        std_em_entry = ttk.Entry(sci_frame7,textvariable=self.var_email,font=("new times roman",12,"bold"),width=30)
        std_em_entry.pack(side="left",anchor="n")

        # sci_frame8
        sci_frame8 = Frame(si_frame, width=650, height=30,bg="#6bb5e0")
        sci_frame8.pack(padx=50,pady=5)   
        sci_frame8.pack_propagate(False)
        # field_8
        std_pn_lbl = Label(sci_frame8,text="Phone No:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        std_pn_lbl.pack(side="left",anchor="n",padx=60)

        std_pn_entry = ttk.Entry(sci_frame8,textvariable=self.var_phoneno,font=("new times roman",12,"bold"),width=30)
        std_pn_entry.pack(side="left",anchor="n")

        # sci_frame9 Address
        sci_frame9 = Frame(si_frame, width=650, height=65,bg="#6bb5e0")
        sci_frame9.pack(padx=50,pady=5)   
        sci_frame9.pack_propagate(False)
        # field_9
        std_ad_lbl = Label(sci_frame9,text="Address:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        std_ad_lbl.pack(side="left",anchor="n",padx=65)

        self.std_ad_entry = Text(sci_frame9,font=("new times roman",12,"bold"),width=30,height=3)
        self.std_ad_entry.pack(side="left",anchor="n")
        # $$$$$$$$$$$$$ variable for address $$$$$$$$$$$$$ #
        # self.var_addr = self.std_ad_entry.get("1.0",END)

        # sci_frame10 buttons for photo
        sci_frame10 = Frame(si_frame, width=650, height=30,bg="#6bb5e0")
        sci_frame10.pack(padx=50,pady=5)   
        sci_frame10.pack_propagate(False)

 
        # field_10
        photo_btn1 = ctk.CTkRadioButton(sci_frame10,text="Take Photo Sample",font=("new times roman",15,"bold"),variable=self.var_radio,value="Yes",
                                        text_color="white",fg_color="yellow",hover_color="white")
        photo_btn1.pack(side="left",anchor="n",padx=100)
        photo_btn2 = ctk.CTkRadioButton(sci_frame10,text="No Photo Sample",font=("new times roman",15,"bold"),variable=self.var_radio,value="No",
                                        text_color="white",fg_color="yellow",hover_color="white")
        photo_btn2.pack(side="left",anchor="n")

        # var_pt.set("Radio")

        # sci_frame11 Main buttons
        sci_frame11 = Frame(si_frame, width=650, height=45,bg="#6bb5e0")
        sci_frame11.pack(padx=50,pady=5)   
        sci_frame11.pack_propagate(False)

        # field_11
        save_btn  = ctk.CTkButton(sci_frame11,text="SAVE",text_color="white",width=130,height=40,fg_color="dark green"
                                  ,cursor="hand2",command=self.add_data)
        save_btn.pack(side="left",anchor="n",padx=10)

        update_btn  = ctk.CTkButton(sci_frame11,text="UPDATE",text_color="white",width=130,height=40,fg_color="royal blue"
                                    ,cursor="hand2",command=self.updating_details)
        update_btn.pack(side="left",anchor="n",padx=10)

        del_btn  = ctk.CTkButton(sci_frame11,text="DELETE",text_color="white",width=130,height=40,fg_color="#C62828"
                                 ,cursor="hand2",command=self.delete_data)
        del_btn.pack(side="left",anchor="n",padx=10)
        
        clr_btn  = ctk.CTkButton(sci_frame11,text="CLEAR",text_color="white",width=130,height=40,fg_color="#424242"
                                 ,cursor="hand2",command=self.reset_fields)
        clr_btn.pack(side="left",anchor="n",padx=10)

        # sci_frame12 Main buttons
        sci_frame12 = Frame(si_frame, width=650, height=45,bg="#6bb5e0")
        sci_frame12.pack(padx=50,pady=5)   
        sci_frame12.pack_propagate(False)

        # field_12
        add_psample_btn  = ctk.CTkButton(sci_frame12,text="ADD PHOTO SAMPLE",text_color="white",width=150,height=40,fg_color="blue",
                                         cursor="hand2",command=self.generate_dataset)
        add_psample_btn.pack(side="left",anchor="n",padx=70)

        update_psample_btn  = ctk.CTkButton(sci_frame12,text="UPDATE PHOTO SAMPLE",text_color="white",width=150,height=40,
                                            fg_color="blue",cursor="hand2",command=self.update_photo_sample)
        update_psample_btn.pack(side="left",anchor="n",padx=70)



        # student details frame ...................................................................................................... #
        sdetails_frame = ctk.CTkFrame(self.root,width=735,height=578,corner_radius=20,fg_color="#6bb5e0")
        sdetails_frame.pack_propagate(False)
        sdetails_frame.place(x=775,y=200)

        # image for sdetails_lbl
        sdetails_img = ctk.CTkImage(Image.open("app_images/sdetails_icon.png"))

        sdetails_lbl = ctk.CTkLabel(sdetails_frame,text="View Student Details",font=("new times roman",20,"bold"),corner_radius=15,
                                    width=700,height=28,fg_color="blue",text_color="white",image=sdetails_img,compound="left",
                                    padx=10
                                    )
        sdetails_lbl.pack(pady=18)

        # frame for Search ................................. #
        search_frame = Frame(sdetails_frame, width=725, height=45,bg="gray",relief="ridge",borderwidth=2)
        search_frame.pack(pady=5)   
        search_frame.pack_propagate(False)

        # search_icon
        search_img = ctk.CTkImage(Image.open("app_images/search_icon.png"))
        search_lbl = ctk.CTkLabel(search_frame,text="Search By:",width=50,height=30,font=("new times roman",15,"bold"),
                                  fg_color="red",text_color="white",image=search_img,compound="left",corner_radius=10
                                  )
        search_lbl.pack(side="left",anchor="n",pady=10)
        # search entry
        search_entry = ttk.Combobox(search_frame,font=("new times roman",13,"bold"),state="readonly",textvariable=self.var_search)
        search_entry["values"] = ("Student ID","Roll No","Student Name","Department","Course")
        search_entry.pack(side="left",anchor="n",pady=10,padx=5)
        search_entry.current(0)
        # item entry 
        item_entry = ctk.CTkEntry(search_frame,font=("new times roman",15,"bold"),
                                  width=200,border_color="black",textvariable=self.var_search_item)
        item_entry.pack(side="left",anchor="n",pady=10)
        # button for this search frame
        search_btn = ctk.CTkButton(search_frame,text="SEARCH",font=("new times roman",15,"bold"),fg_color="blue",
                                   width=80,height=40,cursor="hand2",command=self.search_data)
        search_btn.pack(side="left",anchor="n",pady=10,padx=5)

        show_btn = ctk.CTkButton(search_frame,text="SHOW ALL",font=("new times roman",15,"bold"),fg_color="green",
                                   width=80,height=40,cursor="hand2",command=self.fetch_data)
        show_btn.pack(side="left",anchor="n",pady=10,padx=5)

        # table frame ............................................. #
        table_frame = Frame(sdetails_frame,width=725,height=600,relief="ridge",borderwidth=2,bg="white")
        table_frame.pack_propagate(False)
        table_frame.pack(pady=10)
        # scrollbars
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("dept","course","year","sem","id",
                                                               "stdname","classdiv","rollno",
                                                               "gender","dob","email",
                                                               "phoneno","addr","photo"),xscrollcommand=scroll_x.set,
                                                               yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="right",fill="y")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Headers
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("stdname",text="Student Name")
        self.student_table.heading("classdiv",text="Class Division")
        self.student_table.heading("rollno",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date Of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phoneno",text="Phone No")
        self.student_table.heading("addr",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        # giving width

        self.student_table.column("dept",width=200,stretch=NO,anchor="center")
        self.student_table.column("course",width=200,stretch=0,anchor="center")
        self.student_table.column("year",width=200,stretch=0,anchor="center")
        self.student_table.column("sem",width=200,stretch=0,anchor="center")
        self.student_table.column("id",width=200,stretch=0,anchor="center")
        self.student_table.column("stdname",width=200,stretch=0,anchor="center")
        self.student_table.column("classdiv",width=200,stretch=0,anchor="center")
        self.student_table.column("rollno",width=200,stretch=0,anchor="center")
        self.student_table.column("gender",width=200,stretch=0,anchor="center")
        self.student_table.column("dob",width=200,stretch=0,anchor="center")
        self.student_table.column("email",width=200,stretch=0,anchor="center")
        self.student_table.column("phoneno",width=200,stretch=0,anchor="center")
        self.student_table.column("addr",width=200,stretch=0)
        self.student_table.column("photo",width=200,stretch=0,anchor="center")

        self.student_table.pack(fill="both",expand=1)
        self.student_table.bind('<ButtonRelease>',self.get_cursor)
        self.fetch_data()


    # adding the details
    def add_data(self):
        import datetime
        if self.var_dept.get() == '' or self.var_course.get() == '' or self.var_year.get() == '' or self.var_dob.get() == '' or self.var_email.get() == '' or self.var_gender.get() == 'Select Gender' or self.var_phoneno.get() == '' or self.var_rollno.get() == '' or self.var_sem.get() == '' or self.var_std_div.get() == '' or self.var_std_name.get() == '' or self.var_radio.get() == '' or self.std_ad_entry.get("1.0", "end").strip() == '':
            mb.showerror('Error', 'All fields are required!',parent=self.root)
            return
        
        std_id_input = self.var_std_id.get()
        std_rollno_input = self.var_rollno.get()
        if std_id_input.isdecimal() == False:
            mb.showerror("Invalid Student ID", "Please enter valid Student ID.",parent=self.root)
            return
        
        if std_rollno_input.isdecimal() == False:
            mb.showerror("Invalid Roll No", "Please enter valid Roll No.",parent=self.root)
            return
        
        dob_input = self.var_dob.get() 
        try:
            datetime.datetime.strptime(dob_input,"%Y-%m-%d")
        except:
            mb.showerror("Invalid Date", "Please enter date in this format : YYYY-MM-DD",parent=self.root)
            return

        email_input = self.var_email.get()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, email_input):
            mb.showerror("Invalid Email", "Please enter a valid email address.",parent=self.root)
            return
        
        phone_input = self.var_phoneno.get()
        if len(phone_input) != 10 or phone_input.isdecimal() == False:
            mb.showerror("Invalid Phone No", "Please enter valid Phone Number.",parent=self.root)
            return
        
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="smartattend")
            my_cursor = conn.cursor()

            insert_query = "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            insert_values = (
                self.var_dept.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_std_div.get(),
                self.var_rollno.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phoneno.get(),
                self.std_ad_entry.get("1.0",END),
                self.var_radio.get()
            )

            my_cursor.execute(insert_query,insert_values)
            conn.commit()
            self.fetch_data()
            mb.showinfo('Success','Student Record has been Added Successfully.',parent=self.root)
        except Exception as e:
            mb.showerror('DataBase Error',f'Something went wrong: {str(e)}',parent=self.root)
        finally:
            if conn.is_connected():
                conn.close()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ UPDATE $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def updating_details(self):
        import datetime
        if self.var_dept.get() == '' or self.var_course.get() == '' or self.var_year.get() == '' or self.var_dob.get() == '' or self.var_email.get() == '' or self.var_gender.get() == 'Select Gender' or self.var_phoneno.get() == '' or self.var_rollno.get() == '' or self.var_sem.get() == '' or self.var_std_div.get() == '' or self.var_std_name.get() == '' or self.var_radio.get() == '' or self.std_ad_entry.get("1.0", "end").strip() == '':
            mb.showerror('Error', 'All fields are required!',parent=self.root)
            return
        std_id_input = self.var_std_id.get()
        std_rollno_input = self.var_rollno.get()
        if std_id_input.isdecimal() == False:
            mb.showerror("Invalid Student ID", "Please enter valid Student ID.",parent=self.root)
            return

        if std_rollno_input.isdecimal() == False:
            mb.showerror("Invalid Roll No", "Please enter valid Roll No.",parent=self.root)
            return
        
        dob_input = self.var_dob.get() 
        try:
            datetime.datetime.strptime(dob_input,"%Y-%m-%d")
        except:
            mb.showerror("Invalid Date", "Please enter date in this format : YYYY-MM-DD",parent=self.root)
            return

        email_input = self.var_email.get()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, email_input):
            mb.showerror("Invalid Email", "Please enter a valid email address.",parent=self.root)
            return
        
        phone_input = self.var_phoneno.get()
        if len(phone_input) != 10 or phone_input.isdecimal() == False:
            mb.showerror("Invalid Phone No", "Please enter valid Phone Number.",parent=self.root)
            return
        
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="smartattend")
            my_cursor = conn.cursor()

            # $$$$$$$$$$$$$$$$$$$ Checking Student ID exist or not $$$$$$$$$$$$$$$$$$$ #

            query = "select std_id from student where std_id=%s"
            value = (std_id_input,)

            my_cursor.execute(query,value)
            result = my_cursor.fetchone()
            if not result:
                mb.showerror("Not Found",f"Student ID: {std_id_input} not found!",parent=self.root)
                return
            # $$$$$$$$$$$$$$$$$$$ Updating the record $$$$$$$$$$$$$$$$$$$ #
            v = mb.askyesno('Update','Do you want to update this student record ?',parent=self.root)
            if v:
                update_query = "update student set dept=%s,course=%s,year=%s,sem=%s,std_id=%s,std_name=%s,std_div=%s,rollno=%s,gender=%s,dob=%s,email=%s,phoneno=%s,addr=%s,photo_sample=%s where std_id=%s"
                update_values = (
                self.var_dept.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_std_div.get(),
                self.var_rollno.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phoneno.get(),
                self.std_ad_entry.get("1.0",END),
                self.var_radio.get(),
                self.var_std_id.get()
                )

                my_cursor.execute(update_query,update_values)
                conn.commit()
                self.fetch_data()
                mb.showinfo('Success','Student Record has been updated Successfully.',parent=self.root)
        except Exception as e:
            mb.showerror('DataBase Error',f'Something went wrong: {str(e)}',parent=self.root)
        finally:
            if conn.is_connected():
                conn.close()
        
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Delete Data $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def delete_data(self):
        import glob
        import os
        if self.var_std_id.get() == '':
            mb.showerror('Error', 'Please enter Student ID that you want to delete',parent=self.root)
            return
        
        std_id_input = self.var_std_id.get()
        if std_id_input.isdecimal() == False:
            mb.showerror("Invalid Student ID", "Please enter valid Student ID.",parent=self.root)
            return
        
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="smartattend")
            my_cursor = conn.cursor()

            # $$$$$$$$$$$$$$$$$$$ Checking Student ID exist or not $$$$$$$$$$$$$$$$$$$ #

            query = "select std_id from student where std_id=%s"
            value = (std_id_input,)

            my_cursor.execute(query,value)
            result = my_cursor.fetchone()
            if not result:
                mb.showerror("Not Found",f"Student ID: {std_id_input} not found!",parent=self.root)
                return
            # $$$$$$$$$$$$$$$$$$$ Deleting the record $$$$$$$$$$$$$$$$$$$ #
            v = mb.askyesno('Delete','Do you want to delete this student record ?',parent=self.root)
            if v:
                delete_query = "delete from student where std_id=%s"
                delete_value = (self.var_std_id.get(),)

                my_cursor.execute(delete_query,delete_value)
                conn.commit()
                old_images = glob.glob(f"data/std.{self.var_std_id.get()}.*.jpg")
                for img in old_images:
                    os.remove(img)
                self.fetch_data()
                self.reset_fields()
                mb.showinfo('Success','Student Record has been deleted Successfully.',parent=self.root)
        except Exception as e:
            mb.showerror('DataBase Error',f'Something went wrong: {str(e)}',parent=self.root)
        finally:
            if conn.is_connected():
                conn.close()
        
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Clear all fields $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def reset_fields(self):
        self.var_dept.set("")
        self.var_course.set("")
        self.var_year.set("")
        self.var_sem.set("")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_std_div.set("")
        self.var_rollno.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phoneno.set("")
        self.std_ad_entry.delete("1.0",END)
        self.var_radio.set("")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ fetching data for Tree $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def fetch_data(self):
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="smartattend")
            my_cursor = conn.cursor()

            my_cursor.execute("select * from student")
            data = my_cursor.fetchall()
            self.student_table.delete(*self.student_table.get_children())#I001 , I002
            if len(data) != 0:
                for i in data:
                    self.student_table.insert("",END,values=i)# values=()
                conn.commit()
        except Exception as e:
            mb.showerror('DataBase Error',f'Something went wrong: {str(e)}',parent=self.root)
        finally:
            if conn.is_connected():
                conn.close()


    # $$$$$$$$$$$$$$$$$$$$$$$$$$ Data display over the Fields $$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def get_cursor(self,event=""):
        try:
            cursor_row = self.student_table.focus()
            content = self.student_table.item(cursor_row)
            data = content["values"]
            if data:  
                self.var_dept.set(data[0])
                self.var_course.set(data[1])
                self.var_year.set(data[2])
                self.var_sem.set(data[3])
                self.var_std_id.set(data[4])
                self.var_std_name.set(data[5])
                self.var_std_div.set(data[6])
                self.var_rollno.set(data[7])
                self.var_gender.set(data[8])
                self.var_dob.set(data[9])
                self.var_email.set(data[10])
                self.var_phoneno.set(data[11])
                self.std_ad_entry.delete("1.0",END)
                self.std_ad_entry.insert("1.0",data[12])
                self.var_radio.set(data[13])
        except Exception as e:
            mb.showerror("Error",f"Error in get_cursor: {str(e)}",parent=self.root)

    # $$$$$$$$$$$$$$$$$$$$$$$ Take Photo Sample $$$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def generate_dataset(self):
        if self.var_std_id.get() == '':
            mb.showerror('Error', 'Please enter Student ID!',parent=self.root)
            return
        std_id_input = self.var_std_id.get()
        if std_id_input.isdecimal() == False:
            mb.showerror("Invalid Student ID", "Please enter valid Student ID.",parent=self.root)
            return
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="smartattend")
            my_cursor = conn.cursor()

            # $$$$$$$$$$$$$$$$$$$ Checking Student ID exist or not $$$$$$$$$$$$$$$$$$$ #

            query = "select std_id from student where std_id=%s"
            value = (std_id_input,)

            my_cursor.execute(query,value)
            result = my_cursor.fetchone()
            if not result:
                mb.showerror("Not Found",f"Student ID: {std_id_input} not found!",parent=self.root)
                return
            
            # $$$$$$$$$$$$$$$$$$$ Checking sample already taken or not $$$$$$$$$$$$$$$$$$$ #

            query2 = "select photo_sample from student where std_id=%s"
            value2 = (std_id_input,)

            my_cursor.execute(query2,value2)
            result2 = my_cursor.fetchone()
            
            if result2[0] == "Yes":
                mb.showerror("Already Taken",f"Sample for Student ID:{std_id_input} already taken!",parent=self.root)
                return
            
            # $$$$$$$$$$$$$$$$$$$ Taking the sample $$$$$$$$$$$$$$$$$$$ #

            update_query = "update student set photo_sample=%s where std_id=%s"
            update_values = ("Yes",std_id_input)
            my_cursor.execute(update_query,update_values)
            conn.commit()
            self.fetch_data()
            # self.reset_fields()
            print("success")
        except Exception as e:
            mb.showerror('DataBase Error',f'Something went wrong: {str(e)}',parent=self.root)
        finally:
            if conn.is_connected():
                conn.close()

        # $$$$$$$$$$$$$$$$$$ Load predefined data $$$$$$$$$$$$$$$$$$$$$$ #

        modelFile = "res10_300x300_ssd_iter_140000.caffemodel"
        configFile = "deploy.prototxt.txt"
        net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

        def face_cropped(img):
            h, w = img.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
            net.setInput(blob)
            detections = net.forward()

            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.50:   # confidence threshold
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (x1, y1, x2, y2) = box.astype("int")
                    return img[y1:y2, x1:x2]   # return cropped face

            return None


        # ====== SAMPLE CAPTURE LOGIC (same as before) ======
        cap = cv2.VideoCapture(0)
        img_id = 0
        max_samples = 100
        batch_size = 20  # each 's' press will save 20 images

        while True:
            ret, my_frame = cap.read()
            cv2.imshow("Frame", my_frame)

            key = cv2.waitKey(1)

            # When user presses 's'
            if key == ord('s') and img_id < max_samples:
                count = 0
                while count < batch_size and img_id < max_samples:
                    ret, my_frame = cap.read()
                    face = face_cropped(my_frame)

                    if face is not None:
                        img_id += 1
                        count += 1
                        face = cv2.resize(face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        file_name_path = "data/std." + str(self.var_std_id.get()) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)

                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                        cv2.imshow("Cropped Face", face)
                        cv2.waitKey(100)


            # Press Enter to exit early
            if key == 13 or img_id == max_samples:
                break

        cap.release()
        cv2.destroyAllWindows()
        mb.showinfo("Result", "Data set generation completed!", parent=self.root)
        self.reset_fields()
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ updating photo sample $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def update_photo_sample(self):
        import glob
        import os
        if self.var_std_id.get() == '':
            mb.showerror('Error', 'Please enter Student ID!',parent=self.root)
            return
        std_id_input = self.var_std_id.get()
        if std_id_input.isdecimal() == False:
            mb.showerror("Invalid Student ID", "Please enter valid Student ID.",parent=self.root)
            return
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="smartattend")
            my_cursor = conn.cursor()

            # $$$$$$$$$$$$$$$$$$$ Checking Student ID exist or not $$$$$$$$$$$$$$$$$$$ #

            query = "select std_id from student where std_id=%s"
            value = (std_id_input,)

            my_cursor.execute(query,value)
            result = my_cursor.fetchone()
            if not result:
                mb.showerror("Not Found",f"Student ID: {std_id_input} not found!",parent=self.root)
                return
            # $$$$$$$$$$$$$$$$$$$ Checking sample already taken or not $$$$$$$$$$$$$$$$$$$ #
            query2 = "select photo_sample from student where std_id=%s"
            value2 = (std_id_input,)

            my_cursor.execute(query2,value2)
            result2 = my_cursor.fetchone()
            
            if result2[0] == "No":
                mb.showerror("Sample Not Taken",f"Sample for Student ID:{std_id_input} Not taken!",parent=self.root)
                return
        except Exception as e:
            mb.showerror('DataBase Error',f'Something went wrong: {str(e)}',parent=self.root)
        finally:
            if conn.is_connected():
                conn.close()
        # $$$$$$$$$$$$$$$$$$$ updating the sample $$$$$$$$$$$$$$$$$$$ #
        try:
            v = mb.askyesno("Answer",f"Do want to update the sample for Student ID:{std_id_input}",parent=self.root)
            if v:    
                old_images = glob.glob(f"data/std.{self.var_std_id.get()}.*.jpg")
                for img in old_images:
                    os.remove(img)
                # $$$$$$$$$$$$$$$$$$ Load predefined data $$$$$$$$$$$$$$$$$$$$$$ #

                modelFile = "res10_300x300_ssd_iter_140000.caffemodel"
                configFile = "deploy.prototxt.txt"
                net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

                def face_cropped(img):
                    h, w = img.shape[:2]
                    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
                    net.setInput(blob)
                    detections = net.forward()

                    for i in range(0, detections.shape[2]):
                        confidence = detections[0, 0, i, 2]
                        if confidence > 0.50:   # confidence threshold
                            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                            (x1, y1, x2, y2) = box.astype("int")
                            return img[y1:y2, x1:x2]   # return cropped face

                    return None


                # ====== SAMPLE CAPTURE LOGIC (same as before) ======
                cap = cv2.VideoCapture(0)
                img_id = 0
                max_samples = 100
                batch_size = 20  # each 's' press will save 20 images

                while True:
                    ret, my_frame = cap.read()
                    cv2.imshow("Frame", my_frame)

                    key = cv2.waitKey(1)

                    # When user presses 's'
                    if key == ord('s') and img_id < max_samples:
                        count = 0
                        while count < batch_size and img_id < max_samples:
                            ret, my_frame = cap.read()
                            face = face_cropped(my_frame)

                            if face is not None:
                                img_id += 1
                                count += 1
                                face = cv2.resize(face, (450, 450))
                                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                                file_name_path = "data/std." + str(self.var_std_id.get()) + "." + str(img_id) + ".jpg"
                                cv2.imwrite(file_name_path, face)

                                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                                cv2.imshow("Cropped Face", face)
                                cv2.waitKey(100)


                    # Press Enter to exit early
                    if key == 13 or img_id == max_samples:
                        break

                cap.release()
                cv2.destroyAllWindows()
                mb.showinfo("Result", "Data set generation completed!", parent=self.root)
                self.reset_fields()
        except Exception as e:
            mb.showerror("Error in Updating the Sample",f"Something went wrong:{str(e)}",parent=self.root)
            
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Search Function $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def search_data(self):
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="smartattend")
            my_cursor = conn.cursor()
        except Exception as e:
            mb.showerror("DataBase Error",f"Something went wrong: {str(e)}",parent=self.root)
            return
        # $$$$$$$$$$$$$$$$$ Student ID $$$$$$$$$$$$$$$$ #
        if self.var_search.get() == "Student ID":
            std_id_input = self.var_search_item.get()
            if std_id_input == "":
                mb.showerror("Error","Enter search item!",parent=self.root)
                return
            if std_id_input.isdecimal() == False:
                mb.showerror("Invalid Student ID", "Please enter valid Student ID.",parent=self.root)
                return
            try:
                query = "select * from student where std_id=%s"
                value = (std_id_input,)
                my_cursor.execute(query,value)
                result = my_cursor.fetchall()

                if not result:
                    mb.showerror("Not Found","Student ID not found!",parent=self.root)
                    return
                self.student_table.delete(*self.student_table.get_children())
                for i in result:
                    self.student_table.insert("",END,values=i)
            except Exception as e:
                mb.showerror("Error",f"An error occurr in displaying Student ID: {str(e)}")
        # $$$$$$$$$$$$$$$$$ Roll No $$$$$$$$$$$$$$$$ #
        if self.var_search.get() == "Roll No":
            roll_no_input = self.var_search_item.get()
            if roll_no_input == "":
                mb.showerror("Error","Enter search item!",parent=self.root)
                return
            if roll_no_input.isdecimal() == False:
                mb.showerror("Invalid Roll No", "Please enter valid Roll No.",parent=self.root)
                return
            try:
                query = "select * from student where rollno=%s"
                value = (roll_no_input,)
                my_cursor.execute(query,value)
                result = my_cursor.fetchall()

                if not result:
                    mb.showerror("Not Found","Roll No not found!",parent=self.root)
                    return
                self.student_table.delete(*self.student_table.get_children())
                for i in result:
                    self.student_table.insert("",END,values=i)
            except Exception as e:
                mb.showerror("Error",f"An error occurr in displaying Roll No: {str(e)}")
        # $$$$$$$$$$$$$$$$$ Student Name $$$$$$$$$$$$$$$$ #        
        if self.var_search.get() == "Student Name":
            std_name_input = self.var_search_item.get()
            if std_name_input == "":
                mb.showerror("Error","Enter search item!",parent=self.root)
                return
            try:
                query = "select * from student where std_name=%s"
                value = (std_name_input,)
                my_cursor.execute(query,value)
                result = my_cursor.fetchall()

                if not result:
                    mb.showerror("Not Found","Student Name not found!",parent=self.root)
                    return
                self.student_table.delete(*self.student_table.get_children())
                for i in result:
                    self.student_table.insert("",END,values=i)
            except Exception as e:
                mb.showerror("Error",f"An error occurr in displaying Student Name: {str(e)}")
        # $$$$$$$$$$$$$$$$$ Department $$$$$$$$$$$$$$$$ #        
        if self.var_search.get() == "Department":
            dept_input = self.var_search_item.get()
            if dept_input == "":
                mb.showerror("Error","Enter search item!",parent=self.root)
                return
            try:
                query = "select * from student where dept=%s"
                value = (dept_input,)
                my_cursor.execute(query,value)
                result = my_cursor.fetchall()

                if not result:
                    mb.showerror("Not Found","Department not found!",parent=self.root)
                    return
                self.student_table.delete(*self.student_table.get_children())
                for i in result:
                    self.student_table.insert("",END,values=i)
            except Exception as e:
                mb.showerror("Error",f"An error occurr in displaying Department: {str(e)}")
        # $$$$$$$$$$$$$$$$$ Course $$$$$$$$$$$$$$$$ #        
        if self.var_search.get() == "Course":
            course_input = self.var_search_item.get()
            if course_input == "":
                mb.showerror("Error","Enter search item!",parent=self.root)
                return
            try:
                query = "select * from student where course=%s"
                value = (course_input,)
                my_cursor.execute(query,value)
                result = my_cursor.fetchall()

                if not result:
                    mb.showerror("Not Found","Course not found!",parent=self.root)
                    return
                self.student_table.delete(*self.student_table.get_children())
                for i in result:
                    self.student_table.insert("",END,values=i)
            except Exception as e:
                mb.showerror("Error",f"An error occurr in displaying Course: {str(e)}")
if __name__ == '__main__':
    root = Tk()
    s = Student_detail(root)
    root.mainloop()
