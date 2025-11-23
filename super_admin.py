from tkinter import *
import customtkinter as ctk
from tkinter import ttk
from PIL import Image,ImageTk
from PIL.Image import Resampling
from tkinter import messagebox as mb
import re
import mysql.connector

class Super_Admin:
    def __init__(self,root):
        self.root = root

        # variable
        self.var_email = StringVar()
        self.var_search_item = StringVar()

        # logo
        self.icon_image = PhotoImage(file="app_images/logo.png")
        self.root.iconphoto(False, self.icon_image)

        # geometry
        self.root.title("Super Admin")
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

        # admin management frame label

        ad_frame = ctk.CTkFrame(self.root,width=1536,height=80,border_color="light blue",border_width=3,fg_color="#6A89A7")
        ad_frame.place(x=0,y=100)
        ad_frame.pack_propagate(False)

        self.ad_img = ctk.CTkImage(Image.open("app_images/super_admin_icon.png"),size=(30,30))

        ad_lbl = ctk.CTkLabel(ad_frame,text="SUPER ADMIN",font=("new times roman",25,"bold"),text_color="white",
                              fg_color="#6A89A7",image=self.ad_img,compound="left",padx=10)
        ad_lbl.pack(pady=25,anchor='center')

        # admin management frame

        admin_management_frame = ctk.CTkFrame(self.root,width=600,height=250,corner_radius=20,fg_color="#6bb5e0")
        admin_management_frame.pack_propagate(False)
        admin_management_frame.place(x=100,y=350)

        admin_mg_img = ctk.CTkImage(Image.open("app_images/admin_mg_icon.png"))

        admin_mg_lbl = ctk.CTkLabel(admin_management_frame,text="Admin Management",font=("new times roman",20,"bold"),corner_radius=15,
                                    width=700,height=28,fg_color="blue",text_color="white",image=admin_mg_img,compound="left",
                                    padx=10
                                    )
        admin_mg_lbl.pack(padx=15,pady=18)


        # exit ----------------------------------------------------------------------------------------------

        # exit button
        e_image = ctk.CTkImage(Image.open("app_images/exit_icon.png"))
        e_btn = ctk.CTkButton(ad_frame,text="EXIT",width=100,height=40,corner_radius=20,
                               text_color="white",font=("new times roman",15,"bold"),border_color="white",hover_color="red",
                               cursor="hand2",border_width=2,image=e_image,compound="left",command=self.exit
                               )
                               
        e_btn.place(x=1410,y=20)

        # form field
        # admin_frame
        admin_frame = Frame(admin_management_frame, width=650, height=30,bg="#6bb5e0")
        admin_frame.pack(padx=70,pady=30)   
        admin_frame.pack_propagate(False)
        # field
        email_lbl = Label(admin_frame,text="Email:",fg="white",bg="#6bb5e0",font=("new times roman",15,"bold"))
        email_lbl.pack(side="left",anchor="n",padx=10)

        email_entry = ttk.Entry(admin_frame,textvariable=self.var_email,font=("new times roman",15,"bold"),width=30)
        email_entry.pack(side="left",anchor="n") 

        # buttons
        admin_frame2 = Frame(admin_management_frame, width=650, height=45,bg="#6bb5e0")
        admin_frame2.pack(padx=150,pady=20)   
        admin_frame2.pack_propagate(False)

        # field_11
        add_btn  = ctk.CTkButton(admin_frame2,text="Add",font=("new times roman",20,"bold"),text_color="white",width=130,height=40,fg_color="dark green"
                                  ,cursor="hand2",command=self.add_admin)
        add_btn.pack(side="left",anchor="n",padx=10)

        remove_btn  = ctk.CTkButton(admin_frame2,text="Remove",font=("new times roman",20,"bold"),text_color="white",width=130,height=40,fg_color="#C62828"
                                 ,cursor="hand2",command=self.remove_admin)
        remove_btn.pack(side="left",anchor="n",padx=10)


        # View Admins frame 

        admin_view_frame = ctk.CTkFrame(self.root,width=600,height=350,corner_radius=20,fg_color="#6bb5e0")
        admin_view_frame.pack_propagate(False)
        admin_view_frame.place(x=800,y=300)

        # image for sdetails_lbl
        adetails_img = ctk.CTkImage(Image.open("app_images/sdetails_icon.png"))

        adetails_lbl = ctk.CTkLabel(admin_view_frame,text="View Admins",font=("new times roman",20,"bold"),corner_radius=15,
                                    width=700,height=28,fg_color="blue",text_color="white",image=adetails_img,compound="left",
                                    padx=10
                                    )
        adetails_lbl.pack(padx=15,pady=18)

        
        # frame for Search ................................. #
        search_frame = Frame(admin_view_frame, width=590, height=45,bg="gray",relief="ridge",borderwidth=2)
        search_frame.pack(pady=5)   
        search_frame.pack_propagate(False)

        # search_icon
        search_img = ctk.CTkImage(Image.open("app_images/search_icon.png"))
        search_lbl = ctk.CTkLabel(search_frame,text="Search By:",width=50,height=30,font=("new times roman",15,"bold"),
                                  fg_color="red",text_color="white",image=search_img,compound="left",corner_radius=10
                                  )
        search_lbl.pack(side="left",anchor="n",pady=10)

        # email Label

        email_lbl = Label(search_frame,text="Email:",font=("new times roman",15,"bold"),fg="white",bg="grey")
        email_lbl.pack(side="left",padx=5)

        # item entry 
        item_entry = ctk.CTkEntry(search_frame,font=("new times roman",15,"bold"),
                                  width=200,border_color="black",textvariable=self.var_search_item)
        item_entry.pack(side="left",pady=10)

        # button for this search frame
        search_btn = ctk.CTkButton(search_frame,text="SEARCH",font=("new times roman",15,"bold"),fg_color="blue",
                                   width=80,height=40,cursor="hand2",command=self.search_data)
        search_btn.pack(side="left",anchor="n",pady=10,padx=5)

        show_btn = ctk.CTkButton(search_frame,text="SHOW ALL",font=("new times roman",15,"bold"),fg_color="green",
                                   width=80,height=40,cursor="hand2",command=self.show_all)
        show_btn.pack(side="left",anchor="n",pady=10,padx=5)

         # table frame ............................................. #
        table_frame = Frame(admin_view_frame,width=590,height=300,relief="ridge",borderwidth=2,bg="white")
        table_frame.pack_propagate(False)
        table_frame.pack(pady=10)
        # scrollbars
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.admin_table = ttk.Treeview(table_frame,columns=(1),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,style="Treeview")
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="right",fill="y")
        scroll_x.config(command=self.admin_table.xview)
        scroll_y.config(command=self.admin_table.yview)

        # Headers
        self.admin_table.heading(1,text="Admin")
        self.admin_table["show"] = "headings"
        # width
        self.admin_table.column(1,width=590,anchor="center",stretch=NO)
        self.admin_table.pack(fill="both",expand=1)
        self.admin_table.bind("<ButtonRelease>",self.get_cursor)
        self.show_all()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ADD $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def add_admin(self):
        if self.var_email.get() == "":
            mb.showerror('Empty Field', 'Please enter the email!',parent=self.root)
            return
        email_input = self.var_email.get()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, email_input):
            mb.showerror("Invalid Email", "Please enter a valid email address.",parent=self.root)
            return
        
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="smartattend")
            my_cursor = conn.cursor()

            insert_query = "insert into admin values(%s)"
            insert_values = (email_input,)

            my_cursor.execute(insert_query,insert_values)
            conn.commit()
            self.show_all()
            mb.showinfo('Success',f'Admin = {email_input} has been Added Successfully.',parent=self.root)
        except Exception as e:
            mb.showerror('DataBase Error',f'Something went wrong: {str(e)}',parent=self.root)
        finally:
            if conn.is_connected():
                conn.close()
    
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ REMOVE $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
    
    def remove_admin(self):
        if self.var_email.get() == "":
            mb.showerror('Empty Field', 'Please enter the email!',parent=self.root)
            return
        email_input = self.var_email.get()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, email_input):
            mb.showerror("Invalid Email", "Please enter a valid email address.",parent=self.root)
            return
        
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="smartattend")
            my_cursor = conn.cursor()

            check_query = "select * from admin where email=%s"
            check_value = (email_input,)
            my_cursor.execute(check_query,check_value)
            result = my_cursor.fetchone()

            if not result:
                mb.showerror("Not Found",f"Admin = { email_input} not found",parent=self.root)
                return
            
            v = mb.askyesno("Answer",f"Do you want to remove Admin = {email_input}",parent=self.root)
            if v:
                delete_query_1 = "delete from admin where email=%s"
                delete_values_1 = (email_input,)
                my_cursor.execute(delete_query_1,delete_values_1)

                delete_query_2 = "delete from register where email=%s"
                delete_values_2 = (email_input,)
                my_cursor.execute(delete_query_2,delete_values_2)

                conn.commit()
                self.show_all()
                mb.showinfo('Success',f'Admin = {email_input} has been Removed Successfully.',parent=self.root)
        except Exception as e:
            mb.showerror('DataBase Error',f'Something went wrong: {str(e)}',parent=self.root)
        finally:
            if conn.is_connected():
                conn.close()

        
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Search Function $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def search_data(self):
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="smartattend")
            my_cursor = conn.cursor()
        except Exception as e:
            mb.showerror("DataBase Error",f"Something went wrong: {str(e)}",parent=self.root)
            return
        
        if self.var_search_item.get() == "":
            mb.showerror('Empty Field', 'Please enter the email!',parent=self.root)
            return
        
        email_input = self.var_search_item.get()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, email_input):
            mb.showerror("Invalid Email", "Please enter a valid email address.",parent=self.root)
            return
        
        try:
            query = "select * from admin where email=%s"
            value = (email_input,)
            my_cursor.execute(query,value)
            result = my_cursor.fetchall()

            if not result:
                mb.showerror("Not Found","Admin not found!",parent=self.root)
                return
            self.admin_table.delete(*self.admin_table.get_children())
            for i in result:
                self.admin_table.insert("",END,values=i)
        except Exception as e:
            mb.showerror("Error",f"An error occurr in displaying Student ID: {str(e)}")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ fetching data for Tree $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def show_all(self):
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="smartattend")
            my_cursor = conn.cursor()

            my_cursor.execute("select * from admin")
            data = my_cursor.fetchall()
            self.admin_table.delete(*self.admin_table.get_children())#I001 , I002
            if len(data) != 0:
                for i in data:
                    self.admin_table.insert("",END,values=i)# values=()
                conn.commit()
        except Exception as e:
            mb.showerror('DataBase Error',f'Something went wrong: {str(e)}',parent=self.root)
        finally:
            if conn.is_connected():
                conn.close()

     # $$$$$$$$$$$$$$$$$$$$$$$$$$ Data display over the Fields $$$$$$$$$$$$$$$$$$$$$$$$$$ #

    def get_cursor(self,event=""):
        try:
            cursor_row = self.admin_table.focus()
            content = self.admin_table.item(cursor_row)
            data = content["values"]
            if data:  
                self.var_email.set(data[0])

        except Exception as e:
            mb.showerror("Error",f"Error in get_cursor: {str(e)}",parent=self.root)

    def exit(self):

        v = mb.askyesno('EXIT','Do you really want to exit ?',parent=self.root)
        if v:
            self.root.destroy()




if __name__ == '__main__':
    root = Tk()
    sa = Super_Admin(root)
    root.mainloop()