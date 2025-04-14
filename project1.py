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

# Function to open registration form
def register_exam(selected_exam=""):
    registration_window = ctk.CTk()
    registration_window.title("Register for Exam")
    registration_window.geometry("400x450")
    
    # Frame with border
    frame = ctk.CTkFrame(registration_window, border_width=2, border_color="purple")
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    ctk.CTkLabel(frame, text="Exam Registration", font=("Arial", 18, "bold"), text_color="purple").pack(pady=10)

    ctk.CTkLabel(frame, text="Full Name:", text_color="white").pack(pady=5)
    name_entry = ctk.CTkEntry(frame, border_width=2, border_color="purple")
    name_entry.pack(pady=5)

    ctk.CTkLabel(frame, text="Phone Number:", text_color="white").pack(pady=5)
    phone_entry = ctk.CTkEntry(frame, border_width=2, border_color="purple")
    phone_entry.pack(pady=5)

    ctk.CTkLabel(frame, text="Registration Number:", text_color="white").pack(pady=5)
    reg_number_entry = ctk.CTkEntry(frame, border_width=2, border_color="purple")
    reg_number_entry.pack(pady=5)

    ctk.CTkLabel(frame, text="Exam Name:", text_color="white").pack(pady=5)
    exam_entry = ctk.CTkEntry(frame, border_width=2, border_color="purple")
    exam_entry.pack(pady=5)
    exam_entry.insert(0, selected_exam)

    def submit_registration():
        name = name_entry.get()
        phone = phone_entry.get()
        reg_number = reg_number_entry.get()
        exam = exam_entry.get()

        if name and phone and reg_number and exam:
            save_registration(name, phone, reg_number, exam)
            messagebox.showinfo("Success", f"Registered for {exam} Successfully!")
            registration_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    ctk.CTkButton(frame, text="Submit", fg_color="purple", hover_color="#6A0DAD", command=submit_registration).pack(pady=10)
    registration_window.mainloop()

# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "asdfg" and password == "12345":
        messagebox.showinfo("Login Success", "Welcome to the Exam System")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main login window
ctk.set_appearance_mode("Dark")

login_window = ctk.CTk()
login_window.title("Login Page")
login_window.geometry("350x300")

frame = ctk.CTkFrame(login_window, border_width=2, border_color="purple")
frame.pack(pady=20, padx=20, fill="both", expand=True)

ctk.CTkLabel(frame, text="Username:", text_color="white").pack(pady=5)
username_entry = ctk.CTkEntry(frame, border_width=2, border_color="purple")
username_entry.pack(pady=5)

ctk.CTkLabel(frame, text="Password:", text_color="white").pack(pady=5)
password_entry = ctk.CTkEntry(frame, show="*", border_width=2, border_color="purple")
password_entry.pack(pady=5)

ctk.CTkButton(frame, text="Login", fg_color="purple", hover_color="#6A0DAD", command=login).pack(pady=10)
ctk.CTkButton(frame, text="Register", fg_color="purple", hover_color="#6A0DAD", command=lambda: register_exam()).pack(pady=10)

login_window.mainloop()
