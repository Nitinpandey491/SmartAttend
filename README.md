# 🌟 **Overview**

**SmartAttend** is an AI-based attendance automation system that uses **face recognition** to mark attendance instantly and securely.
It eliminates manual entries and improves speed, accuracy, and reliability for institutions.

# ⚡ **Key Features**

### 🎯 **Automated Attendance**

* Recognizes faces in real-time
* Marks present with timestamp
* Saves record to MySQL + CSV

### 🧠 **AI Face Recognition**

* Uses **OpenCV LBPH** recognizer
* Includes **Deep-Learning SSD** face detector for higher accuracy

### 🧑‍🎓 **Student & Admin Management**

* Add/Update/Delete student records
* Capture 100 face samples per student
* Multi-level access: Super Admin → Admin → Students

### 🗂️ **Attendance Reports**

* Search by date, student, or session
* Export to CSV
* Clean attendance viewer GUI

### 🖥️ **Modern GUI**

* Tkinter + CustomTkinter
* Clean, responsive UI
* Minimal, user-friendly navigation

---

# 🏗️ **System Architecture**

```
       +---------------------+
       |   Tkinter GUI       |
       +---------+-----------+
                 |
                 v
       +---------------------+
       |  Face Detection     | <-- OpenCV DNN (SSD)
       +---------+-----------+
                 |
                 v
       +---------------------+
       | Face Recognition    | <-- LBPH Model (classifier.xml)
       +---------+-----------+
                 |
                 v
       +---------------------+
       |   Attendance DB     | <-- MySQL + CSV logs
       +---------------------+
```

---

# 🛠️ **Tech Stack**

| Category    | Tools                                     |
| ----------- | ----------------------------------------- |
| Programming | Python                                    |
| CV / AI     | OpenCV, LBPH, DNN SSD                     |
| GUI         | Tkinter, CustomTkinter, PIL               |
| Database    | MySQL Community Server                    |
| Libraries   | NumPy, OS, CSV, DateTime, MySQL Connector |
| IDE         | VS Code                                   |

---

# 📥 **Installation**

### **1️⃣ Clone the Repo**

```bash
git clone https://github.com/yourusername/SmartAttend.git
cd SmartAttend
```

### **2️⃣ Install Dependencies**

```bash
pip install opencv-python mysql-connector-python numpy pillow customtkinter
```

### **3️⃣ Create MySQL Database**

```
Database  : smartattend
Tables    : superadmin, admin, register, student, attendance
```


### **4️⃣ Run the App**

```bash
python SmartAttend.py
```

---

# 🧩 **How It Works (Flow)**

### 1. **Super Admin Login**

* Registers permitted admin emails

### 2. **Admin Login**

* Manages students
* Captures samples
* Trains model
* Takes attendance

### 3. **Training Phase**

* Reads face samples from `/data/`
* Trains LBPH
* Saves `classifier.xml`

### 4. **Attendance Phase**

* Recognizes faces through webcam
* Marks present
* Saves logs in MySQL + CSV

---

# 👨‍💻 Developer

Nitin Vinay Pandey


# ❤️ Support

If you like this project:

⭐ Star the repository

