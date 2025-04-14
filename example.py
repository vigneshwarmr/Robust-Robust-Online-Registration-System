import sqlite3
import tkinter as tk
from tkinter import messagebox

# Create database and table if not exists
conn = sqlite3.connect("personnel.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS personnel (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    dob TEXT,
                    gender TEXT,
                    designation TEXT)''')
conn.commit()
conn.close()

# Function to save data into database
def save_data():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    dob = entry_dob.get()
    gender = gender_var.get()
    designation = entry_designation.get()

    if first_name and last_name and dob and gender and designation:
        conn = sqlite3.connect("personnel.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO personnel (first_name, last_name, dob, gender, designation) VALUES (?, ?, ?, ?, ?)",
                       (first_name, last_name, dob, gender, designation))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data saved successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "All fields are required!")

# Function to clear input fields
def clear_entries():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_designation.delete(0, tk.END)
    gender_var.set("Select Gender")

# GUI Setup
root = tk.Tk()
root.title("Personnel Details Form")
root.geometry("400x350")

tk.Label(root, text="First Name:").pack(pady=5)
entry_first_name = tk.Entry(root)
entry_first_name.pack(pady=5)

tk.Label(root, text="Last Name:").pack(pady=5)
entry_last_name = tk.Entry(root)
entry_last_name.pack(pady=5)

tk.Label(root, text="Date of Birth (YYYY-MM-DD):").pack(pady=5)
entry_dob = tk.Entry(root)
entry_dob.pack(pady=5)

tk.Label(root, text="Gender:").pack(pady=5)
gender_var = tk.StringVar(root)
gender_var.set("Select Gender")
gender_dropdown = tk.OptionMenu(root, gender_var, "Male", "Female", "Other")
gender_dropdown.pack(pady=5)

tk.Label(root, text="Designation:").pack(pady=5)
entry_designation = tk.Entry(root)
entry_designation.pack(pady=5)

btn_save = tk.Button(root, text="Done", command=save_data, bg="green", fg="white")
btn_save.pack(pady=20)

root.mainloop()