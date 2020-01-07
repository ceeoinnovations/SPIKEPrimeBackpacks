'''
Device: LEGO SPIKE Prime 
Summary: This code reads the values sent by the OpenMV camera, and 
displays the corresponding values on the SPIKE Prime display 

Author: Tufts Center for Engineering Education and Outreach
Updated on: 01/06/2020
'''
import hub,utime

hub.port.B.info()

# if info comes back with None - then you have to restart the OpenMV

#Set mode to Int8
hub.port.B.device.mode(0)

while True:
	try:
		value = hub.port.B.device.get()[0]
		print(value)
		hub.display.show(str(value))
		utime.sleep(0.2)
	except:
		utime.sleep(0.2)
		print("Not Connected")
