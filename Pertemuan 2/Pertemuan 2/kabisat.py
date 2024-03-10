tahun = int(input("Masukan tahun :"))

if tahun % 4 == 0 :
    status = ("Tahun Kabisat")
else : 
    status = ("Bukan tahun Kabisat")
print(status)