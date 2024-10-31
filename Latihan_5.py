
# (222443015) M Dandi Al Idrus 2AEC

login = input("Masukan Password :")
nasi = 15000
mie = 13000
ayam = 20000
nama = "M Dandi Al Idrus";d

while login =="":
    print("Anda tidak memasukkan login kamu")
    login = input("Masukan Password :")

print("Anda Berhasil Login sebagai",nama)
print('=' * 25)
print('Menu Pilihan')
print('  1. Nasi Goreng \t : Rp', nasi)
print('  2. Mie Goreng \t : Rp', mie)
print('  3. Ayam Goreng \t : Rp', ayam)
print('=' * 25)

pilihan = input("Masukan Menu Pilihan :")
uang = int(input("Masukan uang yang akan dibayar :"))

if pilihan == '1':
  hasil = uang - nasi
  print("Kembaliannya anda adalah :",hasil)
elif pilihan == '2':
  hasil = uang - mie
  print("Kembaliannya anda adalah :",hasil)
elif pilihan == '3':
  hasil = uang - ayam
  print("Kembaliannya anda adalah :",hasil)
else:
  print('Tidak valid')


