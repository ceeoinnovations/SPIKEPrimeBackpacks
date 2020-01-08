'''
Device: Breadboard Backpack
Summary: This code sends connects the Pyboard to the WiFi, 
gets live value of the position of a satellite using International Space Station API 
and send the value of the current longitude to the SPIKE Prime

Tufts Center for Engineering Education and Outreach
Updated on: 01/08/2020
'''
import gc,utime
import pyb, micropython
import LPF2
from pyb import Pin
import machine, network, ubinascii, ujson, urequests

WiFi = network.WLAN()

mac = ubinascii.hexlify(network.WLAN().config("mac"),":").decode()
print("MAC address: " + mac)

def connect():
     if not WiFi.isconnected():
          print ("Connecting ..")
          WiFi.active(True)
          #Change the WiFi SSID and Password
          WiFi.connect("SSID","Password")
          i=0
          while i < 25 and not WiFi.isconnected():
               utime.sleep_ms(200)
               i=i+1
          if WiFi.isconnected():
               print ("Connection succeeded")
          else:
               print ("Connection failed")     

connect()
print ("WiFi: ",WiFi.isconnected())

urlValue = "https://api.wheretheiss.at/v1/satellites/25544"

def getValue():
     response=urequests.get(urlValue)
     value=response.text
     response.close()
     data=ujson.loads(value)
     result = data.get("longitude")
     return result

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

# Loop
while True:
     if not lpf2.connected:
          lpf2.sendTimer.callback(None)
          red_led.on()
          utime.sleep_ms(200)
          lpf2.initialize()
     else:
          red_led.off()
          value = getValue()
          print(value)
          lpf2.load_payload('Int8',int(value))
          utime.sleep_ms(200)
