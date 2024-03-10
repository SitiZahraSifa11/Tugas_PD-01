# 3. Menentukan kriteria kelulusan berdasarkan aturan dibawah ini:
# Nilai yang di input ada 5 : English, MTK, Indo, IPA, IPS
# A. Jika Rata-rata nilai 3 Mata pelajaran (English, MTK, dan Indo) >= 75, maka dia lulus
# B. Jika rata-rata semua pelajaran >=70 dia lulus
# C. Jika Nilai English dan MTK lebih 90 maka dia lulus meskipun nilai yang lain 0

English = int(input("Masukan nilai English anda  : "))
Mtk= int(input("Masukan nilai Matematika anda  : "))
Indo = int(input("Masukan nilai Indonesia anda  : "))
Ipa = int(input("Masukan nilai IPA anda  : "))
Ips = int(input("Masukan nilai IPS anda  : "))

rataA= (English + Mtk + Indo) / 3
rataB = (English + Mtk + Indo+Ipa+Ips) / 5

if rataA >= 75:
    kelulusan = "Lulus"
elif rataB >= 70:
    kelulusan = "Lulus"
elif English >90 and Mtk>90:
    kelulusan ="Lulus"
else:
    kelulusan="Maaf tidak lulus"

print(kelulusan)