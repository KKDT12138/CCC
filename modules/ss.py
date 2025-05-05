import numpy as np
from PIL import ImageGrab, Image
import cv2

def capture_screenshot(**args):
    # 捕获屏幕截图
    img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))  # bbox 定义左、上、右和下像素的4元组
    
    # 打印截图尺寸
    print(f"Screenshot size: {img.size[1]} x {img.size[0]}")
    
    # 转换为 NumPy 数组
    img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
    
    # 使用 OpenCV 转换颜色空间
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # 保存为文件
    file_path = 'screenshot1.jpg'
    cv2.imwrite(file_path, img)

    # 返回截图信息
    return {'type': 'screenshot', 'data': file_path}
