import RPi.GPIO as GPIO
import boto3
import time


SWITCH_PIN = 4
LED_PIN = 22

LAMBDA_FUNCTION = 'poo-button'

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

aws_lambda = boto3.client('lambda')


def on_push():
    GPIO.output(LED_PIN, True)
    res = aws_lambda.invoke(FunctionName=LAMBDA_FUNCTION)
    GPIO.output(LED_PIN, False)
    assert res['StatusCode'] == 200
    blink(3)


def blink(n=1, interval=.5):
    for _ in range(n):
        GPIO.output(LED_PIN, True)
        time.sleep(interval)
        GPIO.output(LED_PIN, False)
        time.sleep(interval)


try:
    while True:
        if GPIO.wait_for_edge(SWITCH_PIN, GPIO.RISING, timeout=1000):
            on_push()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
