# Jadwal Shalat
Jadwal Shalat berdasarkan nama kota menggunakan API dari [MyQuran](https://myquran.com/) untuk mendapatkan jadwal shalat.
Terdapat 907 Kota/Kabupaten https://api.myquran.com/v2/sholat/kota/semua

1. **Mencari ID Kota**:
   - URL: `https://api.myquran.com/v2/sholat/kota/cari/{nama_kota}`
   - Metode: `GET`
   - Deskripsi: Mengambil ID kota berdasarkan nama kota/kabupaten yang dimasukkan.

2. **Mendapatkan Jadwal Shalat**:
   - URL: `https://api.myquran.com/v2/sholat/jadwal/{kota_id}/2024/10/01`
   - Metode: `GET`
   - Deskripsi: Mengambil jadwal sholat untuk kota/kabupaten yang ditentukan pada tanggal tertentu.

## Fitur
- Menampilkan Jadwal Shalat berdasarkan nama kota/kabupaten yang dimasukkan oleh pengguna.

# Cara menjalankan nya:
~ git clone https://github.com/dapsamgraphics/JADWAL-SHALAT/

~ cd JADWAL-SHALAT

~ pip install -r requirements.txt

~ py shalat.py

