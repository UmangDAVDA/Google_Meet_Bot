from PIL import ImageGrab
import pytesseract
import winsound

from time import sleep
import pyautogui as auto
import schedule 
import webbrowser
import time

#Alert
pytesseract.pytesseract.tesseract_cmd = r"\tesseract.exe" #Set the path of Tesseract file location

#Time

link = "" #Add Google Meet Link

time = "" #Set Time in 24h format

def join():
     webbrowser.open_new_tab('https://' + link)
     sleep(7)
     auto.hotkey('ctrl', 'e')
     auto.hotkey('ctrl', 'd')
     auto.click(1332, 584)
     sleep(3)
     auto.hotkey('c')

schedule.every().day.at(time).do(join)
while True:
    schedule.run_pending()
    sleep(1)
    #Alert
    im =ImageGrab.grab(bbox=(370,712,1564,901)) 
    keyword =["attendance","UD","23"]
    text =pytesseract.image_to_string(im,lang='eng')
    print(text.split())
    for x in keyword:
        if x in text:#if((keyword[0] in text) or (keyword[1] in text) and (keyword[2] in text)):
          winsound.Beep(frequency=2500,duration=1000)
          print("Attendance Started")
        else:
          continue






