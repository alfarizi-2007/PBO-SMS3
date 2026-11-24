class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nama, nim): 
        self.nama = nama
        self.nim = nim



mhs = Mahasiswa("Alfa","14022500076")
print(mhs.nama)
print(mhs.nim)