import pyqrcode
import png
from PIL import Image

s = input('Insert the url: ')

# creating qr code
url = pyqrcode.create(s)

#saving image
img = "qr_code.png"
url.png(img, scale=100)