from socket import *
import os
import json
import time

Port = 5001
client = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
client.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

broadcastIP = '25.255.255.255'
broadcastPort = 5001
addr = (broadcastIP , broadcastPort)


client.bind(("", 5001))

content_arr = []

while True:
    IP, server = client.recvfrom(2048)
    y, server = client.recvfrom(2048)
    c = json.loads(y)
    content_dictionary = { c.get("chunks")[0] : [IP.decode()]}
    content_arr.append(content_dictionary)

    textFile = open(("contentDictionary.txt"), 'w')
    for i in range (len(content_arr)):
        textFile.write(json.dumps(content_arr[i]))
        textFile.write('\n')
    textFile.close()
   

    print("Chunks discovered till now : " )
    print(content_arr)
    time.sleep(3)

        