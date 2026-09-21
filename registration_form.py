import tkinter as tk
from tkinter import messagebox

def submit_form():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()

    if first_name and last_name and email and password:
        messagebox.showinfo("Success", "Registration Successful!")
    else:
        messagebox.showerror("Error", "All fields are required!")

root = tk.Tk()
root.title("Registration Form")

tk.Label(root, text="First Name").grid(row=0, column=0, padx=10, pady=10)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Last Name").grid(row=1, column=0, padx=10, pady=10)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Password").grid(row=3, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show='*')
entry_password.grid(row=3, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
