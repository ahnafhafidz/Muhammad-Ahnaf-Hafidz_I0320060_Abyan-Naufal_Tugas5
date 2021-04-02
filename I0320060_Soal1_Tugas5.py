#Soal 1
#inputkan nama
nama = input('Silahkan Masukkan Nama Anda: ')
#inputkan jenis kelamin
gender = input('Pilih Jenis Kelamin Anda (L/P): ')

if gender.upper() == "L":
    print("Selamat Datang, Tuan", nama,"!")
elif gender.upper() == "P":
    print("Selamat Datang, Nyonya", nama,"!")
else:
    print("Tidak Valid")