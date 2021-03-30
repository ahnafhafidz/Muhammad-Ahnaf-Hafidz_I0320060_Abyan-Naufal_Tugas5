#Soal 1
#inputkan nama
nama = input('Silahkan Masukkan Nama Anda: ')
#inputkan jenis kelamin
gender = input('Silahkan Masukkan Jenis Kelamin Anda (L/P): ')

if gender == "L":
    print("Selamat Datang, Tuan", nama,"!")
elif gender == "P":
    print("Selamat Datang, Nyonya", nama,"!")
else:
    print()