
# import qrcode as qr

# img = qr.make("https://youtube.com/@aks042?si=2GR1v2SIT6L9Z6Xs")

# img.save("Welcom youtube.png")

import qrcode 
from PIL import Image
qr = qrcode.QRCode (version = 1,
                      error_correction = qrcode.constants.ERROR_CORRECT_H,
                      box_size=20,border=4,)
qr.add_data("https://youtube.com/@aks042?si=2GR1v2SIT6L9Z6Xs")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("Welcom youtube.png")
