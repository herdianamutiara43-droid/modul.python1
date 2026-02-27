import tkinter as tk
from tkinter import messagebox

def hitung_total():
    try:
        harga = float(entry_harga.get())
        kuantitas = float(entry_kuantitas.get())
        total = harga * kuantitas
        label_total_value.config(text=f"Rp.{total:,.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka yang valid untuk Harga dan Kuantitas.")

# Setup jendela utama
root = tk.Tk()
root.title("Program Kasir")
root.geometry("300x200")

# Label dan Entry Harga
label_harga = tk.Label(root, text="Harga:")
label_harga.grid(row=0, column=0, padx=10, pady=5, sticky='w')
entry_harga = tk.Entry(root)
entry_harga.grid(row=0, column=1, padx=10, pady=5)

# Label dan Entry Kuantitas
label_kuantitas = tk.Label(root, text="Kuantitas:")
label_kuantitas.grid(row=1, column=0, padx=10, pady=5, sticky='w')
entry_kuantitas = tk.Entry(root)
entry_kuantitas.grid(row=1, column=1, padx=10, pady=5)

# Tombol Hitung Total
button_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
button_hitung.grid(row=2, column=0, columnspan=2, pady=10)

# Label Total
label_total = tk.Label(root, text="Total:")
label_total.grid(row=3, column=0, padx=10, pady=5, sticky='w')
label_total_value = tk.Label(root, text="Rp.0.00", font=("Helvetica", 12, "bold"))
label_total_value.grid(row=3, column=1, padx=10, pady=5, sticky='e')

# Jalankan aplikasi
root.mainloop()