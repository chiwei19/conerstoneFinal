#include <servo.h>
#include <bt.h>

BluetoothReceiver btReceiver;

ServoMotor servo1(9);  // Create a ServoMotor object for servo1 on pin 9
ServoMotor servo2(10); // Create a ServoMotor object for servo2 on pin 10

void setup() {
  btReceiver.begin(9600); 
}

void loop() {
  int angle;
  angle = btReceiver.listen();
  int hor, ver;
  hor = angle / 1000;
  ver = angle % 1000;
  servo1.setAngle(hor);
  servo2.setAngle(ver);
}
