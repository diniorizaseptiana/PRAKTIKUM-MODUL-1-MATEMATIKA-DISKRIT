# TABEL PENGUJIAN

Tabel pengujian digunakan untuk menguji setiap studi kasus dengan beberapa kombinasi kondisi `True` dan `False`.

## 1. Pendaftaran Kegiatan - AND

| Data Lengkap | Biaya Lunas | Peserta Terdaftar | Hasil |
|---|---|---|---|
| True | True | True | PENDAFTARAN BERHASIL |
| False | True | True | PENDAFTARAN GAGAL |
| True | False | True | PENDAFTARAN GAGAL |
| True | True | False | PENDAFTARAN GAGAL |
| False | False | False | PENDAFTARAN GAGAL |

## 2. Validasi Absensi - AND

| Terdaftar | Hadir | Kartu Aktif | Hasil |
|---|---|---|---|
| True | True | True | ABSENSI BERHASIL |
| False | True | True | ABSENSI GAGAL |
| True | False | True | ABSENSI GAGAL |
| True | True | False | ABSENSI GAGAL |
| False | False | False | ABSENSI GAGAL |

## 3. Notifikasi Pengguna - OR

| Pesan Baru | Email Baru | Notifikasi Aplikasi | Hasil |
|---|---|---|---|
| False | False | False | TIDAK ADA NOTIFIKASI |
| True | False | False | ADA NOTIFIKASI BARU |
| False | True | False | ADA NOTIFIKASI BARU |
| False | False | True | ADA NOTIFIKASI BARU |
| True | True | False | ADA NOTIFIKASI BARU |

## 4. Pilihan Transportasi - OR

| Bus | Kereta | Ojek | Hasil |
|---|---|---|---|
| False | False | False | TRANSPORTASI TIDAK TERSEDIA |
| True | False | False | TRANSPORTASI TERSEDIA |
| False | True | False | TRANSPORTASI TERSEDIA |
| False | False | True | TRANSPORTASI TERSEDIA |
| True | True | False | TRANSPORTASI TERSEDIA |

## 5. Media Penyimpanan - OR

| Google Drive | Flashdisk | Harddisk | Hasil |
|---|---|---|---|
| False | False | False | MEDIA PENYIMPANAN TIDAK TERSEDIA |
| True | False | False | MEDIA PENYIMPANAN TERSEDIA |
| False | True | False | MEDIA PENYIMPANAN TERSEDIA |
| False | False | True | MEDIA PENYIMPANAN TERSEDIA |
| True | True | False | MEDIA PENYIMPANAN TERSEDIA |

## 6. Jenis Pengiriman - XOR

| Pengiriman Reguler | Pengiriman Express | Hasil |
|---|---|---|
| False | False | PILIHAN PENGIRIMAN TIDAK VALID |
| True | False | PILIHAN PENGIRIMAN VALID |
| False | True | PILIHAN PENGIRIMAN VALID |
| True | True | PILIHAN PENGIRIMAN TIDAK VALID |

## 7. Mode Kehadiran - XOR

| Hadir Online | Hadir Offline | Hasil |
|---|---|---|
| False | False | MODE KEHADIRAN TIDAK VALID |
| True | False | MODE KEHADIRAN VALID |
| False | True | MODE KEHADIRAN VALID |
| True | True | MODE KEHADIRAN TIDAK VALID |

## 8. Jenis Keanggotaan - XOR

| Anggota Reguler | Anggota Premium | Hasil |
|---|---|---|
| False | False | KEANGGOTAAN TIDAK VALID |
| True | False | KEANGGOTAAN VALID |
| False | True | KEANGGOTAAN VALID |
| True | True | KEANGGOTAAN TIDAK VALID |
