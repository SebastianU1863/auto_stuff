import pyautogui
import tkinter as tk
from tkinter import messagebox
import time
from tkinter import simpledialog
from pynput import mouse
from pynput.mouse import Listener

clicked_positions = []
click_count = 0
#31, not 30 for hbenchmark
number_of_targets = 0

def start_clicking(targets):
    path = r'C:\Users\SHU\.vscode\auto_stuff\target.png'
    global clicked_positions
    aiming_region = []
    for coordinate in clicked_positions:
        for value in coordinate:
            aiming_region.append(value)

    for i in range(targets):
        #for future  me, this can go faster if you use other imports like mss to find targets rather than pyautogui
        #current speed is about 300-500 avg ms right now
        #maybe take the screenshot
        target_location = pyautogui.locateOnScreen(path, grayscale=True, region=aiming_region)
        pyautogui.leftClick(target_location)
    print("Done")



def calibrate():  
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

#copy-pasted from wordlebot, so there are definitely ways to make this cleaner
def on_click(x, y, button, pressed):
    global click_count
    global clicked_positions
    if pressed and button == mouse.Button.left:
        click_count += 1
        clicked_positions.append((x, y))
        if click_count >= 2:
            return False

def start():
    root = tk.Tk()
    root.withdraw()
    global number_of_targets
    number_of_targets = tk.simpledialog.askinteger(title="Input", prompt="Please enter the number of targets you want to click")
    response = messagebox.askyesno("Confirm", "Start?")
    if response and number_of_targets:
        print("Started Clicking. Number of Targets = " + str(number_of_targets))
        start_clicking(int(number_of_targets))
    else:
        pass

def open_calibration_prompt():
    root = tk.Tk()
    root.withdraw()
    response = messagebox.askyesno("Calibration", "Please calibrate the positioning. \n 1. Click the top left corner of the top left box. \n 2. Click the top left corner of the bottom right box.")
    if response:
        calibrate()
    else:
        print("Stopped Calibration")

open_calibration_prompt()
print("Calibration Done")
start_time = time.time()
start()
total_time = time.time()-start_time
print("Total time = " + str(total_time))
print("Avg Time = " + str(total_time/number_of_targets))


