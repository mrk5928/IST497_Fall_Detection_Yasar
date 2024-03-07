import socket
import time

serverIP = "172.20.10.5"
serverPort = 50001

ssid = "Mahir_iPhone12"
password = "MasterBlaster"

# client
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server
sock.bind((serverIP, serverPort))

print("UDP Server Is Running:")

while True:

   data, addr = sock.recvfrom(1024)
   print("Recieved Message: ", data.decode())
