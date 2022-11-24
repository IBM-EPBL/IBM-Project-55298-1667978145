import RPI.GPIO as gpio
from time import sleep

# for blinking led
BLINK_PIN = 8

# for traffic lights
RED_PIN = 
YELLOW_PIN = 
GREEN_PIN =

gpio.setwarnings(FALSE)
gpio.setmode(gpio.BOARD)    # enable board numbering
gpio.setup(BLINK_PIN, gpio.OUT, initial=gpio.LOW)

# function for blinking
def blink():
    while True:
        gpio.output(BLINK_PIN, gpio.HIGH)
        sleep(1)
        gpio.output(BLINK_PIN, gpio.LOW)
        sleep(1)

def set_red_light():
        gpio.output(RED_PIN, gpio.HIGH)
        gpio.output(YELLOW_PIN, gpio.LOW)
        gpio.output(GREEN_PIN, gpio.LOW)

def set_yellow_light():
        gpio.output(RED_PIN, gpio.LOW)
        gpio.output(YELLOW_PIN, gpio.HIGH)
        gpio.output(GREEN_PIN, gpio.LOW)

def set_green_light():
        gpio.output(RED_PIN, gpio.LOW)
        gpio.output(YELLOW_PIN, gpio.LOW)
        gpio.output(GREEN_PIN, gpio.HIGH)

# function for traffic signal
def trafficSignl():
    while True:
        set_red_light() # block traffic for 5 seconds
        sleep(5)

        set_yellow_light()  # yellow for 2 seconds
        sleep(2)
        
        set_green_light()
        sleep(5)    # allow traffic for 5 seconds