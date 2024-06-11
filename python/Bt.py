import serial

class BluetoothSender:
    def __init__(self, port, baudrate=9600):
        
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(self.port, self.baudrate)
    
    def send(self, number):
        
        data_to_send = str(number).encode()
        self.ser.write(data_to_send)
        print(f"Sent number: {number}")
    
    def close(self):
        
        self.ser.close()

# Example usage
if __name__ == "__main__":
    port = 'COM3'  # Replace with your actual COM port
    bluetooth_sender = BluetoothSender(port)
    
    try:
        number = input("Enter a number to send: ")
        bluetooth_sender.send(number)
    finally:
        bluetooth_sender.close()
