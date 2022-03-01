from socket import *
import os
import math
import time
import json
import sys

#host = gethostname()
#IP = gethostbyname(host) # Change this to your ip address on hamachi and comment host.
IP = '25.41.103.75'

Port = 5001
clientAddress = (IP, Port)
server = socket(AF_INET, SOCK_DGRAM)
server.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

print("[CONNECTED]")

content_name = input('Specify the filename: ')
filename = content_name+'.png'
c = os.path.getsize(filename)
CHUNK_SIZE = math.ceil(math.ceil(c)/5) 

print("Number of chunks: 5 ")
print("Starting to announce the files...")

arr = []
index = 1
with open(filename, 'rb') as infile:
    chunk = infile.read(int(CHUNK_SIZE))
    while chunk:
        chunkname = content_name+'_'+str(index)
        x = { "chunks" : [ chunkname ]}
        s = json.dumps(x)
        arr.append(s)
        with open(chunkname,'wb+') as chunk_file:
            chunk_file.write(chunk)
        index += 1
        chunk = infile.read(int(CHUNK_SIZE))
        time.sleep(1)
    chunk_file.close()

while True:
    print("Announced")

    for i in range(len(arr)):
        server.sendto(IP.encode("utf-8"), ('25.255.255.255' , 5001)) # Change this to 25.255.255.255 while using Hamachi.
        server.sendto(arr[i].encode("utf-8"),('25.255.255.255', 5001)) # Change this to 25.255.255.255 while using Hamachi.
        i += 1

    time.sleep(60)


server.close()