import pyautogui
import time
import keyboard

keyboard.wait('.')
px,py = pyautogui.position()
pyautogui.alert('推送位置获取完成')
keyboard.wait('.')
sx,sy = pyautogui.position()
pyautogui.alert('结束推送位置获取完成')
time.sleep(1)

while 1:
    pyautogui.moveTo(px,py)
    pyautogui.click()
    time.sleep(30)
    pyautogui.moveTo(sx,sy)
    pyautogui.click()
    time.sleep(3)