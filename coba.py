gaji_bulanan = int(input("Gaji bulanan : "))
masuk_kerja = int(input("Berapa hari anda bekerja ? "))
transport = 100000 * masuk_kerja
makan = 50000 * masuk_kerja
lembur = int(input("Berapa jam anda lembur ? "))

# Hitung total honor
if lembur <= 2:
    total_lembur = lembur * 100000
else:
    total_lembur = 2 * 100000 + (lembur - 2) * 150000

honor = gaji_bulanan + transport + makan + total_lembur
print("Honor yang anda dapat Rp.%i" % honor)