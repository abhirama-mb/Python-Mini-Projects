import qrcode

data = input("Enter the URL : ").strip()
filename = input("Enter the filename : ").strip()

qr = qrcode.QRCode(box_size=10, border= 4)
qr.add_data(data)
image = qr.make_image()

image.save(filename)
print(f"QR Code Saved in {filename}")
