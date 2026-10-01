google_drive = False
flashdisk = True
harddisk = False

hasil = google_drive or flashdisk or harddisk

if hasil:
    print("MEDIA PENYIMPANAN TERSEDIA")
else:
    print("MEDIA PENYIMPANAN TIDAK TERSEDIA")
