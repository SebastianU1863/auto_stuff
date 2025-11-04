#import pyautogui
#Switching to pynput cause its faster/cleaner
from pynput import mouse
import tkinter as tk
from tkinter import messagebox
import time
from tkinter import simpledialog

#pyautogui.PAUSE = 0.005
#The following values were tested at 5 seconds
#.1 gets cps 5
#.01 gets cps 45
#.005 gets cps 85
#.001 gets cps of ~120
#Dependding on your pc, I would not suggest lowering the pause time below 0.0001, especially if you have other processes running

mouse_ctrl = mouse.Controller()
delay = 0.01


def start_clicking(seconds: int):
    end_time = time.time() + seconds
    while (time.time()<end_time): 
        #print("loop executed")
        #pyautogui.leftClick()
        mouse_ctrl.click(mouse.Button.left)
        time.sleep(delay)
    print("While Loop Ended")
   

def start():
    root = tk.Tk()
    root.withdraw()
    number_of_seconds = tk.simpledialog.askinteger(title="Input", prompt="Please enter the number of seconds you want to click for")
    response = messagebox.askyesno("Confirm", "Start?")
    if response and number_of_seconds:
        print("Started Clicking. Number of seconds = " + str(number_of_seconds))
        start_clicking(int(number_of_seconds))
    else:
        pass

start()