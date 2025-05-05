import base64
import win32api
import win32con
import win32gui
import win32ui
from PIL import Image


def get_dimensions():
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    return width, height, left, top


def screenshot(filename='screenshot.bmp'):
    hdesktop = win32gui.GetDesktopWindow()
    width, height, left, top = get_dimensions()

    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()

    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)

    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

    screenshot.SaveBitmapFile(mem_dc, filename)

    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())


def compress_image(input_filename, output_filename, target_size_kb=300):
    """ Compress the image to be under the target size (in KB). """
    img = Image.open(input_filename)
    quality = 95  # Start with a high quality

    while True:
        img.save(output_filename, format="JPEG", quality=quality)
        # Check the size of the file
        if os.path.getsize(output_filename) <= target_size_kb * 1024 or quality <= 10:
            break
        quality -= 5


def run():
    screenshot('screenshot.bmp')  # Capture the screenshot
    compress_image('screenshot.bmp', 'screenshot_compressed.jpg')  # Compress it to < 300KB
    with open('screenshot_compressed.jpg', 'rb') as f:
        img = f.read()
    return img


if __name__ == '__main__':
    run()
