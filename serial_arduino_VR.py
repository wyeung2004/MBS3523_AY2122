import serial
import time
from vpython import *

ser = serial.Serial('COM7', 9600)
time.sleep(0.5)

# bulb = sphere(radius=1,color=color.red)
# bulbGlass = sphere(radius=1.2, color=color.white, opacity=0.25)
# tube = cylinder(radius=0.6, color=color.red, axis=vector(0,1,0),length=6)
# tubeGlass = cylinder(radius=0.8, color=color.white, opacity=0.25, axis=vector(0,1,0),length=6)
digitValue = label(text='2.0', height = 30, box=True, pos=vector(0,0,2))
tube = cylinder(radius=0.6, color=color.red, axis=vector(1,0,0),length=5, pos=vector(-2.5,0,0))

while True:
    while ser.inWaiting()==0:
        pass
    VR = ser.readline()
    # print(VR)
    VR = str(VR, 'utf-8')
    # print(type(VR))
    VR = VR.strip('\r\n')
    print(VR)
    # print(type(VR))
    len = round(5/1023*float(VR),2)
    tube.length = len
    digitValue.text = str(len)