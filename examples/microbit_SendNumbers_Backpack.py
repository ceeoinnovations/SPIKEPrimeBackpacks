'''
Device: Microbit Backpack
Summary: This code sends numbers 0 through 9 from Microbit Backpack to LEGO SPIKE Prime

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
    if value<9:
      value=value+1
    else: 
      value=0
    lpf2.send_value(value)
    utime.sleep_ms(200)
