#2

#jadwal
senin = ["ke-1 Algoritma Graf","ke-3 Sistem Operasi","ke-4 PAK","ke-5 Praktikum INLAN"]
selasa = ["ke-2 Matematika Teknik","ke-4 Bhs Indo","ke-6 PKN"]
kamis = ["ke-1 IMK","ke-3 Logmat","ke-4 Prktekkom"]
jumat = ["ke-2 Sistem Basis Data","ke-4 Praktikum Sistem Basis Data","ke-6 INLAN"]

hari = input("Hi Tutu, Silahkan Masukkan hari yang ingin Anda telusuri: ")

if hari == "senin":
    for i in range(len(senin)):
        print("kelas",senin[i])
elif hari == "selasa":
     for i in range(len(selasa)):
         print("kelas",selasa[i])
elif hari == "kamis":
    for i in range(len(kamis)):
         print("kelas",kamis[i])
elif hari == "jumat":
    for i in range(len(jumat)):
        print("kelas",jumat[i])
elif hari == "rabu":
    print("Hari rabu Anda tidak ada kelas")
