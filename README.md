Password Strength Checker

A simple and interactive desktop application built with Python's Tkinter library that helps users assess the strength of their passwords in real-time. The app provides live feedback, a visual strength meter, suggestions for improvement, and a secure password generator. 

FEATURES:
 Real-time password strength checking
 Visual strength meter with progress bar
 Feedback and suggestions to improve weak passwords
 Password visibility toggle 
 Secure random password generator using secrets module
Simple and responsive Tkinter GUI

Requirements
    • Python 3.x
    • Tkinter (comes pre-installed with Python)
    • Standard libraries only (re, string, secrets)

How to Run
    1. Clone the repository:
git clone https://github.com/tensei-81/PASSWORD-STRENGTH-CHECKER
cd PASSWORD-STRENGTH-CHECKER
    2. Run the application:
python3 password_strength2.py

How It Works
    • Passwords are evaluated based on:
        ◦ Length
        ◦ Uppercase and lowercase letters
        ◦ Digits
        ◦ Special characters
    • A score is calculated and mapped to:
        ◦ Weak 
        ◦ Moderate 
        ◦ Strong 
    • Suggestions are displayed to guide the user in creating a strong password.
