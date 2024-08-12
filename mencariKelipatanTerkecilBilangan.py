# Input bilangan
angka1 = int(input("Masukkan bilangan pertama: "))
angka2 = int(input("Masukkan bilangan kedua: "))

# Mencari angka terbesar
if angka1 > angka2:
    terbesar = angka1
else:
    terbesar = angka2

# Mencari KPK
for i in range(terbesar, (angka1 * angka2) + 1):
    if i % angka1 == 0 and i % angka2 == 0:
        kpk = i
        break

# hasil KPK
print(f"KPK dari {angka1} dan {angka2} adalah {kpk}")