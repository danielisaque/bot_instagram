import openpyxl
import pyperclip
import pyautogui
from time import sleep

workbook = openpyxl.load_workbook("danielisaquee_followers_1-149.xlsx")
sheet_seguidores = workbook['sheet1']

pyautogui.click(1098,309)
sleep(0.3)

for linha in sheet_seguidores.iter_rows(min_row=2):
    pyperclip.copy(linha[1].value)
    sleep(0.3)
    pyautogui.hotkey('ctrl','v')
    sleep(0.3)
    pyautogui.hotkey('enter')
    sleep(0.3)
    




