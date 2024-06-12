import pyautogui as auto   
import time
import os

auto.PAUSE = 0.5
#Abrir a tecla windows e chamar o powershell
auto.press('win')
auto.write('vs code')
auto.press('enter')
time.sleep(7)
#Abrir o terminal
auto.hotkey('crtl', 'shift', "'")
time.sleep(5)
#Inicio do commit
auto.write('git init')
auto.press('enter')
time.sleep(3)
auto.write('git add .')
auto.press('enter')
time.sleep(3)
auto.write('git branch -M main')
auto.press('enter')
time.sleep(3)
auto.write('git commit -m Rep atualizado por automação v2.')
auto.press('enter')
time.sleep(3)
auto.write('git remote add origin https://github.com/Marcos-mmvv/git_auto.git')
auto.press('enter')
time.sleep(2)
auto.write('git push')
auto.press('enter')







