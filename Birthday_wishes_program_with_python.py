import pyautogui
import pywhatkit
pywhatkit.sendwhatmsg('WhatsApp no of birthday Boy/Girl','  ',00,00)
import time
import random
time.sleep(5)

count=0
co="Happy Birthday Rohit Our Three Idiot 'Farhan' 😊 , May life lead you to great happiness ,success in your life,Good Health and hope that all your wishes come true!"
  
pyautogui.typewrite(f" {count}."+co)
pyautogui.press("enter")
count=count+1
while count<=2000:
    time.sleep(0.001)
    rno=random.randint(1,1)
    if rno==1:
        cop='Happy birthday! I hope all your birthday wishes and dreams come true. '
    elif rno==2:
        cop='Another adventure filled year awaits you. Welcome it by celebrating your birthday with pomp and splendor. Wishing you a very happy and fun-filled birthday!  '
    elif rno==3:
        cop=' May the joy that you have spread in the past come back to you on this day. Wishing you a very happy birthday!'
    elif rno==4:
        cop="May you be gifted with life’s biggest joys and never-ending bliss. After all, you yourself are a gift to earth, so you deserve the best. Happy birthday.  "
    else:
        cop='  '
    pyautogui.typewrite(f" {count}."+cop)
    pyautogui.press("enter")
    count=count+1
