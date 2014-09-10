import RPi.GPIO as GPIO
from subprocess import call
import time
import ephem
import datetime
o=ephem.Observer()
o.lat='-34.9290'
o.long='138.6010'
s=ephem.Sun()
s.compute()
print ephem.localtime(o.next_rising(s))

sensorPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

#print "Sunset is ", hourSunset, " and now is ", hourNow

while True:
   time.sleep(0.1)
   prevState = currState
   currState = GPIO.input(sensorPin)
   if currState != prevState:
     #  print currState
     call(["/usr/bin/python", "/home/pi/lightsOnDetect.py"])
     newState = "HIGH" if currState else "LOW"
     print "GPIO pin %s is %s" % (sensorPin, newState)


