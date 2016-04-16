#import RPi.GPIO as GPIO
#import time

#GPIO.setmode(GPIO.BOARD)

#define pines used for stepper motor control
# corresponsd to IN# as [In1, In2, In3, In4]
# corespons to wire as [Blue, Pink, Yello, Orange]
StepPins = [2,3,4,17]

#for pin in StepPins:
#	GPIO.setup(pin,GPIO.OUT)
#	GPIO.output(pin,0)

fstepf = [	[1,1,0,0],
			[0,1,1,0],
			[0,0,1,1],
			[1,0,0,1] ]			

			
#for i in range(512):
#	for pstep in range(4):
		#for pin in range(4):
		#	GPIO.output(StepPins[pin], fstep[pstep][pin])
		#time.sleep(0.005)

for pin in StepPins:
	#print (StepPins[pin])
	print (pin)
#GPIO.cleanup()