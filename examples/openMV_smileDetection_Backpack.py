'''
Device: OpenMV 
Summary: This code detects a smile or a frown using OpenMV camera, and 
sends a value of 1 or a 3 to indicate Smile or a frown to the SPIKE Prime. 
Note: Copy openMV_smileDetection_smile.network on the OpenMV flash

Author: Tufts Center for Engineering Education and Outreach
Updated on: 01/06/2020
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
blue_led=pyb.LED(2)
blue_led.on()

#lpf2 = LPF2.LPF2(1, 'P1', 'P0', modes, LPF2.SPIKE_Ultrasonic, timer = 4, freq = 5)    # OpenMV
lpf2 = LPF2.LPF2(3, 'P4', 'P5', modes, LPF2.SPIKE_Ultrasonic, timer = 4, freq = 5)    # OpenMV
#lpf2 = LPF2.Prime_LPF2(1, 'Y1', 'Y2', modes, LPF2.SPIKE_Ultrasonic, timer = 4, freq = 5)    # PyBoard
# use EV3_LPF2 or Prime_LPF2 - also make sure to select the port type on the EV3 to be ev3-uart

lpf2.initialize()

value = 0

# Simle detection using Haar Cascade + CNN.
import sensor, time, image, os, nn

sensor.reset()                          # Reset and initialize the sensor.
sensor.set_contrast(2)
sensor.set_pixformat(sensor.RGB565)     # Set pixel format to RGB565
sensor.set_framesize(sensor.QVGA)       # Set frame size to QVGA (320x240)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False)


# Load smile detection network
net = nn.load('/openMV_smileDetection_Backpack.network')

face_cascade = image.HaarCascade("frontalface", stages=25)
print(face_cascade)

# Loop
while True:
     if not lpf2.connected:
          lpf2.sendTimer.callback(None)
          red_led.on()
          utime.sleep_ms(200)
          lpf2.initialize()
     else:
          red_led.off()
          # Capture snapshot
          img = sensor.snapshot()

          # Find faces.
          objects = img.find_features(face_cascade, threshold=0.75, scale_factor=1.25)
          print("hello")
          lpf2.load_payload('Int8',2)

          # Detect smiles
          for r in objects:
               # Resize and center detection area
               r = [r[0]+10, r[1]+25, int(r[2]*0.70), int(r[2]*0.70)]
               img.draw_rectangle(r)
               out = net.forward(img, roi=r, softmax=True)
               print("got to this point")
               blue_led.off()
               if (out[0] > 0.8):
                    lpf2.load_payload('Int8',1)
                    print("SMILE")
                    green_led.on()
               else:
                    lpf2.load_payload('Int8',3)
                    print("FROWN")
                    red_led.on()
               utime.sleep_ms(500)
               img.draw_string(r[0], r[1], ':)' if (out[0] > 0.9) else ':(', color=(255), scale=2)
