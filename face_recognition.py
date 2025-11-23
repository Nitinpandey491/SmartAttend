from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL.Image import Resampling
from tkinter import messagebox as mb
import mysql.connector
import cv2
import customtkinter as ctk



class Face_recognition:
    def __init__(self, root):
        self.root = root

        # variables
        self.var_sub = StringVar()
        self.var_st = StringVar()
        self.var_fac = StringVar()

        # logo
        self.icon_image = PhotoImage(file="app_images/logo.png")
        self.root.iconphoto(False, self.icon_image)

        self.root.title("Face Recognition")
        self.root.geometry("500x460+500+200")  # 340x450+610+200 , 500x350+500+150 , 500x350+500+250
        self.root.configure(background="#384959")
        self.root.resizable(False, False)

        # Face Recognition
        logo_lbl = Label(self.root, text="Face Recognition", font=("new times roman", 20, "bold"), fg="#384959", bg="#BDDDFC")
        logo_lbl.place(x=0, y=0, width=500, height=50)

        # images
        img1 = Image.open("app_images/mlogo.png")
        img1 = img1.resize((50, 50), Resampling.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(self.root, image=self.photo1, bg="#BDDDFC")
        lbl_img1.place(width=50, height=50, x=15, y=0)

        img2 = Image.open("app_images/mlogo.png")
        img2 = img2.resize((50, 50), Resampling.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root, image=self.photo2, bg="#BDDDFC")
        lbl_img2.place(width=50, height=50, x=435, y=0)

        # Note Label
        note_lbl = Label(self.root,text="Press 'Enter' to close the camera!",font=("new times roman",12,"bold"),fg="white",bg="red")
        note_lbl.place(width=500,height=30,x=0,y=50)

        # attendance information frame ............................................................................................. #

        ai_frame = ctk.CTkScrollableFrame(self.root,width=435,height=50,corner_radius=20,fg_color="#6bb5e0",
                                          label_text="Attendance Information",label_font=("new times roman",20,"bold"),
                                          label_text_color="white",label_fg_color="blue",scrollbar_button_color="blue",
                                          scrollbar_button_hover_color="light blue")
        ai_frame.place(x=15,y=90)

        # attendance info img
        si_img = Image.open("app_images/attendance_icon.png")
        si_img = si_img.resize((20,20), Resampling.LANCZOS)
        self.si_img1 = ImageTk.PhotoImage(si_img)
        lbl_si_img = Label(self.root,image=self.si_img1,bg="blue")
        lbl_si_img.place(width=20,height=20,x=115,y=115)

        # form
        # ai_frame1
        ai_frame1 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame1.pack(padx=20,pady=10)   
        ai_frame1.pack_propagate(False)
        # field_1
        sub_lbl = Label(ai_frame1,text="Subject:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        sub_lbl.pack(side="left",anchor="n",padx=25)

        sub_entry = ttk.Entry(ai_frame1,textvariable=self.var_sub,font=("new times roman",12,"bold"),width=30)
        sub_entry.pack(side="left",anchor="n") 

        # ai_frame2
        ai_frame2 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame2.pack(padx=15,pady=10)   
        ai_frame2.pack_propagate(False)
        # field_2
        st_lbl = Label(ai_frame2,text="Session Type:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        st_lbl.pack(side="left",anchor="n",padx=5)

        st_entry = ttk.Combobox(ai_frame2,textvariable=self.var_st,font=("new times roman",12,"bold"),width=28,state="readonly")
        st_entry["values"] = ("Select Session Type","Theory","Practical")
        st_entry.pack(side="left",anchor="n")
        st_entry.current(0)

        # ai_frame3
        ai_frame3 = Frame(ai_frame, width=650, height=30,bg="#6bb5e0")
        ai_frame3.pack(padx=20,pady=10)   
        ai_frame3.pack_propagate(False)
        # field_3
        fac_lbl = Label(ai_frame3,text="Faculty:",fg="white",bg="#6bb5e0",font=("new times roman",12,"bold"))
        fac_lbl.pack(side="left",anchor="n",padx=27)

        fac_entry = ttk.Entry(ai_frame3,textvariable=self.var_fac,font=("new times roman",12,"bold"),width=30)
        fac_entry.pack(side="left",anchor="n")




        # button
        face_recog_btn = Button(self.root, text="Take Attendance", font=("new times roman", 20, "bold"), fg="white", bg="blue",
                                cursor="hand2", activeforeground="white", activebackground="green", command=self.face_recog)
        face_recog_btn.place(width=500, height=50, x=0, y=410)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Taking Attendance $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
    def mark_attendance(self, i, r, n, d):
        import datetime
        import os
        
        subject = self.var_sub.get()
        session_type = self.var_st.get()
        faculty = "Prof." + self.var_fac.get()
        # Check if attendance should be marked
        if i == "Unknown":
            return
        
        now = datetime.datetime.now()
        current_date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")
        
        # Check if file exists and read existing IDs
        existing_ids = set()
        file_exists = os.path.exists("attendance_report/attendance.csv")
        
        if file_exists:
            with open("attendance_report/attendance.csv", "r") as f:
                lines = f.readlines()
                for line in lines[1:]:  # Skip header
                    if line.strip():
                        entry = line.split(",")
                        if entry:
                            existing_ids.add(entry[0])
        
        # Check if ID already exists
        if i in existing_ids:
            return
        
        # Ensure file ends with newline before appending
        if file_exists and os.path.getsize("attendance_report/attendance.csv") > 0:
            with open("attendance_report/attendance.csv", "rb+") as f:
                f.seek(-1, 2)  # Go to last byte
                if f.read(1) != b'\n':
                    f.write(b'\n')
                      
        # Append to file
        with open("attendance_report/attendance.csv", "a") as f:
            if not file_exists or os.path.getsize("attendance_report/attendance.csv") == 0:
                f.write("Student ID,Roll No,Name,Department,Time,Date,Subject,Session Type,Faculty,Status\n")
            f.write(f"{i},{r},{n},{d},{time},{current_date},{subject},{session_type},{faculty},Present\n")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ face recognition $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
    def face_recog(self):
        if self.var_sub.get() == '' or self.var_st.get() == 'Select Session Type' or self.var_fac.get() == '':
            mb.showerror('Error', 'All fields are required!', parent=self.root)
            return

        try:
            # ========== Settings (you can change this) ==========
            CONF_THRESHOLD = 80              # confidence threshold
            SHOW_CONFIDENCE = True           # show confidence % on screen
            ALLOW_REPEAT_ATTENDANCE = False  # False = 1 time only

            # Track already marked students to avoid duplicate attendance
            marked = set()

            # ========== DB Connection (open only once) ==========
            conn = mysql.connector.connect(
                host="localhost", user="root", password="admin", database="smartattend"
            )
            cursor = conn.cursor()

            # ========== Load Model & Detector ==========
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            def draw_boundary(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                gray = cv2.equalizeHist(gray)
                faces = faceCascade.detectMultiScale(gray, 1.1, 8)

                for (x, y, w, h) in faces:
                    face_img = gray[y:y + h, x:x + w]
                    id, distance = clf.predict(face_img)

                    # Recommended LBPH confidence formula
                    confidence = int(100 * (1 - distance / 300))

                    if SHOW_CONFIDENCE:
                        cv2.putText(img, f"{confidence}%", (x, y + h + 20),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                    if confidence >= CONF_THRESHOLD:

                        cursor.execute(
                            "SELECT std_id, rollno, std_name, dept FROM student WHERE std_id=%s", (id,)
                        )
                        result = cursor.fetchone()

                        if result:
                            std_id, roll, name, dept = map(str, result)

                            # Display data on screen
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                            cv2.putText(img, f"ID:{std_id}", (x, y - 80),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Name:{name}", (x, y - 55),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Roll No:{roll}", (x, y - 30),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Department:{dept}", (x, y - 3),
                                        cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                            # Check attendance duplication
                            if not ALLOW_REPEAT_ATTENDANCE:
                                if std_id not in marked:
                                    self.mark_attendance(std_id, roll, name, dept)
                                    marked.add(std_id)
                            else:
                                self.mark_attendance(std_id, roll, name, dept)

                        else:
                        # no DB data found
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                            cv2.putText(img, "Unknown Face", (x, y - 10),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    else:
                        # Low confidence = Unknown
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 10),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

            # ========== CAMERA LOOP ==========
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                draw_boundary(img)
                cv2.imshow("Face Recognition", img)
                if cv2.waitKey(1) == 13:   # Enter key to exit
                    break

            cap.release()
            cv2.destroyAllWindows()
            conn.close()

        except Exception as e:
            mb.showerror("Error", f"Something went wrong:\n{e}", parent=self.root)


if __name__ == '__main__':
    root = Tk()
    f = Face_recognition(root)
    root.mainloop()