import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "Name:-Ansh Galani"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("MYQR.svg", scale = 8)