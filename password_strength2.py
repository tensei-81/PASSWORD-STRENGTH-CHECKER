import tkinter as tk
from tkinter import ttk, messagebox
import re
import secrets
import string
import pyperclip  

def generate_password():
    """Generate a cryptographically secure password with mixed characters."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(chars) for _ in range(16))
    entry.delete(0, tk.END)
    entry.insert(0, password)
    check_strength_live() 
    pyperclip.copy(password)  
    messagebox.showinfo("Password Generated", "A strong password was generated and copied to clipboard!")

def suggest_improvement():
    """Analyze current password and suggest improvements."""
    password = entry.get()
    if not password:
        messagebox.showwarning("Empty Field", "Please enter a password first.")
        return

    suggestions = []
    
    if len(password) < 12:
        suggestions.append("➤ Increase length to at least 12 characters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("➤ Add uppercase letters (A-Z).")
    if not re.search(r"[a-z]", password):
        suggestions.append("➤ Add lowercase letters (a-z).")
    if not re.search(r"\d", password):
        suggestions.append("➤ Include numbers (0-9).")
    if not re.search(r"[!@#$%^&*]", password):
        suggestions.append("➤ Add special characters (!@#$%^&*).")

    if suggestions:
        feedback_text.delete("1.0", tk.END)
        feedback_text.insert(tk.END, "🔍 Suggestions to strengthen your password:\n\n" + "\n".join(suggestions))
    else:
        feedback_text.delete("1.0", tk.END)
        feedback_text.insert(tk.END, "✅ Your password is already strong!")


def check_strength_live(event=None):
    password = entry.get()
    strength_points = 0
    feedback = []

   
    if len(password) >= 16:
        strength_points += 2
    elif len(password) >= 12:
        strength_points += 1.5
    elif len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("➤ Use at least 8 characters (12+ recommended).")


    checks = [
        (r"[A-Z]", "➤ Add uppercase letters (A-Z)."),
        (r"[a-z]", "➤ Add lowercase letters (a-z)."),
        (r"\d", "➤ Include numbers (0-9)."),
        (r"[!@#$%^&*]", "➤ Add special characters (!@#$%^&*).")
    ]
    
    for pattern, message in checks:
        if re.search(pattern, password):
            strength_points += 1
        else:
            feedback.append(message)

   
    progress['value'] = (strength_points / 5) * 100

    
    if strength_points >= 5:
        strength_label.config(text="Strength: Strong 🔒", fg="#2ecc71")  # Green
        progress.config(style="Strong.Horizontal.TProgressbar")
    elif 3 <= strength_points < 5:
        strength_label.config(text="Strength: Moderate ⚠️", fg="#f39c12")  # Orange
        progress.config(style="Moderate.Horizontal.TProgressbar")
    else:
        strength_label.config(text="Strength: Weak ❌", fg="#e74c3c")  # Red
        progress.config(style="Weak.Horizontal.TProgressbar")

    
    feedback_text.delete("1.0", tk.END)
    if feedback:
        feedback_text.insert(tk.END, "🔍 Suggestions:\n\n" + "\n".join(feedback))
    else:
        feedback_text.insert(tk.END, "✅ Perfect! This password is strong and secure.")

def clear_fields():
    entry.delete(0, 'end')
    feedback_text.delete("1.0", tk.END)
    strength_label.config(text="Strength: ", fg="black")
    progress['value'] = 0


root = tk.Tk()
root.title("Ultimate Password Strength Checker")
root.geometry("500x400")
root.resizable(False, False)

style = ttk.Style()
style.theme_use('clam')
style.configure("Weak.Horizontal.TProgressbar", troughcolor='#ffdddd', background='#e74c3c')
style.configure("Moderate.Horizontal.TProgressbar", troughcolor='#fff3dd', background='#f39c12')
style.configure("Strong.Horizontal.TProgressbar", troughcolor='#ddffdd', background='#2ecc71')

entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Password:", font=("Arial", 12)).pack(side=tk.LEFT)

entry = tk.Entry(entry_frame, show='*', width=30, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)
entry.bind("<KeyRelease>", check_strength_live)

toggle_btn = tk.Button(entry_frame, text="👁️", command=lambda: [entry.config(show='' if entry.cget('show') == '*' else '*'), toggle_btn.config(text="👁️" if entry.cget('show') == '*' else "🙈")])
toggle_btn.pack(side=tk.LEFT)


progress = ttk.Progressbar(root, orient='horizontal', length=350, mode='determinate', style="Weak.Horizontal.TProgressbar")
progress.pack(pady=5)


strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12))
strength_label.pack()


feedback_text = tk.Text(root, height=8, width=50, font=("Arial", 10), wrap=tk.WORD, padx=10, pady=10)
feedback_text.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

generate_btn = tk.Button(button_frame, text="Generate Strong 🔑", command=generate_password, bg="#2ecc71", fg="white")
generate_btn.pack(side=tk.LEFT, padx=5)

suggest_btn = tk.Button(button_frame, text="Suggest Improvements ✨", command=suggest_improvement, bg="#3498db", fg="white")
suggest_btn.pack(side=tk.LEFT, padx=5)

clear_btn = tk.Button(button_frame, text="Clear 🧹", command=clear_fields, bg="#95a5a6", fg="white")
clear_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()