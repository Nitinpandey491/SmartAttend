from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from PIL.Image import Resampling
from tkinter import messagebox as mb
import mysql.connector
import re
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

class Forget_password:
    def __init__(self,root):
        self.root = root
        
        # variables
        self.var_email = StringVar()
        self.var_otp = StringVar()

        self.generated_otp = None
        self.otp_creation_time = None

        # logo
        self.icon_image = PhotoImage(file="app_images/logo.png")
        self.root.iconphoto(False, self.icon_image)

        self.root.title("Forget Password")
        self.root.geometry("500x450+500+200")
        self.root.configure(background="#384959")
        self.root.resizable(False,False)

        # forget password
        logo_lbl = Label(self.root,text="Forget Password",font=("new times roman",20,"bold"),fg="#384959",bg="#BDDDFC")
        logo_lbl.place(x=0,y=0,width=500,height=50)

        # images
        img1 = Image.open("app_images/mlogo.png")
        img1 = img1.resize((50,50), Resampling.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(self.root,image=self.photo1,bg="#BDDDFC")
        lbl_img1.place(width=50,height=50,x=15,y=0)

        img2 = Image.open("app_images/mlogo.png")
        img2 = img2.resize((50,50), Resampling.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root,image=self.photo2,bg="#BDDDFC")
        lbl_img2.place(width=50,height=50,x=435,y=0)

        # form

        # field 1
        self.email = Label(self.root,text="Email Address:",font=("new times roman",15,"bold"),fg="white",bg="#384959")
        self.email.place(x=180,y=120)
        self.email_entry = ttk.Entry(self.root,textvariable=self.var_email,font=("new times roman",15,"bold"))
        self.email_entry.place(x=110,y=150,width=300)

        #  send otp button
        send_btn = Button(self.root,cursor="hand2",text="Send OTP",
                          font=("new times roman",20,"bold"),fg="white",bg="blue",relief=RIDGE,bd=3,
                          activeforeground="white",activebackground="green",command=self.send_otp)
        send_btn.place(width=225,height=50,x=145,y=190)

        # field 2
        self.enter_otp = Label(self.root,text="Enter OTP:",font=("new times roman",15,"bold"),fg="white",bg="#384959")
        self.enter_otp.place(x=195,y=270)
        self.enter_otp_entry = ttk.Entry(self.root,font=("new times roman",15,"bold"),textvariable=self.var_otp)
        self.enter_otp_entry.place(x=110,y=300,width=300)

        #  verify otp button
        verify_btn = Button(self.root,cursor="hand2",text="Verify OTP",
                          font=("new times roman",20,"bold"),fg="white",bg="red",relief=RIDGE,bd=3,
                          activeforeground="white",activebackground="green",command=self.verify_otp)
        verify_btn.place(width=225,height=50,x=145,y=340)


    def send_otp(self):
        # Get email from input
        email = self.var_email.get().strip()
    
        if email == '':
            mb.showerror("Empty Field", "Please enter email address",parent=self.root)
            return
        
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, email):
            mb.showerror("Invalid Email", "Please enter a valid email address.")
            return
        
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost",user="root",password="admin",database="smartattend")
            db_cursor = conn.cursor()
            
            query = "select * from register where email=%s"
            value = (email,)
            db_cursor.execute(query,value)
            
            row = db_cursor.fetchone()
            if row is None:
                mb.showerror("Not Found",f"Email = {email} is not registered!",parent=self.root)
                return

        except Exception as e:
            mb.showerror('Database Error',f'Something went wrong: {str(e)}')
        finally:
            if conn and conn.is_connected():
                conn.close()
        
        # Generate OTP
        self.generated_otp = str(random.randint(100000, 999999))
        self.otp_creation_time = time.time()
        
        # Try to send OTP via email
        try:
            # Email configuration - replace with your actual credentials
            sender_email = "supera4597@gmail.com"
            sender_password = "uowg fkkl zjif chir"
            
            # Create email message
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = email
            message["Subject"] = "Password Reset OTP"
            
            body = f"Your OTP for password reset is: {self.generated_otp}\n"
            body += "This OTP will expire in 2 minutes."
            
            message.attach(MIMEText(body, "plain"))
            
            # Send email
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())
            server.quit()
            
            mb.showinfo("Success", "OTP sent to your email! It will expire in 2 minutes.",parent=self.root)
            
        except Exception as e:
            mb.showerror("Error", f"Failed to send OTP: {str(e)}",parent=self.root)
    
    def verify_otp(self):
        # Get OTP from input
        entered_otp = self.var_otp.get().strip()
        
        # Check if OTP was entered
        if not entered_otp:
            mb.showerror("Empty Field", "Please enter the OTP",parent=self.root)
            return
        
        # Check if OTP was generated
        if self.generated_otp is None:
            mb.showerror("Not Found", "Please request an OTP first",parent=self.root)
            return
        
        # Check if OTP is expired (2 minutes = 120 seconds)
        current_time = time.time()
        time_difference = current_time - self.otp_creation_time
        
        if time_difference > 120:
            mb.showerror("OTP Expired", "OTP has expired. Please request a new one.",parent=self.root)
            return
        
        # Check if OTP matches
        if entered_otp == self.generated_otp:
            mb.showinfo("Success", "OTP verified successfully!",parent=self.root)
            # Open reset password window and pass the email
            self.var_otp.set('')
            self.open_reset_window()
        else:
            mb.showerror("Incorrect OTP", "Invalid OTP. Please try again.",parent=self.root)
    
    def open_reset_window(self):
        reset_window = Toplevel(self.root)
        reset_window.title("Reset Password")
        reset_window.geometry("500x450+500+200")
        reset_window.configure(background="#384959")
        reset_window.resizable(False, False)
    
        ResetPassword(reset_window, self.var_email.get())

