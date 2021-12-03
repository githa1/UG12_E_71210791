
angka1 = [3, 20, 100, -35, 50]
print (angka1)

max1 = angka1[0]
min1 = angka1[0]

for i in range(0, len(angka1)):
    max1 = max(max1,angka1[i])
    min1 = min(min1,angka1[i])

print("Nilai terbesar: ",max1)
print("Nilai terkecil: ",min1)

print("")

angka2 = [3, 20, 90, 35, 75]
print(angka2)

max2 = angka2[0]
min2 = angka2[0]

for i in range(0, len(angka2)):
    max2 = max(max2,angka2[i])
    min2 = min(min2,angka2[i])

print("Nilai terbesar: ",max2)
print("Nilai terkecil: ",min2)
