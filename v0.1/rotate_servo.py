import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(02, GPIO.OUT)
GPIO.setup(03, GPIO.OUT)

pwm=GPIO.PWM(02,50)
pwm.start(0)

id = int(sys.argv[1])
print id

def SetAngle(angle):
	GPIO.output(03, True)
	duty = angle / 18 + 2
	GPIO.output(02, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(02,False)
	pwm.ChangeDutyCycle(0)
	sleep(3)
	GPIO.output(03, False)

SetAngle(id)
pwm.stop()
GPIO.cleanup()