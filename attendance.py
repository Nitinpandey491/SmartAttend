from tkinter import *
import customtkinter as ctk
from tkinter import ttk
from PIL import Image,ImageTk
from PIL.Image import Resampling
from tkinter import messagebox as mb
from tkinter import filedialog
import os
import csv


class Attendance:
    def __init__(self,root):
        self.root = root

        # variables
        self.var_dept = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_rollno = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_sub = StringVar()
        self.var_st = StringVar()
        self.var_fac = StringVar()
        self.var_atd_status = StringVar()
        self.var_search = StringVar()
        self.var_search_item = StringVar()

        # variable for csv rows 
        self.mydata = []

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

        # attendance management frame label
        ad_frame = ctk.CTkFrame(self.root,width=1536,height=80,border_color="light blue",border_width=3,fg_color="#6A89A7")
        ad_frame.place(x=0,y=100)
        ad_frame.pack_propagate(False)

        self.ad_img = ctk.CTkImage(Image.open("app_images/attendance_m_icon.png"),size=(30,30))

        ad_lbl = ctk.CTkLabel(ad_frame,text="ATTENDANCE MANAGEMENT",font=("new times roman",25,"bold"),text_color="white",
                              fg_color="#6A89A7",image=self.ad_img,compound="left",padx=10)
        ad_lbl.pack(pady=25,anchor='center')

        # attendance information frame ............................................................................................. #

        ai_frame = ctk.CTkScrollableFrame(self.root,width=700,height=470,corner_radius=20,fg_color="#6bb5e0",
                                          label_text="Attendance Information",label_font=("new times roman",20,"bold"),
                                          label_text_color="white",label_fg_color="blue",scrollbar_button_color="blue",
                                          scrollbar_button_hover_color="light blue")
        ai_frame.place(x=15,y=200)

        # attendance info img
        si_img = Image.open("app_images/attendance_icon.png")
        si_img = si_img.resize((20,20), Resampling.LANCZOS)
        self.si_img1 = ImageTk.PhotoImage(si_img)
        lbl_si_img = Label(self.root,image=self.si_img1,bg="blue")
        lbl_si_img.place(width=20,height=20,x=245,y=224)

        # form
         # ai_frame1
        ai_frame1 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame1.pack(padx=50,pady=10)   
        ai_frame1.pack_propagate(False)
        # field_1
        std_id_lbl = Label(ai_frame1,text="Student ID:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        std_id_lbl.pack(side="left",anchor="n",padx=75)

        std_id_entry = ttk.Entry(ai_frame1,textvariable=self.var_std_id,font=("new times roman",12,"bold"),width=30)
        std_id_entry.pack(side="left",anchor="n") 

        # ai_frame2
        ai_frame2 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame2.pack(padx=50,pady=10)   
        ai_frame2.pack_propagate(False)
        # field_2
        std_rn_lbl = Label(ai_frame2,text="Roll No:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        std_rn_lbl.pack(side="left",anchor="n",padx=85)

        std_rn_entry = ttk.Entry(ai_frame2,textvariable=self.var_rollno,font=("new times roman",12,"bold"),width=30)
        std_rn_entry.pack(side="left",anchor="n")

        # ai_frame3
        ai_frame3 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame3.pack(padx=50,pady=10)   
        ai_frame3.pack_propagate(False)
        # field_3
        std_name_lbl = Label(ai_frame3,text="Student Name:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        std_name_lbl.pack(side="left",anchor="n",padx=60)

        std_name_entry = ttk.Entry(ai_frame3,textvariable=self.var_std_name,font=("new times roman",12,"bold"),width=30)
        std_name_entry.pack(side="left",anchor="n")

        # ai_frame4
        ai_frame4 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame4.pack(padx=50,pady=10)   
        ai_frame4.pack_propagate(False)
        # field_4
        dept_lbl = Label(ai_frame4,text="Department:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        dept_lbl.pack(side="left",anchor="n",padx=70)

        dept_entry = ttk.Entry(ai_frame4,textvariable=self.var_dept,font=("new times roman",12,"bold"),width=30)
        dept_entry.pack(side="left",anchor="n")

        # ai_frame5
        ai_frame5 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame5.pack(padx=50,pady=10)   
        ai_frame5.pack_propagate(False)
        # field_5
        time_lbl = Label(ai_frame5,text="Time:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        time_lbl.pack(side="left",anchor="n",padx=95)

        time_entry = ttk.Entry(ai_frame5,textvariable=self.var_time,font=("new times roman",12,"bold"),width=30)
        time_entry.pack(side="left",anchor="n")

        # ai_frame6
        ai_frame6 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame6.pack(padx=50,pady=10)   
        ai_frame6.pack_propagate(False)
        # field_6
        date_lbl = Label(ai_frame6,text="Date:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        date_lbl.pack(side="left",anchor="n",padx=95)

        date_entry = ttk.Entry(ai_frame6,textvariable=self.var_date,font=("new times roman",12,"bold"),width=30)
        date_entry.pack(side="left",anchor="n")

        # ai_frame7
        ai_frame7 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame7.pack(padx=50,pady=10)   
        ai_frame7.pack_propagate(False)
        # field_7
        sub_lbl = Label(ai_frame7,text="Subject:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        sub_lbl.pack(side="left",anchor="n",padx=85)

        sub_entry = ttk.Entry(ai_frame7,textvariable=self.var_sub,font=("new times roman",12,"bold"),width=30)
        sub_entry.pack(side="left",anchor="n")

        # ai_frame8
        ai_frame8 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame8.pack(padx=50,pady=10)   
        ai_frame8.pack_propagate(False)
        # field_8
        st_lbl = Label(ai_frame8,text="Session Type:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        st_lbl.pack(side="left",anchor="n",padx=60)

        st_entry = ttk.Combobox(ai_frame8,textvariable=self.var_st,font=("new times roman",12,"bold"),width=28,state="readonly")
        st_entry["values"] = ("Select Session Type","Theory","Practical")
        st_entry.pack(side="left",anchor="n")
        st_entry.current(0)

        # ai_frame9
        ai_frame9 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame9.pack(padx=50,pady=10)   
        ai_frame9.pack_propagate(False)
        # field_9
        fac_lbl = Label(ai_frame9,text="Faculty:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        fac_lbl.pack(side="left",anchor="n",padx=85)

        fac_entry = ttk.Entry(ai_frame9,textvariable=self.var_fac,font=("new times roman",12,"bold"),width=30)
        fac_entry.pack(side="left",anchor="n")

        # ai_frame10
        ai_frame10 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame10.pack(pady=10)   
        ai_frame10.pack_propagate(False)     
        # field_10
        atd_status_lbl = Label(ai_frame10,text="Attendance Status:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        atd_status_lbl.pack(side="left",anchor="n",padx=55)

        atd_status_entry = ttk.Combobox(ai_frame10,textvariable=self.var_atd_status,font=("new times roman",12,"bold"),width=28,state="readonly")
        atd_status_entry["values"] = ("Status","Present","Absent")
        atd_status_entry.pack(side="left",anchor="n")
        atd_status_entry.current(0)

         # ai_frame11 Main buttons
        ai_frame11 = Frame(ai_frame, width=650, height=45,bg="#6bb5e0")
        ai_frame11.pack(padx=50,pady=20)   
        ai_frame11.pack_propagate(False)

        # field_11
        imp_btn  = ctk.CTkButton(ai_frame11,text="Import csv",text_color="white",width=130,height=40,fg_color="dark green"
                                  ,cursor="hand2",command=self.import_csv)
        imp_btn.pack(side="left",anchor="n",padx=10)

        exp_btn  = ctk.CTkButton(ai_frame11,text="Export csv",text_color="white",width=130,height=40,fg_color="royal blue"
                                    ,cursor="hand2",command=self.export_csv)
        exp_btn.pack(side="left",anchor="n",padx=10)

        up_btn  = ctk.CTkButton(ai_frame11,text="Update",text_color="white",width=130,height=40,fg_color="#C62828"
                                 ,cursor="hand2",command=self.update_data)
        up_btn.pack(side="left",anchor="n",padx=10)
        
        clr_btn  = ctk.CTkButton(ai_frame11,text="Clear",text_color="white",width=130,height=40,fg_color="#424242"
                                 ,cursor="hand2",command=self.reset_fields)
        clr_btn.pack(side="left",anchor="n",padx=10)

         # attendance details frame ...................................................................................................... #
        adetails_frame = ctk.CTkFrame(self.root,width=735,height=578,corner_radius=20,fg_color="#6bb5e0")
        adetails_frame.pack_propagate(False)
        adetails_frame.place(x=775,y=200)

        # image for sdetails_lbl
        adetails_img = ctk.CTkImage(Image.open("app_images/sdetails_icon.png"))

        adetails_lbl = ctk.CTkLabel(adetails_frame,text="View Attendance Details",font=("new times roman",20,"bold"),corner_radius=15,
                                    width=700,height=28,fg_color="blue",text_color="white",image=adetails_img,compound="left",
                                    padx=10
                                    )
        adetails_lbl.pack(pady=18)

        # frame for Search ................................. #
        search_frame = Frame(adetails_frame, width=725, height=45,bg="gray",relief="ridge",borderwidth=2)
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
        search_entry["values"] = ("Student ID","Roll No","Student Name","Department")
        search_entry.pack(side="left",anchor="n",pady=10,padx=5)
        search_entry.current(0)
        # item entry 
        item_entry = ctk.CTkEntry(search_frame,font=("new times roman",15,"bold"),
                                  width=200,border_color="black",textvariable=self.var_search_item,placeholder_text_color="gray"
                                  )
        item_entry.pack(side="left",anchor="n",pady=10)
        # button for this search frame
        search_btn = ctk.CTkButton(search_frame,text="SEARCH",font=("new times roman",15,"bold"),fg_color="blue",
                                   width=80,height=40,cursor="hand2",command=self.search_data)
        search_btn.pack(side="left",anchor="n",pady=10,padx=5)

        show_btn = ctk.CTkButton(search_frame,text="SHOW ALL",font=("new times roman",15,"bold"),fg_color="green",
                                   width=80,height=40,cursor="hand2",command=self.show_all)
        show_btn.pack(side="left",anchor="n",pady=10,padx=5)

         # table frame ............................................. #
        table_frame = Frame(adetails_frame,width=725,height=600,relief="ridge",borderwidth=2,bg="white")
        table_frame.pack_propagate(False)
        table_frame.pack(pady=10)
        # scrollbars
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=(1,2,3,4,5,6,7,8,9,10),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="right",fill="y")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Headers
        self.student_table.heading(1,text="Student ID")
        self.student_table.heading(2,text="Roll No")
        self.student_table.heading(3,text="Name")
        self.student_table.heading(4,text="Department")
        self.student_table.heading(5,text="Time")
        self.student_table.heading(6,text="Date")
        self.student_table.heading(7,text="Subject")
        self.student_table.heading(8,text="Session Type")
        self.student_table.heading(9,text="Faculty")
        self.student_table.heading(10,text="Attendacne Status")
        self.student_table["show"] = "headings"
        # width
        self.student_table.column(1,width=200,stretch=NO,anchor="center")
        self.student_table.column(2,width=200,stretch=NO,anchor="center")
        self.student_table.column(3,width=200,stretch=NO,anchor="center")
        self.student_table.column(4,width=200,stretch=NO,anchor="center")
        self.student_table.column(5,width=200,stretch=NO,anchor="center")
        self.student_table.column(6,width=200,stretch=NO,anchor="center")
        self.student_table.column(7,width=200,stretch=NO,anchor="center")
        self.student_table.column(8,width=200,stretch=NO,anchor="center")
        self.student_table.column(9,width=200,stretch=NO,anchor="center")
        self.student_table.column(10,width=200,stretch=NO,anchor="center")
        self.student_table.pack(fill="both",expand=1)

        self.student_table.bind('<ButtonRelease>',self.get_cursor)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ fetch data from csv $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
    def fetch_data(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows[1:]:
            self.student_table.insert("",END,values=i)
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Import csv $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
    def import_csv(self):
        try:
            fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All files","*.*")),parent=self.root)

            if not fln:
                return 
        
            with open(fln) as myfile:
                self.mydata.clear()
                csvread = csv.reader(myfile,delimiter=",")
                for i in csvread:
                    self.mydata.append(i)
                self.fetch_data(self.mydata)
        except Exception as e:
            mb.showerror("Error","Please select an csv file!",parent=self.root)
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Export csv $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
    def export_csv(self):
        try:
            if len(self.mydata) < 1:
                mb.showerror("No Data",f"No data found to export",parent=self.root)
                return
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV As",filetypes=(("CSV File","*.csv"),("All files","*.*")),defaultextension=".csv",parent=self.root)
            
            if not fln:
                return
            
            with open(fln,"w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in self.mydata:
                    exp_write.writerow(i)
                mb.showinfo("Success",f"Your data exported to: {os.path.basename(fln)} successfully",parent=self.root)
        except Exception as e:
            mb.showerror("Error",f"Something went wrong: {str(e)}",parent=self.root)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$ Data display over the Fields $$$$$$$$$$$$$$$$$$$$$$$$$$ #
    def get_cursor(self,event=""):
        try:
            cursor_row = self.student_table.focus()
            content = self.student_table.item(cursor_row)
            data = content["values"]
            if data:
                self.var_std_id.set(data[0])
                self.var_rollno.set(data[1])
                self.var_std_name.set(data[2])
                self.var_dept.set(data[3])
                self.var_time.set(data[4])
                self.var_date.set(data[5])
                self.var_sub.set(data[6])
                self.var_st.set(data[7])
                self.var_fac.set(data[8])
                self.var_atd_status.set(data[9])
            # else:
            #     print("no row selected")
        except Exception as e:
            mb.showerror("Error",f"Error in get_cursor: {str(e)}",parent=self.root)
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Clear all fields $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
    def reset_fields(self):
         self.var_std_id.set("")
         self.var_rollno.set("")
         self.var_std_name.set("")
         self.var_dept.set("")
         self.var_time.set("")
         self.var_date.set("")
         self.var_sub.set("")
         self.var_st.set("Select Session Type")
         self.var_fac.set("")
         self.var_atd_status.set("Status")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Update csv $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def update_data(self):
        import datetime
        if len(self.mydata) < 1:
                mb.showerror("No Data",f"No data found to update",parent=self.root)
                return
        if (not self.var_std_id.get() or not self.var_rollno.get() or not self.var_std_name.get() or 
            not self.var_dept.get() or not self.var_time.get() or not self.var_date.get() or 
            not self.var_sub.get() or self.var_st.get() == "Select Session Type" or 
            not self.var_fac.get() or self.var_atd_status.get() == "Status"):
            
            mb.showerror("Error", "All fields are required!", parent=self.root)
            return
        std_id_input = self.var_std_id.get()
        std_rollno_input = self.var_rollno.get()
        if std_id_input.isdecimal() == False:
            mb.showerror("Invalid Student ID", "Please enter valid Student ID.",parent=self.root)
            return
        
        if std_rollno_input.isdecimal() == False:
            mb.showerror("Invalid Roll No", "Please enter valid Roll No.",parent=self.root)
            return
        try:
            try:
                time_intput = self.var_time.get()
                datetime.datetime.strptime(time_intput,"%H:%M:%S")
            except:
                 mb.showerror("Invalid Time","Please enter time in 24 hrs format: Hour:Minute:Second")
                 return
            date_input = self.var_date.get()
            datetime.datetime.strptime(date_input,"%d-%m-%Y")
        except:
             mb.showerror("Invalid Date","Please enter date in this format: dd-mm-yyyy")
             return
        try:
            updated = False
            for i, row in enumerate(self.mydata):
                if row[0] == self.var_std_id.get():
                    self.mydata[i] = [
                        self.var_std_id.get(),
                        self.var_rollno.get(),
                        self.var_std_name.get(),
                        self.var_dept.get(),
                        self.var_time.get(),
                        self.var_date.get(),
                        self.var_sub.get(),
                        self.var_st.get(),
                        self.var_fac.get(),
                        self.var_atd_status.get()
                    ]
                    updated = True
                    break
            
            if updated:
                self.fetch_data(self.mydata)
                mb.showinfo("Success", "Attendance record updated in table\nPlease export to save changes to a new CSV file.", parent=self.root)
            else:
                mb.showerror("Error", "Student ID not found!", parent=self.root)
        except Exception as e:
            mb.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)
    
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Search $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
    def search_data(self):
        if len(self.mydata) < 1:
                mb.showerror("No Data",f"No data found",parent=self.root)
                return
        std_id_index = 0
        std_rollno_index = 1
        std_name_index = 2
        std_dept_index = 3
        # $$$$$$$$$$$$$$$$$ Student ID $$$$$$$$$$$$$$$$ #
        if self.var_search.get() == "Student ID":
            data = []
            std_id_input = self.var_search_item.get()
            if std_id_input == "":
                mb.showerror("Error","Enter search item!",parent=self.root)
                return
            if std_id_input.isdecimal() == False:
                mb.showerror("Invalid Student ID", "Please enter valid Student ID.",parent=self.root)
                return
            try:
                id_found = False
                for row in self.mydata[1:]:
                    if std_id_input == row[0]:
                        data.append(row)
                        id_found = True
                if not id_found:
                    mb.showerror("Not Found","Student ID not found!",parent=self.root)
                    return
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
            except Exception as e:
                mb.showerror("Error",f"An error occurr in displaying Student ID: {str(e)}")
        # $$$$$$$$$$$$$$$$$ Roll No $$$$$$$$$$$$$$$$ #        
        if self.var_search.get() == "Roll No":
            data = []
            roll_no_input = self.var_search_item.get()
            if roll_no_input == "":
                mb.showerror("Error","Enter search item!",parent=self.root)
                return
            if roll_no_input.isdecimal() == False:
                mb.showerror("Invalid Roll No", "Please enter valid Roll No.",parent=self.root)
                return
            try:
                roll_no_found = False
                for row in self.mydata:
                    if roll_no_input == row[1]:
                        data.append(row)
                        roll_no_found = True
                if not roll_no_found:
                    mb.showerror("Not Found","Roll No not found!",parent=self.root)
                    return
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
            except Exception as e:
                mb.showerror("Error",f"An error occurr in displaying Roll No: {str(e)}")        
        # $$$$$$$$$$$$$$$$$ Student Name $$$$$$$$$$$$$$$$ #        
        if self.var_search.get() == "Student Name":
            data = []
            std_name_input = self.var_search_item.get()
            if std_name_input == "":
                mb.showerror("Error","Enter search item!",parent=self.root)
                return
            try:
                std_name_found = False
                for row in self.mydata:
                    if std_name_input == row[2]:
                        data.append(row)
                        std_name_found = True
                if not std_name_found:
                    mb.showerror("Not Found","Student Name not found!",parent=self.root)
                    return
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
            except Exception as e:
                mb.showerror("Error",f"An error occurr in displaying Student Name: {str(e)}") 
        # $$$$$$$$$$$$$$$$$ Department $$$$$$$$$$$$$$$$ #        
        if self.var_search.get() == "Department":
            data = []
            dept_input = self.var_search_item.get()
            if dept_input == "":
                mb.showerror("Error","Enter search item!",parent=self.root)
                return
            try:
                dept_found = False
                for row in self.mydata:
                    if dept_input == row[3]:
                        data.append(row)
                        dept_found = True
                if not dept_found:
                    mb.showerror("Not Found","Department not found!",parent=self.root)
                    return
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
            except Exception as e:
                mb.showerror("Error",f"An error occurr in displaying Department: {str(e)}")
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Show All $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ # 
    def show_all(self):
        if len(self.mydata) < 1:
                mb.showerror("No Data",f"No data found",parent=self.root)
                return
        self.fetch_data(self.mydata)
if __name__ == '__main__':
    root = Tk()
    a = Attendance(root)
    root.mainloop()