#Step 1: install all the libraries needed 
#Step 2: create a function that collects the text and converts it to a qr code
#Step 3: Save the QR code as an image
#Step 4: run the function

import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

url = input("Please enter your URL:")
generate_qrcode(url)
