import RPi.GPIO as GPIO
from time import sleep
import func__set_movie_list as setML


PIN_INPUT = 12


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_INPUT, GPIO.IN)


setML.set_movie_list()


try:
    while True:
        if GPIO.input(PIN_INPUT) == GPIO.HIGH:
            setML.player.play()
        sleep(0.5)
except(KeyboardInterrupt, SystemExit, SystemError):
    print('exit')
    GPIO.cleanup()
