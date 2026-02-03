import tkinter as tk
from tkinter import ttk, messagebox

class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller


        header = tk.Frame(self, bg="#06A77d")
        header.pack(fill="x", padx=0, pady=0)
        tk.Label(header, text="Create Account", font=("Helvetica", 24, "bold"), bg="#06A77d", fg="white").pack(pady=20)


        form_frame = ttk.Frame(self)
        form_frame.pack(fill="both", expand=True, padx=40, pady=20)

        ttk.Label(form_frame, text="Full Name:", font=("Helvetica", 11)).pack(anchor="w", pady=(0, 5))
        self.fullname_entry = ttk.Entry(form_frame, font=("Helvetica", 10), width=35)
        self.fullname_entry.pack(anchor="w",pady=(0, 12))

        ttk.Label(form_frame, text="Email:", font=("Helvetica", 11)).pack(anchor="w",pady=(0, 5))
        self.email_entry = ttk.Entry(form_frame, font=("Helevtica", 10), width=35)
        self.email_entry.pack(anchor="w", pady=(0, 12)) 

        ttk.Label(form_frame, text="User Name:", font=("Helvetica", 11)).pack(anchor="w", pady=(0, 5))
        self.username_entry = ttk.Entry(form_frame, font=("Helevtica", 10), width=35)
        self.username_entry.pack(anchor="w", pady=(0, 12)) 

        ttk.Label(form_frame, text="Password:", font=("Helvetica", 11)).pack(anchor="w", pady=(0, 5))
        self.password_entry = ttk.Entry(form_frame, show=".", font=("Helevtica", 10), width=35)
        self.password_entry.pack(anchor="w", pady=(0, 12))

        ttk.Label(form_frame, text="Confirm Password:", font=("Helvetica", 11)).pack(anchor="w", pady=(0, 5))
        self.conf_pass_entry = ttk.Entry(form_frame, show=".", font=("Helevtica", 10), width=35)
        self.conf_pass_entry.pack(anchor="w", pady=(0, 12)) 







if __name__ == "__main__":
    root = tk.Tk()
    root.title("Blog App - Signup Only")
    root.geometry("450x650")

    signup_page = SignupPage(parent=root, controller=root)
    signup_page.pack(fill="both", expand=True)
    
    root.mainloop()  