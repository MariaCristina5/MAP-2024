import pyautogui
import time
import keyboard

def ss ():
    captura_de_ecran = pyautogui.screenshot()
    captura_de_ecran.save('captura.png')

def cautare_google():
    if(pyautogui.locateOnScreen(r"search_bar.png")!=None):
        camp_google = pyautogui.locateOnScreen(r"search_bar.png")
        pyautogui.click(camp_google)
        time.sleep(3)
        pyautogui.write('https://www.youtube.com/@DacianMalitaFilm')
        pyautogui.press('enter')
        time.sleep(2)
        click_video()

def click_video():
    pyautogui.click(1794, 545)
    time.sleep(1)
    pyautogui.scroll(-100)

def afisare_coordonate():
    while not keyboard.is_pressed('z'):
        print(pyautogui.position() )
        time.sleep(0.1)


#afisare_coordonate()      
cautare_google()