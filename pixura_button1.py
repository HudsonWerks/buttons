#!/bin/python

import RPi.GPIO as GPIO
import time
import os

# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode
GPIO.setmode(GPIO.BCM)


#REVERSE BUTTON - first one is working versions in WP
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#FORWARD BUTTON
GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#POWER BUTTON
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)


# Function on what to do when the button is pressed
#def Shutdown(channel):
#       os.system("sudo shutdown -h now")

def Forward(channel):
#        os.system("ls")
        os.system("echo 'hello - FORWARD'")


def Reverse(channel):
        os.system("echo 'hello - REVERSE'")

def Shutdown(channel):
       os.system("date")
#        os.system("sudo shutdown -h now")


# Add our function to execute when the button pressed event happens


#REVERSE BUTTON DOWN
GPIO.add_event_detect(7, GPIO.FALLING, callback = Reverse, bouncetime = 2000)

#FORWARD BUTTON DOWN
GPIO.add_event_detect(3, GPIO.FALLING, callback = Forward, bouncetime = 2000)

#POWER BUTTON DOWN
GPIO.add_event_detect(23, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)


# Now wait!
while 1:
        time.sleep(1)
