'''
Device: LEGO SPIKE Prime 
Summary: This code reads a 1 or a 3 from the OpenMV camera, and 
displays a Happy or a Sad face on the SPIKE Prime display. 

Tufts Center for Engineering Education and Outreach
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
		if (value == 1):
			print("HAPPY")
			hub.display.show(hub.Image.HAPPY)
		elif (value == 3):
			print("SAD")
			hub.display.show(hub.Image.SAD)
		else:
			hub.display.show("-")
		utime.sleep(0.5)
	except:
		utime.sleep(0.5)
		print("Not Connected")
