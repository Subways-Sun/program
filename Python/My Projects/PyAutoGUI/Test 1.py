import pyautogui
pyautogui.PAUSE=0.5
pyautogui.hotkey('ctrl','space')
pyautogui.typewrite('wechat')
pyautogui.hotkey('enter')
pyautogui.hotkey('command','f')
pyautogui.typewrite('g')
pyautogui.hotkey('enter')
pyautogui.moveTo(728,694)
pyautogui.click()
for i in range(20):
    pyautogui.typewrite('{}'.format(i))
    pyautogui.hotkey('enter')
