import qrcode

url = "https://yourwebsite.com"

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 = smallest, 40 = largest)
    box_size=10,  # Size of each box in the QR Code grid
    border=5,  # Border thickness
)

qr.add_data(url)
qr.make(fit=True)

# Generate the QR Code image
img = qr.make_image(fill="black", back_color="white")

# Save the QR Code as an image file
img.save("my_qr_code.png")

print("QR code generated successfully! Check 'my_qr_code.png'.")
