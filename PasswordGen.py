import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        # Get user input
        length = int(entry_length.get())
        if length < 6:
            messagebox.showerror("Error", "Password length must be at least 6.")
            return
        
        # Get character options
        include_lowercase = var_lowercase.get()
        include_uppercase = var_uppercase.get()
        include_digits = var_digits.get()
        include_special = var_special.get()
        
        # Ensure at least one type is selected
        if not (include_lowercase or include_uppercase or include_digits or include_special):
            messagebox.showerror("Error", "At least one character type must be selected.")
            return
        
        # Build character pool and mandatory characters
        char_pool = ""
        mandatory_chars = []

        if include_lowercase:
            char_pool += string.ascii_lowercase
            mandatory_chars.append(random.choice(string.ascii_lowercase))
        if include_uppercase:
            char_pool += string.ascii_uppercase
            mandatory_chars.append(random.choice(string.ascii_uppercase))
        if include_digits:
            char_pool += string.digits
            mandatory_chars.append(random.choice(string.digits))
        if include_special:
            char_pool += string.punctuation
            mandatory_chars.append(random.choice(string.punctuation))

        # Ensure length is sufficient
        if length < len(mandatory_chars):
            messagebox.showerror("Error", f"Password length must be at least {len(mandatory_chars)} to include all selected types.")
            return
        
        # Generate remaining random characters
        remaining_length = length - len(mandatory_chars)
        random_chars = random.choices(char_pool, k=remaining_length)
        
        # Combine and shuffle characters
        password_list = mandatory_chars + random_chars
        random.shuffle(password_list)
        password = ''.join(password_list)
        
        # Display generated password
        result_label.config(text=f"Generated Password: {password}")
        copy_button.config(state=tk.NORMAL)  # Enable the copy button
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

def copy_to_clipboard():
    # Copy the generated password to clipboard
    password = result_label.cget("text").replace("Generated Password: ", "")
    if password.strip():
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy.")

# Create main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x450")

# Title Label
tk.Label(root, text="Advanced Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

# Password Length
tk.Label(root, text="Enter Password Length (min 6):").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Character Options
tk.Label(root, text="Include the following:").pack(pady=5)

var_lowercase = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Lowercase Letters", variable=var_lowercase).pack(anchor='w', padx=20)

var_uppercase = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Uppercase Letters", variable=var_uppercase).pack(anchor='w', padx=20)

var_digits = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Digits", variable=var_digits).pack(anchor='w', padx=20)

var_special = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Special Characters", variable=var_special).pack(anchor='w', padx=20)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white").pack(pady=20)

# Result Label
result_label = tk.Label(root, text="Generated Password: ", wraplength=350, font=("Helvetica", 12))
result_label.pack(pady=10)

# Copy to Clipboard Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED, bg="green", fg="white")
copy_button.pack(pady=10)

# Run main loop
root.mainloop()
