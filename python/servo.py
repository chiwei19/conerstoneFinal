import RPi.GPIO as GPIO
import time

class ServoMotor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)  # 50 Hz frequency
        self.pwm.start(0)  # Initialization

    def set_angle(self, angle):
        duty = angle / 18 + 2
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(0)

    def stop(self):
        self.pwm.stop()

# GPIO setup
GPIO.setmode(GPIO.BOARD)

# Initialize two servo motors
servo1 = ServoMotor(12)  # Replace 12 with the GPIO pin number for servo1
servo2 = ServoMotor(13)  # Replace 13 with the GPIO pin number for servo2

try:
    while True:
        for i in range(0, 7):
            angle = 30 * i
            servo1.set_angle(angle)  # Control servo1
            servo2.set_angle(angle)  # Control servo2
            time.sleep(0.1)
except KeyboardInterrupt:
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()
