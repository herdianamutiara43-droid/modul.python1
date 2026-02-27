# program Menghitung Luas dan keLiLing Bangun Datar 
# python

print("--- Program Hitung persegi ---")
sisi = float(input("Masukkan sisi persegi: "))
luas_p = sisi * sisi
keliling_p = 4 * sisi
print(f"Luas: {luas_p}, keliling: {keliling_p}\n")

print("--- Program Hitung Persegi Panjang ---")
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
luas_pp = panjang * lebar
keliling_pp = 2 * (panjang + lebar)
print(f"Luas: {luas_pp}, keliling: {keliling_pp}\n")

print("--- Program Hitung Trapesium ---")
a = float(input("Masukkan sisi atas: "))
b = float(input("Masukkan sisi bawah: "))
t = float(input("Masukkan tinggi: "))
sisi_miring1 = float(input("Masukkan sisi miring 1: "))
sisi_miring2 = float(input("Masukkan sisi miring 2: "))
luas_t = 0.5 * (a + b) * t
keliling_t = a + b + sisi_miring1 + sisi_miring2
print(f" luas: {luas_t}, keliling: {keliling_t} ")