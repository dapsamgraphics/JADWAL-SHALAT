# Jadwal Shalat
Jadwal Shalat berdasarkan nama kota menggunakan API dari [MyQuran](https://myquran.com/) untuk mendapatkan jadwal shalat. 

1. **Mencari ID Kota**:
   - URL: `https://api.myquran.com/v2/sholat/kota/cari/{nama_kota}`
   - Metode: `GET`
   - Deskripsi: Mengambil ID kota berdasarkan nama kota yang dimasukkan.

2. **Mendapatkan Jadwal Sholat**:
   - URL: `https://api.myquran.com/v2/sholat/jadwal/{kota_id}/2024/10/01`
   - Metode: `GET`
   - Deskripsi: Mengambil jadwal sholat untuk kota yang ditentukan pada tanggal tertentu.

## Fitur
- Menampilkan Jadwal Shalat berdasarkan nama kota yang dimasukkan oleh pengguna. "nama kota bukan provinsi" bukan provinsi

# Cara menjalankan nya:
~ git clone https://github.com/dapsamgraphics/JADWAL-SHALAT/

~ cd JADWAL-SHALAT/

~ pip install -r requirements.txt

~ py shalat.py

