Uang_semula =int(input("Masukan uang anda :"))
pengeluaran=int(input("Masukan total belanja : "))

if pengeluaran >60000:
    pengeluaran -= 10000

total= pengeluaran
kembalian=Uang_semula-pengeluaran


print ("Total uang yang harus di bayar Rp.%i dan kembaliannya Rp.%i"%(total,kembalian))