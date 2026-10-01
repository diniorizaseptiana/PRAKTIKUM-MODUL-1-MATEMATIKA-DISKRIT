anggota_reguler = True
anggota_premium = False

hasil = anggota_reguler ^ anggota_premium

if hasil:
    print("KEANGGOTAAN VALID")
else:
    print("KEANGGOTAAN TIDAK VALID")
