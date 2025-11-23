from tkinter import *
from PIL import Image,ImageTk
from PIL.Image import Resampling
from tkinter import messagebox as mb
import os
import numpy as np
import cv2


class Train_data:
    def __init__(self,root):
        self.root = root


        # logo
        self.icon_image = PhotoImage(file="app_images/logo.png")
        self.root.iconphoto(False, self.icon_image)

        self.root.title("Train Data")
        self.root.geometry("500x350+500+250") #340x450+610+200
        self.root.configure(background="#384959")
        self.root.resizable(False,False)

        # train data
        logo_lbl = Label(self.root,text="Train Data",font=("new times roman",20,"bold"),fg="#384959",bg="#BDDDFC")
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

        img3 = Image.open("app_images/train_data_img.png")
        img3 = img3.resize((500,250), Resampling.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(self.root,image=self.photo3,bg="#BDDDFC")
        lbl_img3.place(width=500,height=250,x=0,y=50)

        # button

        train_data_btn = Button(self.root,text="Train Data",font=("new times roman",20,"bold"),fg="white",bg="red",
                                cursor="hand2",activeforeground="white",activebackground="green",command=self.train_classifier)
        train_data_btn.place(width=500,height=50,x=0,y=300)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') # Gray Scale Image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)
        ids = np.array(ids)

        # $$$$$$$$$$$$$ Train the classifier and save $$$$$$$$$$$$$ #
        clf = cv2.face.LBPHFaceRecognizer_create()
        # Train the classifier
        clf.train(faces, ids)

        # Save the trained model
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        mb.showinfo("Result", "Training completed successfully!",parent=self.root)



if __name__ == '__main__':
    root = Tk()
    t = Train_data(root)
    root.mainloop()