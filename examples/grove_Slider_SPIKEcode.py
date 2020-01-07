'''
Device: LEGO SPIKE Prime
Summary: This code reads the slider potentiometer value from Grove Pyboard backpack and 
runs the motor with corresponding speeds

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
		#Convert the values between range 0 to 4000 to 0 to 90
		value=2*(value/100)
		hub.port.A.motor.pwm(int(value)) # powers motor from 0 - 90
		utime.sleep(0.2)
	except:
		utime.sleep(0.2)
		print("Not Connected")
