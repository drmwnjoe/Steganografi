# Steganografi
# 🔐 Steganografi Gambar Menggunakan Metode LSB (Python)

Proyek ini merupakan implementasi teknik steganografi digital menggunakan metode Least Significant Bit (LSB) untuk menyembunyikan sebuah gambar rahasia ke dalam gambar lain (cover image) menggunakan bahasa pemrograman Python.

Teknik ini memungkinkan penyisipan data tanpa mengubah tampilan visual secara signifikan, sehingga keberadaan pesan sulit dideteksi oleh manusia.

## 🎯 Tujuan

* Mengimplementasikan konsep steganografi pada citra digital
* Menyembunyikan gambar rahasia ke dalam gambar penampung
* Mengembalikan (decode) gambar rahasia dari hasil steganografi

## ⚙️ Cara Kerja Sistem

### 📥 Encoding (Menyembunyikan Gambar)

1. Membaca gambar penampung (`wadah.png`)
2. Membaca gambar rahasia (`secret.png`)
3. Mengambil 4 bit paling signifikan dari gambar rahasia
4. Mengganti 4 bit terakhir pada gambar penampung
5. Menghasilkan gambar baru (`output.png`)

---

### 📤 Decoding (Mengambil Gambar)

1. Membaca gambar hasil steganografi (`output.png`)
2. Mengambil 4 bit terakhir dari setiap pixel
3. Menggeser bit untuk membentuk kembali gambar
4. Menghasilkan gambar rahasia (`recovered.png`)

---

## 📂 Struktur Folder

```
steganografi-image-python/
│
├── wadah.png
├── secret.png
├── output.png
├── recovered.png
├── encode.py
├── decode.py
├── kompress.py
├── README.md
```

---

## ▶️ Cara Menjalankan

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

## 📸 Hasil

* **Gambar Wadah** → wadah.png
* **Gambar Rahasia** → secret.png
* **Hasil Steganografi** → output.png
* **Hasil Decode** → recovered.png

## 👨‍💻 Identitas

* Nama: Joelianto Darmawan(Ketua)(20230410500025), Annisa Hardian Faradela (20230410500007), Adinda Puteri Aulia (2022D1E057)
* Mata Kuliah: Kriptografi
