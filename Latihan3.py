# input nilai variable
a=input("masukan nilai a:")
b=input("masukan nilai b:")

# cetak nilai variabel
print("Variabel a=",a)
print("Variabel a=",b)

# cetak hasil operasi kedua variabel dengan String Format
print("Hasil penggabungan {1}&{0}=%s".format(a,b) %(a+b))

# konversi nilai variabel
a=int(a)
b=int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b) %(a+b))
