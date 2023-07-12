import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_scale.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''
    while not any(char.isdigit() for char in password):
        password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    password = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def copy_button_click():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo('Erfolg', 'Das Passwort wurde in die Zwischenablage kopiert!')

root = tk.Tk()
root.title('Passwort-Generator')

main_frame = tk.Frame(root, bg='white')
main_frame.pack(padx=20, pady=20)

title_label = tk.Label(main_frame, text='Passwort-Generator', font=('Arial', 16), bg='white')
title_label.grid(row=0, column=0, columnspan=2, pady=10)

length_label = tk.Label(main_frame, text='Passwortlänge:', font=('Arial', 12), bg='white')
length_label.grid(row=1, column=0, sticky='w')

length_scale = tk.Scale(main_frame, from_=8, to=20, orient=tk.HORIZONTAL, length=200, bg='white')
length_scale.grid(row=1, column=1, padx=10)

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(main_frame, text='Zahlen einbeziehen', variable=digits_var, font=('Arial', 12), bg='white')
digits_checkbox.grid(row=2, column=0, pady=5, sticky='w')

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(main_frame, text='Sonderzeichen einbeziehen', variable=special_chars_var, font=('Arial', 12), bg='white')
special_chars_checkbox.grid(row=3, column=0, pady=5, sticky='w')

generate_button = tk.Button(main_frame, text='Generieren', command=generate_button_click, font=('Arial', 12), bg='white', fg='blue')
generate_button.grid(row=4, column=0, pady=10, sticky='w')

copy_button = tk.Button(main_frame, text='Kopieren', command=copy_button_click, font=('Arial', 12), bg='white', fg='blue')
copy_button.grid(row=4, column=1, pady=10, padx=10, sticky='e')

password_entry = tk.Entry(main_frame, width=30, font=('Arial', 12))
password_entry.grid(row=5, columnspan=2, pady=10)

root.configure(bg='white')
root.mainloop()


