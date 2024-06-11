class ServoMotor {
public:
    ServoMotor(int pin) : pin(pin) {
        // Constructor initializes the pin and attaches the servo
        servo.attach(pin);
    }

    void setAngle(int angle) {
        servo.write(angle);
        delay(1000); // Wait 1 second to allow the servo to move
    }

private:
    int pin;
    Servo servo; // Create a Servo object to control the servo motor
};

ServoMotor servo1(9);  // Create a ServoMotor object for servo1 on pin 9
ServoMotor servo2(10); // Create a ServoMotor object for servo2 on pin 10

void setup() {
    // No initialization needed in setup
}

void loop() {
    for (int i = 0; i < 7; i++) {
        int angle = 30 * i;   // Calculate the angle
        servo1.setAngle(angle); // Set the angle for servo1
        servo2.setAngle(angle); // Set the angle for servo2
        delay(100);            // Delay for 0.1 seconds
    }
}
