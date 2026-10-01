hadir_online = True
hadir_offline = False

hasil = hadir_online ^ hadir_offline

if hasil:
    print("MODE KEHADIRAN VALID")
else:
    print("MODE KEHADIRAN TIDAK VALID")
