import serial

ser = serial.Serial('COM7', 19200)

while True:
    command = input('Input you command: ')
    command = command + '\r'
    ser.write(command.encode())

