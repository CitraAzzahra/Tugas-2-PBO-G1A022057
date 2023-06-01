class Mahasiswa:
    def _init_(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def tampilkan_info(self):
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("Jurusan: ", self.jurusan.NamaJurusan)


class Jurusan:
    def _init_(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []
    
    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)
    
    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            mahasiswa.tampilkan_info()


class Universitas:
    def _init_(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []
    
    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)
    
    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)


# Membuat objek Universitas "XYZ University"
xyz_university = Universitas("XYZ University")

# Membuat objek Jurusan "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ
teknik_informatika = Jurusan("Teknik Informatika")
xyz_university.tambah_jurusan(teknik_informatika)

# Membuat objek Mahasiswa "Kalian masing" dan memasukkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa_1 = Mahasiswa("Kalian masing", "NIM Kalian masing", teknik_informatika)
teknik_informatika.tambah_mahasiswa(mahasiswa_1)

# Menampilkan daftar jurusan yang ada di Universitas XYZ
xyz_university.tampilkan_daftar_jurusan()

# Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
teknik_informatika.tampilkan_daftar_mahasiswa()
