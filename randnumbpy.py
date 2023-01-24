import pyautogui as auto
import pyperclip as pc 
import time
import random as ran

open("C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2210.5.0_x64__8wekyb3d8bbwe\Notepad\Notepad.exe", 'r')


i=0 
while i<=380:
    i+=1
    if i%4==0 and i!=1:
        a=str(ran.randint(1,1000000001))
        pc.copy(a)
        auto.hotkey('alt' ,'tab')
        time.sleep(3)
        auto.hotkey('ctrl','v')
        time.sleep(3)
        auto.press('down')
        time.sleep(3)
        auto.hotkey('alt','tab')
        time.sleep(3)
    elif i%4==1 and i==1:
        a=str(ran.randint(1,1000000001)) + ","
        pc.copy(a)
        auto.hotkey('alt' ,'tab')
        time.sleep(3)
        auto.press('=')
        time.sleep(3)
        auto.hotkey('ctrl','v')
        time.sleep(3)
        auto.hotkey('alt','tab')
        time.sleep(3)
    else:
        a=str(ran.randint(1,10000000001)) + ","
        pc.copy(a) 
        time.sleep(3)
        auto.hotkey('alt','tab')
        time.sleep(3) 
        auto.hotkey('ctrl','v')
        time.sleep(3) 
        auto.hotkey('alt','tab') 
        time.sleep(3)
    
print("FINITO")