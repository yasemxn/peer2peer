from socket import *
import json
import os
import sys
import math
import time
from datetime import datetime

serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(10)
print('The uploader is ready to receive')


while 1:
    connectionSocket, addr = serverSocket.accept()
    v = connectionSocket.recv(2048)
    now = datetime.now()
    h = json.loads(v)
    m = h.get( "requested_content" )
    print(m)
    time.sleep(10)
    with open (m[0], 'rb') as chunk_py:
        t = chunk_py.read(2048)
        print(t)
        connectionSocket.send(t)
        
    timestamp = datetime.timestamp(now)
    uploadLog = open ("uploadLog.txt", "a")
    uploadLog.write("timestamp :" + str(timestamp))
    uploadLog.write('\n')
    uploadLog.write("chunkname :" + m[0])
    uploadLog.write('\n')
    uploadLog.write("IP Addresses :" + str(addr))
    uploadLog.write('\n')
    uploadLog.write("##############################")
    uploadLog.write('\n')
    uploadLog.write('\n')
    uploadLog.write('\n')
    uploadLog.close()
connectionSocket.close()