class ResetPassword:
    def __init__(self, root2, email):
        self.root2 = root2
        self.email = email 

        # variables
        self.var_new_password = StringVar()
        self.var_confirm_password = StringVar()
        
        self.reset()
    
    def reset(self):
        title_lbl = Label(self.root2, text="Reset Password", font=("new times roman", 20, "bold"), 
                         fg="#384959", bg="#BDDDFC")
        title_lbl.place(x=0, y=0, width=500, height=50)

        # images
        img3 = Image.open("app_images/mlogo.png")
        img3 = img3.resize((50,50), Resampling.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(self.root2,image=self.photo3,bg="#BDDDFC")
        lbl_img3.place(width=50,height=50,x=15,y=0)

        img4 = Image.open("app_images/mlogo.png")
        img4 = img4.resize((50,50), Resampling.LANCZOS)
        self.photo4 = ImageTk.PhotoImage(img4)
        lbl_img4 = Label(self.root2,image=self.photo4,bg="#BDDDFC")
        lbl_img4.place(width=50,height=50,x=435,y=0)
        
        # Email display Label
        email_lbl = Label(self.root2, text=f"Email: {self.email}", font=("new times roman", 12), 
                         fg="white", bg="#384959")
        email_lbl.place(x=50, y=80)
        
        # field_1
        new_pass_lbl = Label(self.root2, text="New Password:", font=("new times roman", 15, "bold"), 
                            fg="white", bg="#384959")
        new_pass_lbl.place(x=50, y=130)
        
        new_pass_entry = ttk.Entry(self.root2, textvariable=self.var_new_password, 
                                  font=("new times roman", 15, "bold"), show="*")
        new_pass_entry.place(x=50, y=160, width=400)
        
        # field_2
        confirm_pass_lbl = Label(self.root2, text="Confirm Password:", font=("new times roman", 15, "bold"), 
                                fg="white", bg="#384959")
        confirm_pass_lbl.place(x=50, y=210)
        
        confirm_pass_entry = ttk.Entry(self.root2, textvariable=self.var_confirm_password, 
                                      font=("new times roman", 15, "bold"), show="*")
        confirm_pass_entry.place(x=50, y=240, width=400)
        
        # Reset button
        reset_btn = Button(self.root2, cursor="hand2", text="Reset Password",
                          font=("new times roman", 20, "bold"), fg="white", bg="green", relief=RIDGE, bd=3,
                          activeforeground="white", activebackground="darkgreen", command=self.reset_password)
        reset_btn.place(width=225, height=50, x=145, y=300)
    
    def reset_password(self):

        new_password = self.var_new_password.get().strip()
        confirm_password = self.var_confirm_password.get().strip()

        if new_password == '' or confirm_password == '':
            mb.showerror("Empty Fields", "Please fill in all fields", parent=self.root2)
            return
        
        if new_password != confirm_password:
            mb.showerror("Mismatch", "New Password and Confirm Password is not matching\nPlease Ty Again!", parent=self.root2)
            return
        
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost", user="root", 
                                          password="admin", database="smartattend")
            db_cursor = conn.cursor()
            
            query = "update register set password=%s where email=%s"
            values = (new_password, self.email)
            db_cursor.execute(query, values)
            
            conn.commit()
            if db_cursor.rowcount > 0:
                mb.showinfo("Success", "Password updated successfully!", parent=self.root2)
                self.root2.destroy()
            else:
                mb.showerror("Error", "Failed to update password", parent=self.root2)
                
        except Exception as e:
            mb.showerror('Database Error', f'Something went wrong: {str(e)}', parent=self.root2)
        finally:
            if conn and conn.is_connected():
                conn.close()


if __name__ == '__main__':
    root = Tk()
    f = Forget_password(root)
    root.mainloop()