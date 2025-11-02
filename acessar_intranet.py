import pyautogui
import os, time

pyautogui.PAUSE = 2 
USER = os.getenv("INTRA_USER")
PASS = os.getenv("INTRA_PASS")
link = ("https://www.intranetmall.com/boulevardshoppingvilavelha4/")



pyautogui.press ('win')
pyautogui.write ('chorme')
pyautogui.press ('enter')
pyautogui.write (link)
pyautogui.press ('enter')
pyautogui.press ('enter')

pyautogui.click()

print("Script realizado com sucesso")