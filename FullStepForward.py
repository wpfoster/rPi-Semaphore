import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

#define pines used for stepper motor control
# corresponsd to IN# as [In1, In2, In3, In4]
# corespons to wire as [Blue, Pink, Yello, Orange]
StepPins = [27,22,4,17]

for pin in StepPins:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)
	

	
fstepf = [	[1,1,0,0],
			[0,1,1,0],
			[0,0,1,1],
			[1,0,0,1] ]			

			
for i in range(512):
	for pstep in range(4):
		for pin in range(4):
			GPIO.output(StepPins[pin], fstepf[pstep][pin])
		time.sleep(0.005)



		
GPIO.cleanup()