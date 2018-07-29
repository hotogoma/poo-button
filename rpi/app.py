import RPi.GPIO as GPIO
import time


SWITCH_PIN = 4
LED_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)


def on_push():
    blink(3)


def blink(n=1, interval=.5):
    for _ in range(n):
        GPIO.output(LED_PIN, True)
        time.sleep(interval)
        GPIO.output(LED_PIN, False)
        time.sleep(interval)


if __name__ == '__main__':
    try:
        while True:
            if GPIO.wait_for_edge(SWITCH_PIN, GPIO.RISING, timeout=1000):
                on_push()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
