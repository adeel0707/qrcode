import qrcode

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="red", back_color="white")
    img.save(file_path)

if __name__ == "__main__":
    data = input("Enter the data to encode in the QR code: ")
    file_path = input("Enter the file path to save the QR code image: ")

    generate_qr_code(data, file_path)
    print("QR code generated successfully!")
