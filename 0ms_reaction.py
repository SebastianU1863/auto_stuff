# #from PIL import ImageGrab, Image
# import pyautogui
# import time
# from pynput import mouse
# import mss

# pyautogui.PAUSE = 0
# pyautogui.MINIMUM_DURATION = 0

# def on_click(x,y,button, pressed):
#     stop = False
#     if pressed and button == mouse.Button.left:
#         sct = mss.mss()
#         print("Left Clicked")
#         end_time = time.time()+10
#         mouseX, mouseY = pyautogui.position()
#         while(time.time()<end_time):

#             #This old code used pillow and only got 500 ms. By switching to mss, I was able to lower the ms
#             # screenshot = ImageGrab.grab(bbox=(mouseX,mouseY,mouseX+2,mouseY+2))
#             # screenshot.save('letter.png')
#             # image = Image.open("letter.png")
#             # pixel_color = image.getpixel((1, 1))
#             pixel_color = sct.grab({"top": mouseY, "left": mouseX, "width": 1, "height": 1}).pixel(0,0)
#             if(pixel_color == (75, 219, 106)):
#                 pyautogui.leftClick()
#                 end_time = time.time()
#             time.sleep(0.1)
#         return False
#     elif pressed and button == mouse.Button.right:
#         print("Stopped (Hopefully)")
#         stop = True
#         return False
#     return False
      

# def start():
#     print("Program Started")
#     with mouse.Listener(on_click=on_click) as listener:
#             listener.join()
#     print("Program Ended")

# start()


import time
import mss
#Using pynput instead of pyautogui cause its faster (according to google search)
from pynput import mouse

human_benchmark_green = (75, 219, 106)
delay = 0.005  # 5ms delay so we don't crash
is_running = False #flag for in-between clicks
end_now = False #flag to kill while true loop
mouse_ctrl = mouse.Controller()
sct = mss.mss()

#Changed to a flag-based system cause the while loops relying on time wasn't great
def on_click(x, y, button, pressed):
    global is_running
    global end_now
    if pressed and button == mouse.Button.left:
        is_running = True
        print("Running")
    elif pressed and button == mouse.Button.right:
        is_running = False
        end_now = True
        print("Stopped")

def get_pixel(x, y):
    img = sct.grab({"top": y, "left": x, "width": 1, "height": 1})
    return img.pixel(0, 0)

def start():
    print("Started")
    global is_running
    global end_now
    with mouse.Listener(on_click=on_click):
        while True:
            if is_running:
                x, y = mouse_ctrl.position
                if get_pixel(x, y) == human_benchmark_green:
                    mouse_ctrl.click(mouse.Button.left)
                    print("Clicked")
                    is_running = False
            elif end_now:
                break
            time.sleep(delay)

start()

