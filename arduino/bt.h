class BluetoothReceiver {
public:
  void begin(long baudrate) {
    Serial.begin(baudrate); // Start serial communication at the specified baud rate
    Serial.println("Waiting for Bluetooth signal...");
  }

  int listen() {
    int receivedNumber;
    if (Serial.available()) { // Check if there is any data available to read
      receivedNumber = Serial.parseInt(); // Read the number sent via Bluetooth
      Serial.print("Received number: ");
      Serial.println(receivedNumber); // Print the received number to the serial monitor
    }
    return receivedNumber;
  }
};

BluetoothReceiver btReceiver;

void setup() {
  btReceiver.begin(9600); // Initialize BluetoothReceiver with 9600 baud rate
}

void loop() {
  btReceiver.listen(); // Continuously listen for incoming Bluetooth data
}
