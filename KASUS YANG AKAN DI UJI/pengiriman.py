pengiriman_reguler = True
pengiriman_express = False

hasil = pengiriman_reguler ^ pengiriman_express

if hasil:
    print("PILIHAN PENGIRIMAN VALID")
else:
    print("PILIHAN PENGIRIMAN TIDAK VALID")
