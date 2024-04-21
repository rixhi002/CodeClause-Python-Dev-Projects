import tkinter as tk
import random
import string
import pyperclip

# Define a function to generate the password
def generate_password():
    length = int(length_entry.get())
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    if length < 8:
        password_entry.insert("end", "Error: Password must be at least 8 characters long.")
        return

    alphabet = string.ascii_lowercase
    if use_numbers:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation

    pwd = ''.join(random.choice(alphabet) for _ in range(length))
    pwd = "".join(random.sample(pwd, len(pwd)))

    return pwd

# Define a function to copy the password to the clipboard
def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create the input fields and labels
length_label = tk.Label(root, text="Password length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root, width=10, font=("Arial", 14))
length_entry.grid(row=0, column=1, padx=5, pady=5)

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Include numbers", variable=numbers_var)
numbers_checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="w")

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Include symbols", variable=symbols_var)
symbols_checkbox.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Create the password generation button
generate_button = tk.Button(root, text="Generate password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create the password entry field
password_entry = tk.Entry(root, width=30, font=("Arial", 14))
password_entry.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create the copy to clipboard button
copy_button = tk.Button(root, text="Copy to clipboard", command=copy_to_clipboard)
copy_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Start the main loop
root.mainloop()