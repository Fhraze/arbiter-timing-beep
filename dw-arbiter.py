from keyboard import is_pressed
from playsound import playsound
from time import sleep

while True:
    if is_pressed('F'):
        print("1")
        playsound('blipSelect.wav')
        sleep(0.028)
        print("2")
        playsound('blipSelect.wav')
        sleep(0.028)
        print("3")
        playsound('blipSelect.wav')
        sleep(0.028)
        print("BOOM!")
        playsound('blipNow.wav')
        print("\nSleeping for 5 seconds...")
        sleep(5)
        print("<Ready>")
    sleep(0.0005)
