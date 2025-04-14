import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages")
import customtkinter as ctk
import sqlite3
from tkinter import messagebox

# Database setup
conn = sqlite3.connect("exam_regs.db")  # Using your database name
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS exam_registrations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT,
                    phone TEXT,
                    reg_number TEXT,
                    exam_name TEXT)''')
conn.commit()
conn.close()

# Function to save registration data
def save_registration(name, phone, reg_number, exam):
    conn = sqlite3.connect("exam_regs.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO exam_registrations (full_name, phone, reg_number, exam_name) VALUES (?, ?, ?, ?)",
                   (name, phone, reg_number, exam))
    conn.commit()
    conn.close()

# Function to open dashboard
def open_dashboard():
    login_window.destroy()
    dashboard = ctk.CTk()
    dashboard.title("Dashboard")
    dashboard.geometry("400x300")
    
    ctk.CTkLabel(dashboard, text="Welcome to Exam System", font=("Arial", 16)).pack(pady=20)
    
    ctk.CTkButton(dashboard, text="View Available Exam Details", command=open_exam_list).pack(pady=10)
    
    dashboard.mainloop()

# Function to open registration form
def register_exam(selected_exam=""):
    registration_window = ctk.CTk()
    registration_window.title("Register for Exam")
    registration_window.geometry("400x400")
    

    ctk.CTkLabel(registration_window, text="Exam Registration", font=("Arial", 16)).pack(pady=10)

    ctk.CTkLabel(registration_window, text="Full Name:").pack(pady=5)
    name_entry = ctk.CTkEntry(registration_window)
    name_entry.pack(pady=5)

    ctk.CTkLabel(registration_window, text="Phone Number:").pack(pady=5)
    phone_entry = ctk.CTkEntry(registration_window)
    phone_entry.pack(pady=5)

    ctk.CTkLabel(registration_window, text="Registration Number:").pack(pady=5)
    reg_number_entry = ctk.CTkEntry(registration_window)
    reg_number_entry.pack(pady=5)

    ctk.CTkLabel(registration_window, text="Exam Name:").pack(pady=5)
    exam_entry = ctk.CTkEntry(registration_window)
    exam_entry.pack(pady=5)
    exam_entry.insert(0, selected_exam)  # Auto-fill selected exam

    def submit_registration():
        name = name_entry.get()
        phone = phone_entry.get()
        reg_number = reg_number_entry.get()
        exam = exam_entry.get()

        if name and phone and reg_number and exam:
            save_registration(name, phone, reg_number, exam)  # Store data in the database
            messagebox.showinfo("Success", f"Registered for {exam} Successfully!")
            registration_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    ctk.CTkButton(registration_window, text="Submit", command=submit_registration).pack(pady=10)

    registration_window.mainloop()

# Function to open exam categories
def open_exam_list():
    exam_window = ctk.CTk()
    exam_window.title("Available Exams")
    exam_window.geometry("500x400")
    
    ctk.CTkLabel(exam_window, text="Available Exam Categories", font=("Arial", 14)).pack(pady=10)
    
    ctk.CTkButton(exam_window, text="1. Engineering Entrance Exams", command=open_engineering_exams).pack(pady=5)
    ctk.CTkButton(exam_window, text="2. Medical Entrance Exams", command=open_medical_exams).pack(pady=5)
    ctk.CTkButton(exam_window, text="3. Commerce & Management Exams", command=open_commerce_exams).pack(pady=5)
    ctk.CTkButton(exam_window, text="4. Law Entrance Exams", command=open_law_exams).pack(pady=5)
    
    exam_window.mainloop()

# Engineering Exams Window
def open_engineering_exams():
    engineering_window = ctk.CTk()
    engineering_window.title("Engineering Exams")
    engineering_window.geometry("500x300")
    
    ctk.CTkLabel(engineering_window, text="Engineering Entrance Exams", font=("Arial", 14)).pack(pady=10)
    exams = ["JEE Main", "JEE Advanced", "BITSAT", "VITEEE", "COMEDK UGET", "KCET"]
    
    for exam in exams:
        ctk.CTkButton(engineering_window, text=exam, command=lambda e=exam: register_exam(e)).pack(pady=2)
    
    engineering_window.mainloop()

# Medical Exams Window
def open_medical_exams():
    medical_window = ctk.CTk()
    medical_window.title("Medical Exams")
    medical_window.geometry("500x300")

    ctk.CTkLabel(medical_window, text="Medical Entrance Exams", font=("Arial", 14)).pack(pady=10)
    exams = ["NEET", "AIIMS Entrance Exam", "JIPMER Entrance Exam"]
    
    for exam in exams:
        ctk.CTkButton(medical_window, text=exam, command=lambda e=exam: register_exam(e)).pack(pady=2)

    medical_window.mainloop()

# Commerce & Management Exams Window
def open_commerce_exams():
    commerce_window = ctk.CTk()
    commerce_window.title("Commerce & Management Exams")
    commerce_window.geometry("500x300")

    ctk.CTkLabel(commerce_window, text="Commerce & Management Entrance Exams", font=("Arial", 14)).pack(pady=10)
    exams = ["CUET", "IPMAT", "NPAT", "SET"]

    for exam in exams:
        ctk.CTkButton(commerce_window, text=exam, command=lambda e=exam: register_exam(e)).pack(pady=2)

    commerce_window.mainloop()

# Law Exams Window
def open_law_exams():
    law_window = ctk.CTk()
    law_window.title("Law Exams")
    law_window.geometry("500x300")

    ctk.CTkLabel(law_window, text="Law Entrance Exams", font=("Arial", 14)).pack(pady=10)
    exams = ["CLAT", "AILET", "LSAT", "DU LLB Entrance Exam"]

    for exam in exams:
        ctk.CTkButton(law_window, text=exam, command=lambda e=exam: register_exam(e)).pack(pady=2)

    law_window.mainloop()

# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "asdfg" and password == "12345":
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main login window
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

login_window = ctk.CTk()
login_window.title("Login Page")
login_window.geometry("300x250")

frame = ctk.CTkFrame(login_window)
frame.pack(pady=20, padx=20, fill="both", expand=True)

ctk.CTkLabel(frame, text="Username:").pack(pady=5)
username_entry = ctk.CTkEntry(frame)
username_entry.pack(pady=5)

ctk.CTkLabel(frame, text="Password:").pack(pady=5)
password_entry = ctk.CTkEntry(frame, show="*")
password_entry.pack(pady=5)

ctk.CTkButton(frame, text="Login", command=login).pack(pady=10)
ctk.CTkButton(frame, text="Register", command=lambda: register_exam()).pack(pady=10)

login_window.mainloop()
