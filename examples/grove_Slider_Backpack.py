'''
Device: Grove Pyboard 
Summary: This code reads the slider potentiometer value from Grove Slider and 
sends the corresponding values to LEGO SPIKE Prime

Attribures: http://wiki.seeedstudio.com/Grove-Rotary_Angle_Sensor/

Tufts Center for Engineering Education and Outreach
Updated on: 01/07/2020
'''
import gc,utime
import pyb, micropython
import LPF2

micropython.alloc_emergency_exception_buf(200)

modes = [
LPF2.mode('int8',type = LPF2.DATA8),
LPF2.mode('int16', type = LPF2.DATA16),
LPF2.mode('int32', type = LPF2.DATA32),
LPF2.mode('float', format = '2.1', type = LPF2.DATAF),
LPF2.mode('int8_array',size = 4, type = LPF2.DATA8),
LPF2.mode('int16_array',size = 4, type = LPF2.DATA16),
LPF2.mode('int32_array',size = 4, type = LPF2.DATA32),
LPF2.mode('float_array',size = 4, format = '2.1', type = LPF2.DATAF)
]

red_led=pyb.LED(1)
green_led = pyb.LED(2)
red_led.on()

#lpf2 = LPF2.LPF2(1, 'P1', 'P0', modes, LPF2.SPIKE_Ultrasonic, timer = 4, freq = 5)    # OpenMV
#lpf2 = LPF2.LPF2(3, 'P4', 'P5', modes, LPF2.SPIKE_Ultrasonic, timer = 4, freq = 5)    # OpenMV
lpf2 = LPF2.Prime_LPF2(1, 'Y1', 'Y2', modes, LPF2.SPIKE_Ultrasonic, timer = 4, freq = 5)    # Grove PyBoard
# use EV3_LPF2 or Prime_LPF2 - also make sure to select the port type on the EV3 to be ev3-uart

lpf2.initialize()

value = 0

'''
http://wiki.seeedstudio.com/Grove-Slide_Potentiometer/
connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal -  pin X1
'''

from pyb import ADC

class GroveSlider(object):
    def __init__(self, pin):
         self.adc = ADC(pin)

    def value(self):
        return self.adc.read()

pot = GroveSlider('X1')

# Loop
while True:
     if not lpf2.connected:
          lpf2.sendTimer.callback(None)
          red_led.on()
          utime.sleep_ms(200)
          lpf2.initialize()
     else:
          red_led.off()
          value=pot.value()
          #Raw value
          print(value)
          
          lpf2.load_payload('Int16',value)
          
          utime.sleep_ms(200)

