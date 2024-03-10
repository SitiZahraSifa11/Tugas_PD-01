# 2. Menghitung uang yang harus dibayar untuk membeli mangga dengan kriteria

# jika beli 2 kilo atau kurang harga perkilonya 20.000

# jika beli lebih dari 2 kilo sampe dengan 5 kilo harga perkilonya 18.000

# jika beli lebih dari 5 kilo harga perkilonya 16.000

# Berapa banyak yang harus dibayar jika beli 10 kilo?

# contoh output: Harga yang harus dibayar untuk membeli 10 kilo mangga adalah 160.000
kg = int(input("Berapa kg mangga yang akan di beli  : "))

if kg <= 2:
    harga = 20_000
elif kg <= 5:
    harga = 18_000
else : 
    harga = 16_000

totalHarga = kg* harga
print("Harga yang harus di bayar adalah Rp. %i " %totalHarga)


