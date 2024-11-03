import time
import keyboard
import pyautogui
import keyboard
import os
f = open("cropper.txt")
print(f.read())
f.close()
print("Swap to the game now\nPress 0 to end the script")
time.sleep(4)
start = time.time()
#1701 353
def func():
    pyautogui.press("r")#Hoe hotkey
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.press("3")#Bonemeal hotkey
    for x in range(0,3):
        pyautogui.click(button='right')
        time.sleep(0.2)
    stop()
end = 0
def stop():
    global end
    end = time.time()
    keyboard.add_hotkey('0', lambda: os._exit(0))
def sell():
    if img[1701, 353] == (255,84,84):
        pyautogui.press("/")
        pyautogui.typewrite("/sell a\n", interval = 0.5)
        print("Inventory Sold!")
    else:
        pass
while True:
    func()

        
        


    
