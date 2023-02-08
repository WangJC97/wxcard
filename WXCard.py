import pyautogui
import time

x = 1
pyautogui.alert('确认【推送】按钮，5秒后获取鼠标位置')
time.sleep(5)
px,py = pyautogui.position()
pyautogui.alert('【推送】位置获取完成')
pyautogui.alert('确认【结束推送】按钮，5秒后获取鼠标位置')
time.sleep(5)
sx,sy = pyautogui.position()
pyautogui.alert('【结束推送】位置获取完成')
time.sleep(1)
for x in range(0,1000):
    pyautogui.moveTo(px,py)
    pyautogui.click()
    time.sleep(30)
    pyautogui.moveTo(sx,sy)
    pyautogui.click()
    time.sleep(3)
    x += 1
