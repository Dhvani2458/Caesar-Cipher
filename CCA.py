import tkinter as tk
from tkinter import ttk, messagebox

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher Encryption/Decryption")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        
        # Set app style
        self.style = ttk.Style()
        
        # Configure different button styles with custom colors
        self.style.configure("Encrypt.TButton", font=("Arial", 10), background="#4CAF50", foreground="black")
        self.style.configure("Decrypt.TButton", font=("Arial", 10), background="#2196F3", foreground="black")
        self.style.configure("Clear.TButton", font=("Arial", 10), background="#f44336", foreground="black")
        self.style.map('Encrypt.TButton', background=[('active', '#45a049')])
        self.style.map('Decrypt.TButton', background=[('active', '#0b7dda')])
        self.style.map('Clear.TButton', background=[('active', '#d32f2f')])
        
        self.style.configure("TLabel", font=("Arial", 10), background="#f0f0f0")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Caesar Cipher Tool", font=("Arial", 16, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(fill="both", padx=20, pady=10)
        
        # Message entry
        message_label = tk.Label(input_frame, text="Enter Message:", font=("Arial", 10), bg="#f0f0f0")
        message_label.pack(anchor="w")
        
        self.message_text = tk.Text(input_frame, height=5, width=50, font=("Arial", 10))
        self.message_text.pack(fill="both", expand=True, pady=5)
        
        # Shift value
        shift_frame = tk.Frame(self.root, bg="#f0f0f0")
        shift_frame.pack(fill="x", padx=20, pady=5)
        
        shift_label = tk.Label(shift_frame, text="Shift Value (1-25):", font=("Arial", 10), bg="#f0f0f0")
        shift_label.pack(side="left")
        
        self.shift_var = tk.IntVar(value=3)
        self.shift_spinbox = ttk.Spinbox(
            shift_frame, 
            from_=1, 
            to=25, 
            textvariable=self.shift_var,
            width=5,
            font=("Arial", 10)
        )
        self.shift_spinbox.pack(side="left", padx=10)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(fill="x", padx=20, pady=10)
        
        self.encrypt_button = ttk.Button(
            button_frame, 
            text="Encrypt", 
            command=self.encrypt,
            style="Encrypt.TButton",
            width=15
        )
        self.encrypt_button.pack(side="left", padx=10)
        
        self.decrypt_button = ttk.Button(
            button_frame, 
            text="Decrypt", 
            command=self.decrypt,
            style="Decrypt.TButton",
            width=15
        )
        self.decrypt_button.pack(side="left", padx=10)
        
        self.clear_button = ttk.Button(
            button_frame, 
            text="Clear All", 
            command=self.clear_all,
            style="Clear.TButton",
            width=15
        )
        self.clear_button.pack(side="left", padx=10)
        
        # Output frame
        output_frame = tk.Frame(self.root, bg="#f0f0f0")
        output_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        output_label = tk.Label(output_frame, text="Result:", font=("Arial", 10), bg="#f0f0f0")
        output_label.pack(anchor="w")
        
        self.result_text = tk.Text(output_frame, height=5, width=50, font=("Arial", 10))
        self.result_text.pack(fill="both", expand=True, pady=5)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(
            self.root, 
            textvariable=self.status_var, 
            bd=1, 
            relief=tk.SUNKEN, 
            anchor=tk.W,
            font=("Arial", 9),
            bg="#e0e0e0"
        )
        status_bar.pack(side="bottom", fill="x")
    
    def encrypt(self):
        try:
            message = self.message_text.get("1.0", "end-1c")
            shift = self.shift_var.get()
            
            if not message:
                self.status_var.set("Error: Please enter a message")
                return
            
            result = self.caesar_cipher(message, shift, encrypt=True)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert("1.0", result)
            self.status_var.set(f"Message encrypted with shift value: {shift}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during encryption: {str(e)}")
            self.status_var.set("Error during encryption")
    
    def decrypt(self):
        try:
            message = self.message_text.get("1.0", "end-1c")
            shift = self.shift_var.get()
            
            if not message:
                self.status_var.set("Error: Please enter a message")
                return
            
            result = self.caesar_cipher(message, shift, encrypt=False)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert("1.0", result)
            self.status_var.set(f"Message decrypted with shift value: {shift}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during decryption: {str(e)}")
            self.status_var.set("Error during decryption")
    
    def caesar_cipher(self, text, shift, encrypt=True):
        """
        Apply Caesar cipher to the given text
        
        Args:
            text (str): Text to encrypt/decrypt
            shift (int): Shift value (1-25)
            encrypt (bool): True for encrypt, False for decrypt
            
        Returns:
            str: Encrypted/decrypted text
        """
        result = ""
        
        # If decrypting, reverse the shift
        if not encrypt:
            shift = -shift
        
        for char in text:
            if char.isalpha():
                # Determine ASCII offset based on case
                ascii_offset = ord('A') if char.isupper() else ord('a')
                
                # Apply Caesar cipher formula: (position + shift) % 26
                shifted_position = (ord(char) - ascii_offset + shift) % 26
                new_char = chr(shifted_position + ascii_offset)
                result += new_char
            else:
                # Keep non-alphabetic characters as is
                result += char
        
        return result
    
    def clear_all(self):
        """Clear all input and output fields"""
        self.message_text.delete("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)
        self.shift_var.set(3)
        self.status_var.set("All fields cleared")


if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
