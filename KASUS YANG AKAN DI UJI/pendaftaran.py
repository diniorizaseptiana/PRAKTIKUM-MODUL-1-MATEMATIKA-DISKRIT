data_lengkap = True
biaya_lunas = True
peserta_terdaftar = True

hasil = data_lengkap and biaya_lunas and peserta_terdaftar

if hasil:
    print("PENDAFTARAN BERHASIL")
else:
    print("PENDAFTARAN GAGAL")
