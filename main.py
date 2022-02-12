import RPi.GPIO as GPIO
from time import sleep
import func__set_movie_list as setML


PIN_INPUT = 12
PIN_PAUSE = 6

status = 0


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_INPUT, GPIO.IN)
GPIO.setup(PIN_PAUSE, GPIO.IN)

setML.set_movie_list()


try:
    while True:
        print(status)
        if GPIO.input(PIN_INPUT) == GPIO.HIGH and status == 0:
            setML.player.play()
            status = 1
        sleep(0.5)
        if GPIO.input(PIN_PAUSE) == GPIO.HIGH and status == 1:
            setML.player.pause()
            status = 2
            sleep(0.5)
        if GPIO.input(PIN_PAUSE) == GPIO.HIGH and status == 2:
            setML.player.pause()
            status = 1
            sleep(0.5)
except(KeyboardInterrupt, SystemExit, SystemError):
    print('exit')
    GPIO.cleanup()
