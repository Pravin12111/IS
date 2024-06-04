#program to create instance messaging and encrypt messages in information security
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import base64
import hashlib

class ChatApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Secure Chat")
        self.root.geometry("400x400")

        self.message = tk.StringVar()
        self.key = tk.StringVar()
        self.mode = tk.IntVar()
        self.output = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        headingFrame1 = tk.Frame(self.root, bg="gray91", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.7, relheight=0.16)
        headingLabel = tk.Label(headingFrame1, text="Welcome to Secure Chat", fg='grey19', font=('Courier', 15, 'bold'))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        label1 = tk.Label(self.root, text='Enter the Message', font=('Courier', 10))
        label1.place(x=10, y=150)
        msg = tk.Entry(self.root, textvariable=self.message, width=35, font=('calibre', 10, 'normal'))
        msg.place(x=200, y=150)

        label2 = tk.Label(self.root, text='Enter the Key', font=('Courier', 10))
        label2.place(x=10, y=200)
        InpKey = tk.Entry(self.root, textvariable=self.key, width=35, font=('calibre', 10, 'normal'))
        InpKey.place(x=200, y=200)

        label3 = tk.Label(self.root, text='Check one of encrypt or decrypt', font=('Courier', 10))
        label3.place(x=10, y=250)
        tk.Radiobutton(self.root, text='Encrypt', variable=self.mode, value=1).place(x=100, y=300)
        tk.Radiobutton(self.root, text='Decrypt', variable=self.mode, value=2).place(x=200, y=300)

        label4 = tk.Label(self.root, text='Result', font=('Courier', 10))
        label4.place(x=10, y=350)
        Output = tk.Label(self.root, textvariable=self.output, font=('Courier', 10))
        Output.place(x=200, y=350)

        def Result():
            msg = self.message.get()
            k = self.key.get()
            i = self.mode.get()
            if i == 1:
                self.output.set(self.encrypt(msg, k))
            elif i == 2:
                self.output.set(self.decrypt(msg, k))
            else:
                messagebox.showinfo('Secure Chat', 'Please Choose one of Encryption or Decryption. Try again.')

        def Reset():
            self.message.set("")
            self.key.set("")
            self.mode.set(0)
            self.output.set("")

        ShowBtn = tk.Button(self.root, text="Show Message", bg='lavender blush2', fg='black', width=15, height=1, command=Result)
        ShowBtn['font'] = font.Font(size=12)
        ShowBtn.place(x=180, y=400)

        ResetBtn = tk.Button(self.root, text='Reset', bg='honeydew2', fg='black', width=15, height=1, command=Reset)
        ResetBtn['font'] = font.Font(size=12)
        ResetBtn.place(x=15, y=400)

        QuitBtn = tk.Button(self.root, text='Exit', bg='old lace', fg='black', width=15, height=1, command=self.root.destroy)
        QuitBtn['font'] = font.Font(size=12)
        QuitBtn.place(x=345, y=400)

        self.root.mainloop()

    def encrypt(self, message, key):
        encrypted_message = ""
        for i in range(len(message)):
            list_key = key[i % len(key)]
            encrypted_message += chr((ord(message[i]) + ord(list_key)) % 256)
        return base64.urlsafe_b64encode(encrypted_message.encode()).decode()

    def decrypt(self, message, key):
        decrypted_message = base64.urlsafe_b64decode(message.encode()).decode()
        decrypted_message = ""
        for i in range(len(decrypted_message)):
            list_key = key[i % len(key)]
            decrypted_message += chr((ord(decrypted_message[i]) - ord(list_key)) % 256)
        return decrypted_message

if __name__ == "__main__":
    app = ChatApp()
