import time
import RPi.GPIO as GPIO
import subprocess, os
import signal

PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "Press Ctrl & C to Quit"


while True:
    GPIO.wait_for_edge(PIN, GPIO.FALLING)
    print "Pressed"
    start = time.time()
    time.sleep(0.2)

    while GPIO.input(PIN) == GPIO.LOW:
        time.sleep(0.01)
    length = time.time() - start
    print length
    print "Started Linphone"

    str = "linphonec"
    p=subprocess.Popen(str,shell=True, preexec_fn=os.setsid)

    if length > 2:
        print "Long Press"
        print "Stopped"
#        os.killpg(p.pid, signal.SIGTERM)
#       strkill = "killall -9 linphonec"
#        os.kill(p.pid, signal.SIGKILL)
        os.system("killall -9 linphonec")
        os.system("reset")
    else:
        print "Short Press"
