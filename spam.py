import pyautogui
import time
import tkinter as tk
from tkinter import ttk
import pyperclip
import random
import string

def create_virtex(text, repetitions, format_type, length):
    if format_type == 'Huruf Besar':
        text = text.upper()
    elif format_type == 'Huruf Kecil':
        text = text.lower()
    elif format_type == 'GEDE SEMUA':
        text = text.title()
    
    if length > 0:
        text = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    virtex = text + "\n"
    virtex = virtex * repetitions
    return virtex

# Kirim ke Whatsapp
def send_virtex_on_whatsapp(text, repetitions, interval, delay_between_messages):
    virtex = create_virtex(text, repetitions, format_combobox.get(), int(length_entry.get()))
    time.sleep(5)  # 5 Detik

    for _ in range(repetitions):
        pyautogui.typewrite(virtex)
        pyautogui.press('enter')
        time.sleep(interval)
        time.sleep(delay_between_messages)

def on_send_button_click():
    text = text_entry.get()
    repetitions = int(repetitions_entry.get())
    interval = float(interval_entry.get())
    delay_between_messages = float(delay_entry.get())
    send_virtex_on_whatsapp(text, repetitions, interval, delay_between_messages)
    if clipboard_var.get():
        pyperclip.copy(create_virtex(text, repetitions, format_combobox.get(), int(length_entry.get())))

def set_transparency():
    root.attributes('-alpha', 0.7)

root = tk.Tk()
root.title("All-chat Spammer @SilverWolfUwU")
root.geometry("400x300")
set_transparency()

root.configure(bg='#333333')

tk.Label(root, text="Teks:", bg="#333333", fg="white").grid(row=0, column=0, padx=10, pady=10)
text_entry = tk.Entry(root, width=50)
text_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Jumlah Pengulangan:", bg="#333333", fg="white").grid(row=1, column=0, padx=10, pady=10)
repetitions_entry = tk.Entry(root, width=10)
repetitions_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Interval (detik):", bg="#333333", fg="white").grid(row=2, column=0, padx=10, pady=10)
interval_entry = tk.Entry(root, width=10)
interval_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Delay antara chat (detik):", bg="#333333", fg="white").grid(row=3, column=0, padx=10, pady=10)
delay_entry = tk.Entry(root, width=10)
delay_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Panjang Teks Acak (0 untuk gaada):", bg="#333333", fg="white").grid(row=4, column=0, padx=10, pady=10)
length_entry = tk.Entry(root, width=10)
length_entry.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Format Teks:", bg="#333333", fg="white").grid(row=5, column=0, padx=10, pady=10)
format_combobox = ttk.Combobox(root, values=["Huruf Besar", "Huruf Kecil", "GEDE SEMUA", "Gaada"])
format_combobox.set("None")
format_combobox.grid(row=5, column=1, padx=10, pady=10)

clipboard_var = tk.BooleanVar()
tk.Checkbutton(root, text="Copy ke Keyboard", variable=clipboard_var, bg="#333333", fg="white").grid(row=6, column=0, columnspan=2, pady=10)

send_button = ttk.Button(root, text="Kirim", command=on_send_button_click)
send_button.grid(row=7, column=0, columnspan=2, pady=20)

#loop gui @silverwolfhsr
root.mainloop()
