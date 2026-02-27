#Fungsi untuk menghitung rata-rata dari sejumlah angka
def hitung_rata_rata(angka):
    total = sum(angka)
    rata-rata = total /  len(angka)
    return rata_rata

#Fungsi untuk mendapatkan input angka dari pengguna
def input_angka():
    angka = []
    while true:
        try:
            bilangan = float (input("Masukkan angka (0 untuk mengakhiri): "))
            if bilangan == 0:
                break
            angka.append(bilangan)
        except ValueError:
            print("Masukkan angka yang valid.")
    return angka

#program  utama
if _name_== "_main_":
   print("Program Menghitung rata-rata")
   daftar_angka = input_angka()

   if daftar_angka:
       rata-rata = hitung_rata_rata(daftar_angka)
       print(f"Rata-rata dari angka-angka yang dimasukkan adalah: {rata-rata:.2f}")
   else:
       print("Tidak ada angka yang dimasukkan.")
