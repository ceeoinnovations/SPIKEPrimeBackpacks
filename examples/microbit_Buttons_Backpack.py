'''
Device: Microbit Backpack
Summary: This code sends numbers 0, 1 or 2 to SPIKE Prime, 
depending on which button on the Microbit is pressed 
and also displays a Heart, Smiley or a Frowny icon 

Tufts Center for Engineering Education and Outreach
Updated on: 01/08/2020
'''
import utime
import gc
from microbit import *
import LPF2forMicrobit

lpf2 = LPF2forMicrobit.LPF2()
lpf2.initialize()

value = 0
while True:
  if not lpf2.connected:
    print('not connected')
    utime.sleep(1)
    lpf2.initialize()
  else:
    if microbit.button_a.is_pressed() and microbit.button_b.is_pressed():
        image=microbit.Image.HEART
        microbit.display.show(image)
        value=0
    elif microbit.button_a.is_pressed():
        image=microbit.Image.HAPPY
        microbit.display.show(image)
        value=1
    elif microbit.button_b.is_pressed():
        image=microbit.Image.SAD
        microbit.display.show(image)
        value=2
    lpf2.send_value(value)
    utime.sleep_ms(200)
