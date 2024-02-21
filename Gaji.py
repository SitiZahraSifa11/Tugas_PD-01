#Menghitung Gaji
# gajiBulanan = 
# transport = 100.000/hari
# makan = 50.000/hari
# uang lembur = 2 jam pertama itu 100.000, selebihnya 150.000

# berapa honor yang saya dapatkan jika saya bekerja selama 21 hari dan lembur 10 jam.

gaji_bulanan=int(input("Gaji bulanan : "))
masuk_kerja=int(input("Berapa hari anda bekerja ? "))
transport=100000 * masuk_kerja
makan=50000 * masuk_kerja
lembur = int(input("Berapa jam anda lembur ? "))
if lembur <= 2:
    total_lembur = lembur * 100000
else :
    total_lembur = 2 * 100000 + (lembur - 2) * 150000

honor = gaji_bulanan+transport+makan+total_lembur
print("Honor yang anda dapat Rp.%i"%honor) 
