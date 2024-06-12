#include <Servo.h>   //載入函式庫，這是內建的，不用安裝

Servo servo1;
Servo servo2;   // 建立SERVO物件

void setup() {
  pinMode(3,OUTPUT);
  servo1.attach(4);  // 設定要將伺服馬達接到哪一個PIN腳
  servo2.attach(5);  // 設定要將伺服馬達接到哪一個PIN腳
  // bluetooth initialization
  Serial1.begin(9600);
  // Serial window
  Serial.begin(9600);
}

void loop() { 
  angle = ask_BT();
  int hor, ver;
  hor = angle / 1000;
  ver = angle % 1000;
  servo1.setAngle(hor);
  servo2.setAngle(ver);
  
}