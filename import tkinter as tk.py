import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Fungsi untuk menambah data ke tabel
def tambah_data():
    nama = entry_nama.get()
    kelas = entry_kelas.get()
    if nama and kelas:
        tree.insert("", "end", values=(nama, kelas))
        entry_nama.delete(0, tk.END)
        entry_kelas.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Mohon isi semua bidang!")

# Fungsi untuk menghapus data terpilih
def hapus_data():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Selection Error", "Pilih data yang akan dihapus!")

# Setup Window Utama
app = tk.Tk()
app.title("Program Data Siswa - Tkinter")
app.geometry("500x400")

# Input Frame
frame_input = tk.Frame(app)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nama:").grid(row=0, column=0, padx=5, pady=5)
entry_nama = tk.Entry(frame_input)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Kelas:").grid(row=1, column=0, padx=5, pady=5)
entry_kelas = tk.Entry(frame_input)
entry_kelas.grid(row=1, column=1, padx=5, pady=5)

# Button Frame
frame_btn = tk.Frame(app)
frame_btn.pack(pady=10)

btn_tambah = tk.Button(frame_btn, text="Tambah", command=tambah_data)
btn_tambah.pack(side=tk.LEFT, padx=10)

btn_hapus = tk.Button(frame_btn, text="Hapus", command=hapus_data)
btn_hapus.pack(side=tk.LEFT, padx=10)

# Tabel Data
columns = ("nama", "kelas")
tree = ttk.Treeview(app, columns=columns, show="headings")
tree.heading("nama", text="Nama Siswa")
tree.heading("kelas", text="Kelas")
tree.pack(pady=10, fill=tk.BOTH, expand=True)

app.mainloop()
