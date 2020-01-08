'''
Device: LEGO SPIKE Prime
Summary: This code reads numbers 0, 1 or 2 from Microbit backpack, and 
displays a Heart, Simley or a Frowny icon on SPIKE Prime display 

Tufts Center for Engineering Education and Outreach
Updated on: 01/08/2020
'''

import hub,utime

hub.port.B.info()

while True:
	try:
		value = hub.port.B.device.get()[0]
		print(value)
		if (value == 1):
			hub.display.show(hub.Image.HAPPY)
			utime.sleep(0.2)
		elif (value == 2):
			hub.display.show(hub.Image.SAD)
			utime.sleep(0.2)
		elif (value==0):
			hub.display.show(hub.Image.HEART)
			utime.sleep(0.2)
	except:
		utime.sleep(0.2)
		print("Not Connected")