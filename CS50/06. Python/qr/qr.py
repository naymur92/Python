
import os
import qrcode

# Generate a QR code
img = qrcode.make("https://bdprogrammers.com")

# Save as file
img.save("qr.png", "PNG")

# Open file
os.system("open qr.png")
