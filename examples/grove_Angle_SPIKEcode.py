'''
Device: LEGO SPIKE Prime
Summary: This code reads the angle value from Grove Pyboard backpack and 
displays the numbers on the SPIKE Prime display 

Tufts Center for Engineering Education and Outreach
Updated on: 01/07/2020
'''
import hub,utime

hub.port.B.info()

# if info comes back with None - then you have to restart the Grove Pyboard backpack

#Set mode to Int16
hub.port.B.device.mode(1)

while True:
	try:
		value = hub.port.B.device.get()[0]
		print(value)
		hub.display.show(str(value))
		utime.sleep(0.2)
	except:
		utime.sleep(0.2)
		print("Not Connected")
