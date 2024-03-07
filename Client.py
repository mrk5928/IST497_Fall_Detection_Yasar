from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import socket
import unit

setScreenColor(0x222222)
mic_2 = unit.get(unit.MICROPHONE_AD, unit.PORTB)

label0 = M5TextBox(55, 69, "label0", lcd.FONT_Default, 0xFFFFFF, rotate=0)

# Initialize ADC for reading analog signals
adc0 = machine.ADC(machine.Pin(36))

circle0 = M5Circle(85, 115, 15, 0xFFFFFF, 0xFFFFFF)

wifiCfg.doConnect("Mahir_iPhone12", "MasterBlaster")

def sendData(data):
    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSocket.connect(("172.20.10.5", 50001))
    udpSocket.send(data.encode())
    udpSocket.close()

while True:
    mic_value = adc0.read()  # Read analog signal from microphone
    if mic_value >= 4095:  # Check if the sound level is above a certain threshold
        rgb.setColorAll(0x00FF00)  # Set circle color to white
        sendData("Patient Is Stable")
        wait_ms(10)

    else:
        rgb.setColorAll(0x0000FF)
        wait_ms(200)
        rgb.setColorAll(0xFF0000)
        wait_ms(200)
        sendData("Emergency Help Needed!")

    label0.setText(str(mic_value))