#HOW TO USE >> python3 alternativeMobile.py <PORT NUMBER>


import socket
import os
import sys

if len(sys.argv) < 2:
     print("E: SHOW HOW TO USE ON THE SCRIPT")
     quit()

port = int(sys.argv[1])
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("52.78.139.181", port))
client_socket.send("second".encode())

data = client_socket.recv(512).decode()
print(data)
os.system("sudo rfcomm bind rfcomm0 98:D3:91:FD:37:9A")
os.system("python3 smartmobile.py --prototxt MobileNetSSD_deploy.prototxt --model MobileNetSSD_deploy.caffemodel")
print ("socket colsed... END.")
