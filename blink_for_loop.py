import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
red=18
GPIO.setup(red,GPIO.OUT)
blink_num=input("How many times do you want to blink?")
for i in range(0,blink_num):
		GPIO.output(red,True)
		time.sleep(1)
		GPIO.output(red,False)
		time.sleep(1)
GPIO.cleanup()
