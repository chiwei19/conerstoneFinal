import RPi.GPIO as GPIOimport RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
servo_pin = 12  # GPIO pin 
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz 
pwm.start(0)  # Initialization

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        for i in range(0, 7):
         set_angle(30 * i)  # Change the angle (0 to 180)
         time.sleep(0.1)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()