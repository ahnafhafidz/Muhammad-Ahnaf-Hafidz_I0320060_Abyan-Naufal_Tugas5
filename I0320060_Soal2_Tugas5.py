#Soal 2

#inputkan nama
nama = input("Silahkan Masukkan Nama Anda: ")

#inputkan nilai
nilai = int(input("Silahkan Masukkan Nilai Anda: "))

if nilai < 60:
    print("Halo", nama,"! Nilai anda setelah dikonversi adalah E")
elif nilai <= 64:
    print("Halo", nama,"! Nilai anda setelah dikonversi adalah C")
elif nilai <= 69:
    print("Halo", nama,"! Nilai anda setelah dikonversi adalah C+")
elif nilai <= 74:
    print("Halo", nama,"! Nilai anda setelah dikonversi adalah B")
elif nilai <= 79:
    print("Halo", nama,"! Nilai anda setelah dikonversi adalah B+")
elif nilai <= 84:
    print("Halo", nama,"! Nilai anda setelah dikonversi adalah A-")
elif nilai <= 100:
    print("Halo", nama,"! Nilai anda setelah dikonversi adalah A")
else:
    print("Tidak Valid")
