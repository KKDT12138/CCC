import numpy as np
from PIL import ImageGrab, Image
import cv2
 
img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))  # bbox 定义左、上、右和下像素的4元组
print(img.size[1], img.size[0])
img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
print(img)
img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR) # 看评论区有C友说颜色相反，于是加了这一条
cv2.imwrite('screenshot1.jpg', img)
# img = Image.fromarray(img)
# img.save('screenshot1.jpg')
