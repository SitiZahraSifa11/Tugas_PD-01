#Buatlah form pendaftaran untuk masuk universitas
#Nama, Tempat lahir, Tanggal Lahir, Tahun lahir, 3 Nilai Mata Pelajaran (English, Mtk, Indonesia), Jenis Kelamin
#Dia akan disarankan ke
#Jurusan Teknik Informatika jika rata-rata nilainya >=80 dan jenis kelaminnya laki-laki
#Jurusan Sistem Informasi jika rata-rata nilainya >=80 dan jenis kelamin Perempuan
#Selebihnya disarankan masuk jurusan DKV
#Meskipun demikian, Mahasiswa yang diterima hanya yang dibawah umur 25

print("                                                                            ")
print("                  FORM PENDAFTARAN UNIVERSITAS NUSA PUTRA                   ")
print("                                                                            ")
print("----------------------------------------------------------------------------")
print("Selamat datang")
print("Silahkan Lengkapi biodata anda")
print("----------------------------------------------------------------------------")

nama = input("Masukan nama lengkap anda                          : ")
tempatLahir = input("Masukan tempat lahir anda                          :")
tanggalLahir= int(input("Masukan tanggal lahir anda                         :"))
tahunLahir  = int(input("Masukan tahun lahir anda                           :"))
jenisKelamin= input("Masukan jenis kelamin anda (lakilaki / perempuan)  :")
tahunDaftar = int(input("Masukan tahun anda mendaftar                       : "))

print("----------------------------------------------------------------------------")
print("Selanjutnya masukan nilai mata pelajaran :English, Mtk, Indonesia. ")
print("----------------------------------------------------------------------------")

english = float(input("Masukan nilai mata pelajaran english anda   : "))
mtk = float(input("Masukan nilai mata pelajaran MTK anda       : "))
indonesia = float(input("Masukan nilai mata pelajaran indonesia anda :"))

umur = tahunDaftar-tahunLahir
print("----------------------------------------------------------------------------")
print("\nData Pendaftaran")
print(f"Nama                 : {nama}")
print(f"Tempat, Tanggal Lahir: {tempatLahir}, {tanggalLahir}, {tahunLahir}")
print(f"Nilai English        : {english}")
print(f"Nilai Matematika     : {mtk}")
print(f"Nilai Indonesia      : {indonesia}")
print(f"Jenis Kelamin        : {jenisKelamin}")
print(f"Usia                 : {umur} tahun")

rata_rata=(english+mtk+indonesia)/3
print("----------------------------------------------------------------------------")
if umur >= 25:
    print("Umur anda sudah tidak memenuhi syarat untuk mendaftar")
elif rata_rata >= 80 and jenisKelamin == "lakilaki":
    print("Anda disarankan untuk masuk Jurusan Teknik Informatika")
elif rata_rata >= 80 and jenisKelamin == "perempuan":
    print("Anda disarankan untuk masuk Jurusan Sistem Informasi")
else:
    print("Anda disarankan untuk masuk Jurusan DKV")
print("----------------------------------------------------------------------------")



















