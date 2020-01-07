'''
Device: LEGO SPIKE Prime
Summary: This code reads numbers 0 through 9 from Grove Pyboard, and 
displays the numbers on the SPIKE Prime display 

Tufts Center for Engineering Education and Outreach
Updated on: 01/06/2020
'''
import hub,utime

hub.port.B.info()

# if info comes back with None - then you have to restart the Grove Pyboard

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
