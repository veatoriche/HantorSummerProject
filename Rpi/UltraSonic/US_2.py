import RPi.GPIO as gpio
import time
  
gpio.setmode(gpio.BCM)

trig = 10
echo = 9

print "start"

fp = open("us_1.txt",'w')

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)


try :
    while True :
        gpio.output(trig, False)
        time.sleep(0.5)

        gpio.output(trig, True)
        time.sleep(0.00001)
        gpio.output(trig, False)

        while gpio.input(echo) == 0 :
            pulse_start = time.time()

        while gpio.input(echo) == 1 :
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)
        
        fp.write(str(distance))
        print "Distance : ", distance, "cm"


except :
    gpio.cleanup()
