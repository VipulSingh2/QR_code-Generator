import segno

# Input text/URL
data = input("Enter the text/URL you want to convert to a QR code: ")

# Parameters for the QR code
scale = 10  # You can change the scale if needed
border = 4  # You can change the border size if needed
color = "#000000"  # You can change the color if needed

# Generate QR code
qrcode = segno.make(data)

# Save QR code to a file
qrcode.save("qrcode.png", kind='png', scale=scale, border=border, dark=color)

print("QR code saved as qrcode.png")
