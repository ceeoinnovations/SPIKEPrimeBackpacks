'''
Device: LEGO SPIKE Prime
Summary: This code reads numbers 1 or 2 from Breadboard backpack, and 
controls motors connected to the SPIKE Prime 

Tufts Center for Engineering Education and Outreach
Updated on: 01/07/2020
'''
import hub,utime

#Breadboard Backpack connected to port B
hub.port.B.info()

# if info comes back with None - then you have to restart the Grove Pyboard

#Set mode to Int8
hub.port.B.device.mode(0)

while True:
	if hub.button.center.is_pressed()==True:
		break
	try:
		value = hub.port.B.device.get()[0]
		print(value)
		if (value == 1):
			hub.display.show(hub.Image.HAPPY)
		else:
			hub.display.show(hub.Image.SAD)     

		utime.sleep(0.2)
	except:
		utime.sleep(0.2)
		print("Not Connected")


