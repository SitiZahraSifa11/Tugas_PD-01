umur = int(input("Berapa umur anda: "))

if umur <=2 :
   kategori = ("Bayi")
elif umur <=5 :
    kategori = ("Balita")
elif umur <=12 :
    kategori = ("Anak - Anak")
elif umur <=17 :
    kategori = ("Remaja")
elif umur >17 and umur <=30 :
    kategori = ("Dewasa")
else :
    kategori = ("Orang Tua")
print(kategori)