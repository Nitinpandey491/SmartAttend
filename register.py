from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from PIL.Image import Resampling
from tkinter import messagebox as mb
from re import *
import mysql.connector 

class Register:
    def __init__(self,root):
        self.root = root
    

        # variables
        self.var_email = StringVar()
        self.var_pwd = StringVar()
        self.var_cpwd = StringVar()


        # logo
        self.icon_image = PhotoImage(file="app_images/logo.png")
        self.root.iconphoto(False, self.icon_image)

        self.root.title("Register")
        self.root.geometry("1550x800+0+0")
        self.root.configure(background="#384959")

        # register frame 
        self.frame = Frame(self.root,bg="#6A89A7")
        self.frame.place(x=350,y=150,width=800,height=600) # y=180 , h=550

        rg_rh = Label(self.frame,text="REGISTER HERE",font=("new times roman",20,"bold"),bg="#6A89A7",fg="white")
        rg_rh.place(x=300,y=50)

        # register image 
        img1 = Image.open("app_images/rg.png")
        img1 = img1.resize((100,100), Resampling.LANCZOS )
        self.photo1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(self.frame,image=self.photo1,bg="#384959",relief=RIDGE)
        lbl_img1.place(x=0,y=0,width=100,height=100)

        img1_c = Image.open("app_images/rg.png")
        img1_c = img1_c.resize((100,100), Resampling.LANCZOS )
        self.photo1_c = ImageTk.PhotoImage(img1_c)
        lbl_img1_c= Label(self.frame,image=self.photo1_c,bg="#384959",relief=RIDGE)
        lbl_img1_c.place(x=700,y=0,width=100,height=100)

        # form
        self.email = Label(self.frame,text="Email:",font=("new times roman",15,"bold"),fg="white",bg="#6A89A7")
        self.email.place(x=300,y=170)
        self.email_entry = ttk.Entry(self.frame,textvariable=self.var_email,font=("new times roman",15,"bold"))
        self.email_entry.place(x=300,y=205,width=250)

        self.pwd = Label(self.frame,text="Password:",font=("new times roman",15,"bold"),fg="white",bg="#6A89A7")
        self.pwd.place(x=300,y=250)
        self.pwd_entry = ttk.Entry(self.frame,show='*',textvariable=self.var_pwd,font=("new times roman",15,"bold"))
        self.pwd_entry.place(x=300,y=285,width=250)

        self.cpwd = Label(self.frame,text="Confirm Password:",font=("new times roman",15,"bold"),fg="white",bg="#6A89A7")
        self.cpwd.place(x=300,y=330)
        self.cpwd_entry = ttk.Entry(self.frame,show='*',textvariable=self.var_cpwd,font=("new times roman",15,"bold"))
        self.cpwd_entry.place(x=300,y=365,width=250)

        # buttons
        img2 = Image.open("app_images/rgbutton.png")
        img2 = img2.resize((200,50), Resampling.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)
        register_btn = Button(self.frame,image=self.photo2,cursor="hand2",bg="#6A89A7",borderwidth=0,activebackground="#6A89A7",command=self.register_data)
        register_btn.place(x=200,y=520,width=200)

        loginbtn = Button(self.frame,cursor="hand2",text="LOGIN NOW",font=("new times roman",20,"bold"),fg="white",bg="#2ea9f0",relief=RIDGE,bd=3,activeforeground="white",activebackground="#2ea9f0",command=self.login_now)
        loginbtn.place(width=200,height=50,x=450,y=520)

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

    def register_data(self):
        if self.var_email.get() == '' or self.var_pwd.get() == '' or self.var_cpwd.get() == '':
            mb.showerror('Error', 'All fields are required!',parent=self.root)
            return

        email_input = self.var_email.get()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not match(pattern, email_input):
            mb.showerror("Invalid Email", "Please enter a valid email address.",parent=self.root)
            return

        if self.var_pwd.get() != self.var_cpwd.get():
            mb.showerror("Error", "Password and confirm password must be same.",parent=self.root)
            return
        
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="smartattend")
            my_cursor = conn.cursor()

            query_1 = "select * from register where email=%s"
            value_1 = (self.var_email.get(),)
            my_cursor.execute(query_1, value_1)
            row1 = my_cursor.fetchone()

            if row1 is not None:
                mb.showerror("Error", "User already exists, please try another email.",parent=self.root)
                return
            
            query_2 = "select * from admin where email=%s"
            value_2 = (self.var_email.get(),)
            my_cursor.execute(query_2, value_2)
            row2 = my_cursor.fetchone()

            if row2 is None:
                mb.showerror("Not Authorised", "You are not allowed to register!\nPlease contact SuperAdmin.",parent=self.root)
                return

            my_cursor.execute("insert into register values(%s, %s)", (
                self.var_email.get(),
                self.var_pwd.get()
                ))

            conn.commit()
            mb.showinfo("Success", "Registration successful!",parent=self.root)

            # clear fields
            self.var_email.set('')
            self.var_pwd.set('')
            self.var_cpwd.set('')
                        

        except Exception as e:
            mb.showerror("Database Error", f"Something went wrong: {str(e)}",parent=self.root)

        finally:
            if conn.is_connected():
                conn.close()
    def login_now(self):
        self.root.destroy()

if __name__ == '__main__':
    root = Tk()
    rg = Register(root)
    root.mainloop()