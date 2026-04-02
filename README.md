# Tugas Kriptografi
* Nama: Joelianto Darmawan(Ketua)(20230410500025), Annisa Hardian Faradela (20230410500007), Adinda Puteri Aulia (2022D1E057)
* Kelas A

#  Steganografi Gambar Menggunakan Metode LSB

Proyek ini merupakan implementasi teknik steganografi digital menggunakan metode Least Significant Bit (LSB) untuk menyembunyikan sebuah data gambar rahasia ke dalam gambar lain (cover image) menggunakan bahasa pemrograman Python.

Teknik ini memungkinkan penyisipan data tanpa mengubah tampilan visual secara signifikan, sehingga keberadaan pesan sulit dideteksi oleh manusia.

##  Deskripsi Data yang Digunakan:

###  Data Penampung (wadah.png) ukuran gambar 736 x 1465 pixel, 1.1 MB

Gambar yang digunakan sebagai wadah adalah sebuah citra digital berformat **PNG** yang menampilkan beberapa kucing dengan latar belakang langit. Gambar ini memiliki karakteristik sebagai berikut:

* Memiliki resolusi tinggi sehingga mampu menampung data dalam jumlah besar
* Mengandung banyak variasi warna (warna alami kucing dan langit)
* Memiliki detail tekstur yang kompleks


###  Data yang Disembunyikan (data secret.png) ukuran gambar 694 x 825 pixel, 375,7 KB

Data yang disembunyikan berupa sebuah gambar yang berisi **tabel data mahasiswa** dengan informasi sebagai berikut:

* Nama Mahasiswa
* Nomor Induk Mahasiswa (NIM)
* Program Studi (Prodi)

Karakteristik data ini:

* Berbentuk citra (image-based data), bukan teks langsung
* Memiliki kontras tinggi (teks hitam di atas latar terang)
* Mengandung informasi penting yang bersifat struktural

##  Cara Kerja Sistem

###  Encoding (Menyembunyikan Gambar)

1. Membaca gambar penampung (`wadah.png`)
2. Membaca gambar rahasia (` data secret.png`)
3. Mengambil 4 bit paling signifikan dari gambar rahasia
4. Mengganti 4 bit terakhir pada gambar penampung
5. Menghasilkan gambar baru (`output secret.png`)

---

###  Decoding (Mengambil Gambar)

1. Membaca gambar hasil steganografi (`output secret.png`)
2. Mengambil 4 bit terakhir dari setiap pixel
3. Menggeser bit untuk membentuk kembali gambar
4. Menghasilkan gambar rahasia (`recovered secret.png`)

---

##  Struktur Folder

```
Steganografi/
│
├── wadah.png
├── data secret.png
├── output secret.png
├── recovered secret.png
├── encode.py
├── decode.py
├── README.md
```

---

##  Cara Menjalankan

### 1. Install Library

```bash
pip install pillow
```

### 2. Jalankan Encoding

```bash
python encode.py
```

### 3. Jalankan Decoding

```bash
python decode.py
```

##  Hasil

* **Gambar Wadah** → wadah.png
* **Gambar Rahasia** → data secret.png
* **Hasil Steganografi** → output secret.png
* **Hasil Decode** → recovered secret.png
