import socket
import json
import time
import os
import sys
import math
from datetime import datetime

content_name = input('Specify the content you want to download : ')
size= len(content_name)
if content_name[size-4]==".":
    content_name=content_name[:size-4]

chunks = []
c = open ('contentDictionary.txt', 'r')
index = 1
for x in range(5):
    chunkname=content_name+"_"+str(index)
    index+=1 
    chunks.append(chunkname)
    

IP_arr = []

requested_arr = []
loc_find = 0
for line in c:
    loc_find+=1
    k = json.loads(line)
    for x in range(len(chunks)):
        if (k.get(chunks[x]) != None): 
            IP_arr.append(k.get(chunks[x]))
        if chunks[x] in line:
            r = { "requested_content" : [ chunks[x] ]} 
            v = json.dumps(r)
            requested_arr.append(v)
            time.sleep(1)


isFound = False
content_arr = []
for i in range(5):
    serverPort = 8000
    m = requested_arr[i].encode()
    now = datetime.now()
    for j in range(len(IP_arr[i])):
        serverName = IP_arr[i][j] 
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))
        clientSocket.send(m)
        t = clientSocket.recv(2048)
        print(m.decode())
        if t == 0:
            print(chunks[i] + " cannot be downloaded from this IP.")
            j+=1
        else:
            print(chunks[i] + " is downloading.")
            name = t
            content_arr.append(name)
            isFound = True
            text_file=open(chunks[i] , "wb")
            text_file.write(name)
            break
            
    if isFound == False:
        print("Chunk" + chunks[i] + " cannot be downloaded from online peers.")
        break


    timestamp = datetime.timestamp(now)
    downloadLog = open ("downloadLog.txt", "a")
    downloadLog.write("timestamp :" + str(timestamp))
    downloadLog.write('\n')
    downloadLog.write("chunknames :" + chunks[i])
    downloadLog.write('\n')
    downloadLog.write("IP addresses : " + str(serverName))
    downloadLog.write('\n')
    downloadLog.write('#######################################')
    downloadLog.write('\n')
    downloadLog.write('\n')
    downloadLog.write('\n')
    downloadLog.close()
    i+=1
    clientSocket.close()
    time.sleep(2)

textFile = open(content_name + ".png", 'wb')
for i in range(len(content_arr)):
    textFile.write(content_arr[i])
    i+=1
    # textFile.write('')
textFile.close()

print("Download is complete.")