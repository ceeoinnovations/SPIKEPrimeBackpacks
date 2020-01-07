'''
Device: OpenMV 
Summary: This code reads QR codes using OpenMV camera, and 
sends the corresponding values to the SPIKE Prime 
Attribution: OpenMV example codes

Tufts Center for Engineering Education and Outreach
Updated on: 01/06/2020
'''
import gc,utime
import pyb, micropython
import LPF2
import sensor, image, time

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
lpf2 = LPF2.LPF2(3, 'P4', 'P5', modes, LPF2.SPIKE_Ultrasonic, timer = 4, freq = 5)    # OpenMV
#lpf2 = LPF2.Prime_LPF2(1, 'Y1', 'Y2', modes, LPF2.SPIKE_Ultrasonic, timer = 4, freq = 5)    # PyBoard
# use EV3_LPF2 or Prime_LPF2 - also make sure to select the port type on the EV3 to be ev3-uart

lpf2.initialize()

value = 0

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must turn this off to prevent image washout...
clock = time.clock()

# Loop
while True:
     if not lpf2.connected:
          lpf2.sendTimer.callback(None)
          red_led.on()
          utime.sleep_ms(200)
          lpf2.initialize()
     else:
          red_led.off()
          clock.tick()
          img = sensor.snapshot()
          img.lens_corr(1.8) # strength of 1.8 is good for the 2.8mm lens.
          
          for code in img.find_qrcodes():
            #Draw a Red rectangle once the camera identifies the QR code
            img.draw_rectangle(code.rect(), color = (255, 0, 0))
            #The value of the QR code read 
            value=int(code.payload())
            #Fot this example, we are reading QR codes of numbers 0 through 9 
            lpf2.load_payload('Int8',value)
            print(value)
          
          utime.sleep_ms(200)
