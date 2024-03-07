# Buatlah Perhitungan IPK untuk semester ini berdasarkan nilai yang di input
#Mata kuliah semster ini adalah Algoritma, Perancangan Objek, Kalkulus, Etika Profesi, Databases, dan English




def hitungNilai(nilai):
    if nilai >= 90:
        return 'A', 4.0
    elif nilai >= 85:
        return 'A-', 3.75
    elif nilai >= 80:
        return 'A/B', 3.5
    elif nilai >= 75:
        return 'B+', 3.25
    elif nilai >= 70:
        return 'B', 3.0
    elif nilai >= 65:
        return 'B-', 2.75
    elif nilai >= 60:
        return 'B/C', 2.5
    elif nilai >= 55:
        return 'C+', 2.25
    elif nilai >= 50:
        return 'C', 2.0
    elif nilai >= 45:
        return 'C-', 1.75
    elif nilai >= 40:
        return 'C/D', 1.5
    elif nilai >= 35:
        return 'D+', 1.25
    elif nilai >= 30:
        return 'D', 1.0
    else:
        return 'E', 0

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

total_nilai_bobot = 0
for nilai, sks, mata_kuliah in [(algoritma, sks_algoritma, 'Algoritma'),
                                (perancangan_objek, sks_perancangan_objek, 'Perancangan Objek'),
                                (kalkulus, sks_kalkulus, 'Kalkulus'),
                                (etika_profesi, sks_etika_profesi, 'Etika Profesi'),
                                (databases, sks_databases, 'Databases'),
                                (english, sks_english, 'English')]:
    nilai_huruf, bobot = hitungNilai(nilai)
    total_nilai_bobot += bobot * sks
    
    print(f"Untuk Mata kuliah {mata_kuliah} dengan {sks} SKS nilai yang di peroleh  :{nilai_huruf} ")

IPK = total_nilai_bobot / total_sks

print(f"Total IPK Anda adalah {IPK:.2f}")
