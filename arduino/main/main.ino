#include <Servo.h>   //載入函式庫，這是內建的，不用安裝

Servo servo1;
Servo servo2;   // 建立SERVO物件

void setup() {
  pinMode(3,OUTPUT);
  servo1.attach(4);  // 設定要將伺服馬達接到哪一個PIN腳
  servo2.attach(5);  // 設定要將伺服馬達接到哪一個PIN腳
}

void loop() { 
  servo1.write(0);   
  servo2.write(0); 
  delay(500);
  servo2.write(45); 
  delay(500);
  servo2.write(90); 
  delay(500);
  
  analogWrite(3,255);
  servo1.write(0);  
  delay(5000);
  servo1.write(5);  
  delay(5000);
  servo1.write(10);  
  delay(5000);
  servo1.write(15);  
  delay(5000);
  servo1.write(20);  
  delay(5000);
  servo1.write(25);  
  delay(5000);
  servo1.write(30);  
  delay(5000);
  servo1.write(35);  
  delay(5000);
  servo1.write(40);  
  delay(5000);
  servo1.write(45);  
  

  
  
}