# Import necessary libraries
import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
import os

def encrypt_file(file_path, key):
    """
    Encrypts the selected file using AES-256 encryption.
    The encrypted file will have a '.enc' extension.
    """
    try:
        cipher = AES.new(key, AES.MODE_EAX)
        with open(file_path, 'rb') as f:
            data = f.read()
        ciphertext, tag = cipher.encrypt_and_digest(data)

        with open(file_path + ".enc", "wb") as file_out:
            file_out.write(cipher.nonce)      # Nonce is needed for decryption
            file_out.write(tag)                # Authentication tag for integrity check
            file_out.write(ciphertext)         # Encrypted file data
        messagebox.showinfo("Success", f"File Encrypted:\n{file_path}.enc")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption Failed:\n{str(e)}")

def decrypt_file(file_path, key):
    """
    Decrypts the selected AES-256 encrypted file.
    The decrypted file will have a '.dec' extension.
    """
    try:
        with open(file_path, "rb") as file_in:
            nonce = file_in.read(16)            # Read nonce
            tag = file_in.read(16)              # Read tag
            ciphertext = file_in.read()         # Read encrypted data

        cipher = AES.new(key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)

        output_file = file_path.replace(".enc", ".dec")
        with open(output_file, "wb") as f:
            f.write(data)
        messagebox.showinfo("Success", f"File Decrypted:\n{output_file}")
    except ValueError:
        messagebox.showerror("Error", "Decryption Failed:\nIncorrect Key or Corrupted File.")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption Failed:\n{str(e)}")

def browse_file():
    """
    Opens file dialog to select a file.
    """
    file_path.set(filedialog.askopenfilename())

def process_file():
    """
    Processes the selected file based on the user's choice (Encrypt/Decrypt).
    """
    path = file_path.get()
    key_text = key_entry.get()

    if not path:
        messagebox.showwarning("Missing File", "Please select a file first.")
        return
    if len(key_text) != 32:
        messagebox.showwarning("Invalid Key", "Key must be exactly 32 characters long.")
        return

    key = key_text.encode('utf-8')

    if action.get() == "encrypt":
        encrypt_file(path, key)
    else:
        decrypt_file(path, key)

# Initialize main application window
root = tk.Tk()
root.title("AES-256 File Encryptor & Decryptor")
root.geometry("500x350")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Variables
file_path = tk.StringVar()
action = tk.StringVar(value="encrypt")

# GUI Widgets
tk.Label(root, text="Select File:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
tk.Entry(root, textvariable=file_path, width=50, font=("Arial", 10)).pack()
tk.Button(root, text="Browse", command=browse_file, bg="#4caf50", fg="white", font=("Arial", 10)).pack(pady=5)

tk.Label(root, text="Enter 32-Character Secret Key:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=15)
key_entry = tk.Entry(root, width=50, show="*", font=("Arial", 10))
key_entry.pack()

tk.Label(root, text="Select Action:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=15)
tk.Radiobutton(root, text="Encrypt", variable=action, value="encrypt", bg="#f0f0f0", font=("Arial", 10)).pack()
tk.Radiobutton(root, text="Decrypt", variable=action, value="decrypt", bg="#f0f0f0", font=("Arial", 10)).pack()

tk.Button(root, text="Process", command=process_file, bg="#2196f3", fg="white", font=("Arial", 12)).pack(pady=25)

# Start the application
root.mainloop()
