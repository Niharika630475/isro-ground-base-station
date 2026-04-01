
import serial
import time

PORT = "COM3"   # Change if needed
BAUD = 9600

print("Starting Ground Base Station...")

try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)
    print("Connected to telemetry device")
except:
    print("Connection failed. Check port.")
    exit()

while True:
    if ser.in_waiting:
        data = ser.readline().decode('utf-8').strip()
        print("Telemetry:", data)
