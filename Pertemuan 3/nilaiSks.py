# Buatlah Perhitungan IPK untuk semester ini berdasarkan nilai yang di input
#Mata kuliah semster ini adalah Algoritma, Perancangan Objek, Kalkulus, Etika Profesi, Databases, dan English




def hitungNilai(nilai):
    if nilai >= 85:
        return 4.00
    elif nilai >= 70:
        return 3.00
    elif nilai >= 55:
        return 2.00
    elif nilai >= 40:
        return 1.00
    else:
        return 0.00
    
algoritma = float(input("Masukkan nilai Algoritma: "))
sks_algoritma = int(input("Masukkan SKS Algoritma: "))
perancangan_objek = float(input("Masukkan nilai Perancangan Objek: "))
sks_perancangan_objek = int(input("Masukkan SKS Perancangan Objek: "))
kalkulus = float(input("Masukkan nilai Kalkulus: "))
sks_kalkulus = int(input("Masukkan SKS Kalkulus: "))
etika_profesi = float(input("Masukkan nilai Etika Profesi: "))
sks_etika_profesi = int(input("Masukkan SKS Etika Profesi: "))
databases = float(input("Masukkan nilai Databases: "))
sks_databases = int(input("Masukkan SKS Databases: "))
english = float(input("Masukkan nilai English: "))
sks_english = int(input("Masukkan SKS English: "))

total_sks = sks_algoritma + sks_perancangan_objek + sks_kalkulus + sks_etika_profesi + sks_databases + sks_english
total_nilai = (hitungNilai(algoritma) * sks_algoritma +
               hitungNilai(perancangan_objek) * sks_perancangan_objek +
               hitungNilai(kalkulus) * sks_kalkulus +
               hitungNilai(etika_profesi) * sks_etika_profesi +
               hitungNilai(databases) * sks_databases +
               hitungNilai(english) * sks_english)

IPK = total_nilai / total_sks

print ("Nilai anda %i"%IPK)

print(f"Total IPK Anda adalah {IPK:.2f}")