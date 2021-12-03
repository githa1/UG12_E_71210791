#3

angka = int(input("Masukkan Angka: "))

for i in range(angka):
    print(" "*(angka-i)+" *"*(i+1))

for j in range(angka-1):
    print(" "*(j+2)+" *"*(angka-1-j))