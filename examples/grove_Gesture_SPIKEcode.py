'''
Device: LEGO SPIKE Prime
Summary: This code reads numbers from Grove Pyboard, and 
displays a corresponding animation on the SPIKE Prime display 

Tufts Center for Engineering Education and Outreach
Updated on: 01/07/2020
'''
import hub,utime

hub.port.B.info()

# if info comes back with None - then you have to restart the Pyboard backpack

#Set mode to Int8
hub.port.B.device.mode(0)

hub.display.show(hub.Image.HAPPY)
utime.sleep(1)

#Code for animation
def left():
    for i in range(3):
        hub.display.show(hub.Image("00000:00000:00009:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00099:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00999:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:09999:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:99999:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:99990:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:99900:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:99000:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:90000:00000:00000"))
        utime.sleep(0.15)

def right():
    for i in range(3):
        hub.display.show(hub.Image("00000:00000:90000:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:99000:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:99900:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:99990:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:99999:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:09999:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00999:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00099:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00009:00000:00000"))
        utime.sleep(0.15)

def clockwise():
    for i in range(3):
        hub.display.show(hub.Image("00900:00000:00000:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00990:00009:00000:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00990:00009:00009:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00990:00009:00009:00009:00090"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00990:00009:00009:00009:00990"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00990:00009:00009:90009:09990"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00990:00009:90009:90009:09990"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("09990:90009:90009:90009:09990"))
        utime.sleep(0.15)

def counterclockwise():
    for i in range(3):
        hub.display.show(hub.Image("00900:00000:00000:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("09990:90009:90009:90009:09990"))
        utime.sleep(0.1)
         hub.display.show(hub.Image("00990:00009:90009:90009:09990"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00990:00009:00009:90009:09990"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00990:00009:00009:00009:00990"))
        utime.sleep(0.1)
         hub.display.show(hub.Image("00990:00009:00009:00009:00090"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00990:00009:00009:00000:00000"))
        utime.sleep(0.15)
        
    

def forward():
    for i in range(3):
        hub.display.show(hub.Image("99999:99999:99999:99999:99999"))
        utime.sleep(0.3)
        hub.display.show(hub.Image("00000:09990:09990:09990:00000"))
        utime.sleep(0.3)
        hub.display.show(hub.Image("00000:00000:00900:00000:00000"))
        utime.sleep(0.5)

def backward():
    for i in range(3):
        hub.display.show(hub.Image("00000:00000:00900:00000:00000"))
        utime.sleep(0.3)
        hub.display.show(hub.Image("00000:09990:09990:09990:00000"))
        utime.sleep(0.3)
        hub.display.show(hub.Image("99999:99999:99999:99999:99999"))
        utime.sleep(0.5)

def down():
    for i in range(3):
        hub.display.show(hub.Image("00900:00000:00000:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00900:00900:00000:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00900:00900:00900:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00900:00900:00900:00900:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00900:00900:00900:00900:00900"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00900:00900:00900:00900"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00900:00900:00900"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00000:00900:00900"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00000:00000:00900"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00000:00000:00000"))
        utime.sleep(0.15)

def up():
    for i in range(3):
        hub.display.show(hub.Image("00000:00000:00000:00000:00900"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00000:00900:00900"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00900:00900:00900"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00900:00900:00900:00900"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00900:00900:00900:00900:00900"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00900:00900:00900:00900:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00900:00900:00900:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00900:00900:00000:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00900:00000:00000:00000:00000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00000:00000:00000"))
        utime.sleep(0.15)

def wave():
    for i in range(2):
        hub.display.show(hub.Image("00009:00009:00009:00009:00009"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00099:00099:00099:00099:00099"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00999:00999:00999:00999:00999"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("09999:09999:09999:09999:09999"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("99999:99999:99999:99999:99999"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("99990:99990:99990:99990:99990"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("99900:99900:99900:99900:99900"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("99000:99000:99000:99000:99000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("90000:90000:90000:90000:90000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00000:00000:00000"))
        utime.sleep(0.15)

        hub.display.show(hub.Image("90000:90000:90000:90000:90000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("99000:99000:99000:99000:99000"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("99900:99900:99900:99900:99900"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("99990:99990:99990:99990:99990"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("09999:09999:09999:09999:09999"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00999:00999:00999:00999:00999"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00099:00099:00099:00099:00099"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00009:00009:00009:00009:00009"))
        utime.sleep(0.1)
        hub.display.show(hub.Image("00000:00000:00000:00000:00000"))
        utime.sleep(0.15)

while True:
	try:
		value = hub.port.B.device.get()[0]
		print(value)
          
		if (value == 1):
			print("forward")
			forward()
		elif (value == 2):
			print("backward")
			backward()
		elif (value == 3):
			print("right")
			right()
		elif (value == 4):
			print("left")
			left()             
		elif (value == 5):
			print("up")
			up()
		elif (value == 6):
			print("down")
			down()
		elif (value == 7):
			print("clockwise")
			clockwise()
		elif (value == 8):
			print("counterclockwise")
			counterclockwise()
		elif (value == 9):
			print("wave")
			wave()
		else:
			hub.display.show(hub.Image.HAPPY)
			utime.sleep(0.2)
	except:
		utime.sleep(0.2)
		print("Not Connected")
