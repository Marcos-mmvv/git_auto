import pyautogui as auto   
import time
import os

auto.PAUSE = 0.5
#Abrir a tecla windows e chamar o powershell
auto.press('win')
auto.write('powershell')
auto.press('enter')
time.sleep(2)
#Entrar no diretorio do programa
auto.write('cd python')
auto.press('enter')
time.sleep(2)
auto.write('cd git_auto')
auto.press('enter')
auto.write('dir')
auto.press('enter')
#Inicio do commit
auto.write('pip freeze > requiriments.txt')
auto.press('enter')
time.sleep(2)
auto.write('git init')
auto.press('enter')
time.sleep(2)
auto.write('git add .')
auto.press('enter')
time.sleep(2)
auto.write('git commit -m "Repositório atualizado por automação."')
auto.press('enter')
time.sleep(3)
auto.write('git branch -M main')
auto.press('enter')
time.sleep(2)
auto.write('git remote add origin https://github.com/Marcos-mmvv/git_auto.git')
auto.press('enter')
time.sleep(2)
auto.write('git push -u origin main')
auto.press('enter')
time.sleep(3)
auto.write('git push -u origin main')
auto.press('enter')
time.sleep(3)
#auto.write('cxfreeze main.py -- target-dir pasta-gitauto')
#auto.press('enter')
#Inicio do Build
auto.write('cxfreeze main.py -- target-dir pasta-gitauto')
time.sleep(8)
auto.press('enter')
#auto.hotkey('alt', 'f4')



