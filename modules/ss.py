import numpy as np
from PIL import ImageGrab
import cv2

def run(**args):
    # Capture the screen within the specified bounding box
    img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Save the screenshot to a file
    cv2.imwrite('screenshot1.jpg', img)
    f=open(img,'rb')
    f_str=base64.b64endcode(f.read())
    f.close()
    return f_str
