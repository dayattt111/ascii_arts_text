# ASCII Art Generator

Program Python untuk menghasilkan ASCII art dari teks dengan berbagai pilihan font.

## 📋 Daftar Isi

- [Deskripsi](#deskripsi)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi](#instalasi)
- [Cara Penggunaan](#cara-penggunaan)
- [Contoh](#contoh)
- [Fitur](#fitur)
- [Struktur Proyek](#struktur-proyek)

---

## Deskripsi

ASCII Art Generator adalah aplikasi command-line yang memungkinkan pengguna untuk:
- Mengubah teks biasa menjadi ASCII art yang menarik
- Memilih berbagai jenis font untuk tampilan yang berbeda-beda
- Menyalin hasil ASCII art langsung ke clipboard

Program ini memanfaatkan library `pyfiglet` untuk menghasilkan ASCII art berkualitas tinggi dan `tkinter` untuk mengelola clipboard.

---

## Persyaratan Sistem

- Python 3.6 atau lebih tinggi
- Sistem operasi: Windows, macOS, atau Linux

---

## Instalasi

### 1. Clone atau download proyek

```bash
git clone <repository-url>
cd asscii_project
```

### 2. Install dependensi

```bash
pip install pyfiglet
```

**Catatan:** `tkinter` biasanya sudah termasuk dalam instalasi Python standar.

---

## Cara Penggunaan

Program dijalankan melalui command-line dengan sintaks berikut:

```bash
python main.py -t "TEKS" [OPTIONS]
```

### Parameter

| Parameter | Singkat | Tipe | Deskripsi |
|-----------|---------|------|-----------|
| `--text` | `-t` | string (wajib) | Teks yang ingin diubah menjadi ASCII art |
| `--font` | `-f` | string (opsional) | Jenis font FIGlet yang digunakan (default: `standard`) |
| `--copy` | - | flag (opsional) | Salin hasil ASCII art ke clipboard |

---

## Contoh

### Contoh 1: ASCII Art Dasar
```bash
python main.py -t "HELLO"
```

Output:
```
  _   _  _____ _     _     ___  
 | | | ||  ___| |   | |   / _ \ 
 | |_| || |_  | |   | |  | | | |
 |  _  ||  _| | |   | |  | | | |
 | | | || |   | |__ | |__| |_| |
 |_| |_||_|   |____||_____\___/ 
```

### Contoh 2: ASCII Art dengan Font Berbeda
```bash
python main.py -t "PYTHON" --font "banner"
```

### Contoh 3: ASCII Art dan Salin ke Clipboard
```bash
python main.py -t "PYTHON" --copy
```

Hasil ASCII art akan ditampilkan di terminal dan disalin ke clipboard secara otomatis.

---

## Fitur

### ✅ Fitur Utama

1. **Konversi Teks ke ASCII Art**
   - Mengubah teks apa saja menjadi ASCII art yang indah dan terstruktur

2. **Pilihan Font Beragam**
   - Mendukung semua font yang tersedia di FIGlet
   - Default menggunakan font `standard` jika tidak dispesifikasi

3. **Salin ke Clipboard**
   - Fitur otomatis untuk menyalin hasil langsung ke clipboard Windows
   - Memudahkan pengguna untuk paste ke aplikasi lain

4. **Command-Line Interface**
   - Interface yang sederhana dan mudah digunakan
   - Support untuk berbagai kombinasi parameter

---

## Struktur Proyek

```
asscii_project/
├── main.py          # File utama program
├── README.md        # Dokumentasi ini
└── requirements.txt # (opsional) File daftar dependensi
```

### Penjelasan File

- **main.py**: File utama yang berisi:
  - `copy_to_clipboard()`: Fungsi untuk menyalin teks ke clipboard
  - `ascii_art()`: Fungsi untuk menghasilkan ASCII art
  - `main()`: Fungsi utama yang mengelola argument parsing dan eksekusi program

---

## Fungsi-Fungsi

### `copy_to_clipboard(text: str)`
Menyalin teks ke clipboard sistem.

**Parameter:**
- `text` (str): Teks yang akan disalin

**Contoh:**
```python
copy_to_clipboard("ASCII Art di sini")
```

### `ascii_art(text: str, font: str = "standard")`
Menghasilkan ASCII art dari teks dengan font tertentu.

**Parameter:**
- `text` (str): Teks yang akan diubah
- `font` (str): Jenis font FIGlet (default: `"standard"`)

**Return:**
- (str): ASCII art dalam bentuk string

**Contoh:**
```python
result = ascii_art("PYTHON", "banner")
print(result)
```

---

## Daftar Font FIGlet

Beberapa font populer yang dapat digunakan:
- `standard` (default)
- `banner`
- `big`
- `block`
- `bubble`
- `digital`
- `ivrit`
- `lean`
- `mini`
- `script`
- `shadow`
- `slant`
- `small`
- `smscript`
- `smshadow`
- `smslant`
- `speed`

**Catatan:** Untuk melihat semua font yang tersedia, jalankan:
```bash
python -c "from pyfiglet import FigletFont; print(FigletFont.getFonts())"
```

---

## Tips & Trik

1. **Font Besar untuk Judul**
   ```bash
   python main.py -t "PYTHON" --font "banner"
   ```

2. **Teks Pendek untuk Hasil Optimal**
   - Gunakan teks yang tidak terlalu panjang untuk hasil visual yang lebih baik

3. **Kombinasi dengan Tools Lain**
   - Hasil dapat dipipe ke file: `python main.py -t "TEXT" > output.txt`

---

## Troubleshooting

### Error: `ModuleNotFoundError: No module named 'pyfiglet'`
**Solusi:** Install pyfiglet dengan perintah:
```bash
pip install pyfiglet
```

### Error: `ModuleNotFoundError: No module named 'tkinter'`
**Solusi:** 
- **Windows**: Tkinter biasanya sudah termasuk. Reinstall Python dan pastikan tkinter terceklist.
- **Linux**: Install dengan `sudo apt-get install python3-tk`
- **macOS**: Biasanya sudah termasuk. Jika tidak, install dengan Homebrew.

### Clipboard Tidak Bekerja di Linux
**Solusi:** Install `xclip`:
```bash
sudo apt-get install xclip
```

---

## Lisensi

[Tambahkan lisensi di sini jika diperlukan]

---

## Kontribusi

Kontribusi sangat diterima! Silakan:
1. Fork repository
2. Buat branch fitur baru
3. Commit perubahan
4. Push ke branch
5. Buat Pull Request

---

## Kontak

[Tambahkan informasi kontak di sini jika diperlukan]

---

**Terakhir diupdate:** November 2025
