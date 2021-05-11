import pyautogui, time  
#(x=549, y=697)
time.sleep(4)
pyautogui.click(549,697)

r = open('rambo.txt','r')


for letra in r:
    
    pyautogui.typewrite(letra)
    pyautogui.typewrite(["enter"])
