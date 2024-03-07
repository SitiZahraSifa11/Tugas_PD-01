#Buatlah konversi nilai dengan kriteria

#<50 E
#50-60 D
#60-70 C
#70-80 B
#selebihnya A


nilai = int(input("masukan nilai anda  : "))

if nilai < 50 :
    print(" Ada di Kriteria E")
elif nilai >= 50 and nilai < 60:
     print(" Ada di Kriteria D")  
elif nilai >= 60 and nilai < 70:
     print(" Ada di Kriteria C")  
elif nilai >= 70 and nilai < 80:
     print(" Ada di Kriteria B")  
else :
     print("Ada di kriteria A")
