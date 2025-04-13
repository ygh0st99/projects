import pyautogui 
import time
"""
1- rodar o codigo
2- time.sleep
3-abrir whatsapp
4-buscar link
5-abrir link
6-preencher nome e desativar microfone
7-gravar a tela (win+alt+r)

time.sleep(600)
"""
""" time.sleep(10)
http://meet.google.com/fjd-wcwy-qby
 """

# Wait for 10 seconds to allow user to prepare
""" time.sleep(10) """

# Open WhatsApp (assuming it's pinned to the taskbar at position 1)
""" 
pyautogui.hotkey('win', '5')
time.sleep(5)

 """
# Search for the link in WhatsApp
""" 
pyautogui.hotkey('ctrl', 'f')
time.sleep(1)
pyautogui.typewrite('http://meet.google.com/fjd-wcwy-qby')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2) 

"""

# Open the link in the browser
time.sleep(5)
pyautogui.press('win')
time.sleep(1)
pyautogui.write('opera')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)

time.sleep(1)
pyautogui.typewrite('https://meet.google.com/fjd-wcwy-qby')
pyautogui.press('enter')
time.sleep(10)

pyautogui.click(x=682, y=712)
time.sleep(3)

pyautogui.click(x=1327, y=561)
time.sleep(3)

# Turn off the microphone
""" pyautogui.hotkey('ctrl', 'shift', 'm') """

""" pyautogui.press('enter') """
time.sleep(30)

# Start recording the screen (Windows shortcut: Win + Alt + R)
pyautogui.hotkey('win', 'alt', 'r')
time.sleep(1)