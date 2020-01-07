'''
Device: Grove Pyboard 
Summary: This code reads gesture values from Grove gesture sensor and 
sends corresponding numbers to LEGO SPIKE Prime

Attribution: https://github.com/itechnofrance (grove_GestureClass)

Tufts Center for Engineering Education and Outreach
Updated on: 01/07/2020
'''
import gc,utime
import pyb, micropython
import LPF2
import grove_GestureClass

micropython.alloc_emergency_exception_buf(200)

i2c = machine.I2C(scl=machine.Pin('Y9'), sda=machine.Pin('Y10')) #I2C
#Note: If i2c.scan() returns empty address, run the code again or reset the Grove pyboard
i2c.scan()

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
def detected_gesture(d):
    if d==1:
        print('Forward')
    elif d==2:
        print('Backward')
    elif d==3:
        print('Right')
    elif d==4:
        print('Left')
    elif d==5:
        print('Up')
    elif d==6:
        print('Down')
    elif d==7:
        print('Clockwise')
    elif d==8:
        print('Counterclockwise')
    elif d==9:
        print('Wave')
    else:
        print('No Gesture')

def gestureCall():
     g = grove_GestureClass.PAJ7620(i2c = i2c)
     geste = g.gesture()
     detected_gesture(geste)
     return geste

# Loop
while True:
     if not lpf2.connected:
          lpf2.sendTimer.callback(None)
          red_led.on()
          utime.sleep_ms(200)
          lpf2.initialize()
     else:
          red_led.off()
          #Read the value from sensor
          value=int(gestureCall())
          utime.sleep_ms(500)

          lpf2.load_payload('Int8',value)
          print(value)

          utime.sleep_ms(200)

