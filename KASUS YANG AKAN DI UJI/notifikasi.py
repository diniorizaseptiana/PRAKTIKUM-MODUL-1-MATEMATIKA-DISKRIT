pesan_baru = False
email_baru = True
notifikasi_aplikasi = False

hasil = pesan_baru or email_baru or notifikasi_aplikasi

if hasil:
    print("ADA NOTIFIKASI BARU")
else:
    print("TIDAK ADA NOTIFIKASI")
