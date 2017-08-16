import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
for i in range(50)
    GPIO.output(18, True)
	time.sleep(1)
	GPIO.output(18, False)
	time.sleep(1)

GPIO.cleanup()