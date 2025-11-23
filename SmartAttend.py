from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from PIL.Image import Resampling
from tkinter import messagebox as mb
import re
import mysql.connector



class Login_Window:
    def __init__(self,root):
        self.root = root

        # variables
        self.var_email = StringVar()
        self.var_pwd = StringVar()

    def create_all(self):

        # logo
        self.icon_image = PhotoImage(file="app_images/logo.png")
        self.root.iconphoto(False, self.icon_image)

        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.configure(background="#384959")

        # image_lbl_bg = Image.open("login_bg.jpg")
        # image_lbl_bg = image_lbl_bg.resize((1550,800), Resampling.LANCZOS)
        # self.bg = ImageTk.PhotoImage(image_lbl_bg)
        # lbl_bg = Label(self,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # 1 #6A89A7 2 #BDDDFC 3 #88BDF2 4 #384959

        # login form frame
        self.frame = Frame(self.root,bg="#6A89A7")
        self.frame.place(x=610,y=200,width=340,height=450) # y=170

        # person image
        img1 = Image.open("app_images/image1.png")
        img1 = img1.resize((100,100), Resampling.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(self.root,image=self.photo1,bg="#6A89A7")
        lbl_img1.place(width=100,height=100,x=730,y=205)

        lgn_hr = Label(self.frame,text="LOGIN HERE",font=("new times roman",20,"bold"),bg="#6A89A7",fg="white")
        lgn_hr.place(x=85,y=105)

        # email
        email = Label(self.frame,text="Email",font=("new times roman",15,"bold"),bg="#6A89A7",fg="white")
        email.place(x=70,y=155)
        self.email_entry = ttk.Entry(self.frame,font=("new times roman",15,"bold"),textvariable=self.var_email)
        self.email_entry.place(x=40,y=185,width=270)

         # password
        password = Label(self.frame,text="Password",font=("new times roman",15,"bold"),bg="#6A89A7",fg="white")
        password.place(x=70,y=230)
        self.pwd_entry = ttk.Entry(self.frame,font=("new times roman",15,"bold"),textvariable=self.var_pwd,show="*")
        self.pwd_entry.place(x=40,y=260,width=270)

        # icons
        img2 = Image.open("app_images/image1.png")
        img2 = img2.resize((25,25), Resampling.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.frame,image=self.photo2,bg="#6A89A7")
        lbl_img2.place(width=25,height=25,x=40,y=158)

        img3 = Image.open("app_images/image2.png")
        img3 = img3.resize((40,40), Resampling.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(self.frame,image=self.photo3,bg="#6A89A7")
        lbl_img3.place(width=25,height=25,x=40,y=234)
    
        # login button
        loginbtn = Button(self.frame,cursor="hand2",text="LOGIN",font=("new times roman",15,"bold"),fg="white",bg="#2ea9f0",relief=RIDGE,bd=3,activeforeground="white",activebackground="#2ea9f0",command=self.verify)
        loginbtn.place(width=120,height=35,x=110,y=320)

        # register button
        registerbtn = Button(self.frame,cursor="hand2",text="REGISTER",font=("new times roman",10,"bold"),fg="white",bg="#6A89A7",borderwidth=0,activeforeground="white",activebackground="#6A89A7",command=self.open_register_window)
        registerbtn.place(width=90,x=15,y=370)
  
        # forget password button
        forgetpwdbtn = Button(self.frame,cursor="hand2",text="FORGET PASSWORD",font=("new times roman",10,"bold"),fg="white",bg="#6A89A7",borderwidth=0,activeforeground="white",activebackground="#6A89A7",command=self.open_forget_password_window)
        forgetpwdbtn.place(width=160,x=15,y=405)

    def main_logo(self):
        
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

    def verify(self):
        from super_admin import Super_Admin
        from main import Main

        if self.var_email.get() == '' or self.var_pwd.get() == '':
            mb.showerror('Error', 'All fields are required!')
            return

        email_input = self.var_email.get()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, email_input):
            mb.showerror("Invalid Email", "Please enter a valid email address.")
            return
        
        conn = None # prevents program from crashing
        try:
            conn = mysql.connector.connect(host="localhost",user="root",password="admin",database="smartattend")
            db_cursor = conn.cursor()

            query_1 = "select * from superadmin where email=%s and password=%s"
            value_1 = (self.var_email.get(),self.var_pwd.get())

            db_cursor.execute(query_1,value_1)
            row1 = db_cursor.fetchone()

            query_2 = "select * from register where email=%s and password=%s"
            value_2 = (self.var_email.get(),self.var_pwd.get())

            db_cursor.execute(query_2,value_2)
            row2 = db_cursor.fetchone()

            if row1 is not None:
                v = mb.askyesno('Success',f"welcome {self.var_email.get()} click 'Yes' to continue")
                if v:
                    self.var_email.set("")
                    self.var_pwd.set("")
                    root3 = Toplevel(self.root)
                    sa = Super_Admin(root3)
            elif row2 is not None:
                v = mb.askyesno('Success',f"welcome {self.var_email.get()} click 'Yes' to continue")
                if v:
                    self.var_email.set("")
                    self.var_pwd.set("")
                    root2 = Toplevel(self.root)
                    m = Main(root2)
                    m.clock()
            else:
                mb.showerror('Incorrect','Incorrect email and password')


        except Exception as e:
            mb.showerror('Database Error',f'Something went wrong: {str(e)}')
        finally:
            if conn.is_connected():
                conn.close()

    def open_register_window(self):
        from register import Register
        root5 = Toplevel(self.root)
        rg = Register(root5)


    def open_forget_password_window(self):
        from forget_p import Forget_password
        root4 = Toplevel(self.root)
        f = Forget_password(root4)




if __name__ == '__main__':
    root = Tk()
    lg = Login_Window(root)
    lg.create_all()
    lg.main_logo()
    root.mainloop()
