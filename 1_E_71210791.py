#1

awal = int(input("Masukkan awal deret: "))
akhir = int(input("Masukkan akhir deret: "))

for genap in range(awal,akhir):
    if genap%2 == 0 and genap%5 !=0 and genap%9 !=0:
        print (genap," ",end = "")