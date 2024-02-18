import random
import tkinter as tk
from tkinter import StringVar, IntVar

def encrypt_decrypt():
    global q
    a = input_var.get()
    m = mode_var.get()

    first = ''
    second = ''
    key1 = 0
    key2 = 0
    key = 0
    b = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+=-12345678901234567890'
    q = ''

    if m == 1:
        while key % 10 == 0 or key % 11 == 0:
            key = random.randint(10, 99)
        key = str(key)
        key1 = int(key[0:1])
        key2 = int(key[1:2])
        first = a[0:len(a)//2]
        second = a[len(a)//2:len(a)]
        for i in first:
            q += b[b.find(i) + key1]
        for j in second:
            q += b[b.find(j) + key2]
        q += key
        result_label.config(text="THE ENCRYPTED STRING:")
    elif m == 2:
        key1 = int(a[-2:-3:-1])
        key2 = int(a[-1:-2:-1])
        a = a[0:len(a)-2]
        first = a[0:len(a)//2]
        second = a[len(a)//2:len(a)]
        for i in first:
            q += b[b.find(i) - key1]
        for j in second:
            q += b[b.find(j) - key2]
        result_label.config(text="THE DECRYPTED STRING:")

    result_var.set(q)


window = tk.Tk()
window.title("ENIGMA")
window.geometry("1920x1080")
window.configure(bg='black')


enigma_label = tk.Label(window, text="ENIGMA", font=("Helvetica", 36, "bold"), fg='red', bg='black')
enigma_label.pack(pady=20)

input_label = tk.Label(window, text="Enter a String:", font=("Helvetica", 24), fg='red', bg='black')
input_label.pack(pady=20)

input_var = StringVar()
input_entry = tk.Entry(window, textvariable=input_var, font=("Helvetica", 20), bd=10)
input_entry.pack(pady=10)

mode_var = IntVar()
mode_var.set(1)  
encryption_radio = tk.Radiobutton(window, text="Encryption", variable=mode_var, value=1, font=("Helvetica", 20), fg='red', bg='black')
encryption_radio.pack()
decryption_radio = tk.Radiobutton(window, text="Decryption", variable=mode_var, value=2, font=("Helvetica", 20), fg='red', bg='black')
decryption_radio.pack()

encrypt_button = tk.Button(window, text="Encrypt/Decrypt", command=encrypt_decrypt, font=("Helvetica", 24), fg='red', bg='black', bd=10)
encrypt_button.pack(pady=20)

result_label = tk.Label(window, text="", font=("Helvetica", 24), fg='red', bg='black')
result_label.pack()

result_var = StringVar()
result_entry = tk.Entry(window, textvariable=result_var, state='readonly', font=("Helvetica", 20), bd=10)
result_entry.pack(pady=10)

window.mainloop()

