'''
Device: LEGO SPIKE Prime
Summary: This code reads the button value from Grove Pyboard backpack and 
displays a Happy face if the button is pressed or a Sad fac if it is not, on the SPIKE Prime display 

Tufts Center for Engineering Education and Outreach
Updated on: 01/07/2020
'''
import hub,utime

hub.port.B.info()

# if info comes back with None - then you have to restart the Pyboard backpack

#Set mode to Int8
hub.port.B.device.mode(0)

while True:
	try:
		value = hub.port.B.device.get()[0]
		print(value)
		if (value == 1):
			hub.display.show(hub.Image.HAPPY)
			utime.sleep(0.2)
		else:
			hub.display.show(hub.Image.SAD)
			utime.sleep(0.2)
	except:
		utime.sleep(0.2)
		print("Not Connected")
