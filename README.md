# peer2peer
Peer-2-Peer File Sharing App
SIMPLE PEER-TO-PEER FILESHARING APPLICATION
Run all the codes in python3.

Before running, 
Create a downloadLog.txt & uploadLog.txt files, 

In local host: 

First run Chunk_Announcer.py, 
Then specify the filename to announce the chunks via broadcast. 
Secondly run Chunk_Discovery.py, 
By listening the broadcast of Chunk_Announcer.py discover the chunks and the IP addresses to request them from. 
The discovering loop is forever so you can stop running after any repetitions occurred. 
A txt file will be created during the process, and show the content dictionary which includes chunknames and IP addresses. 
Thirdly run Chunk_Uploader.py, 
This will help you to start a TCP connection and get the requested contents before sending them. 
Meanwhile sending a chunk, take a look at uploadLog.txt you've created to see the chunk names, timestamps and destination IP address in more detailed way. 
Lastly, make sure Chunk_Discovery process is over to run Chunk_Downloader.py 
After requesting the content you want to download, a TCP connection will start and your request will be sent to Chunk_Uploader. 
Finally your request will be downloaded both as chunks and as a merged file. 

In Hamachi: 
First, change your IP = gethostbyname() to your personal Hamachi IP Address. 
Then in line 47 and 48, change "255.255.255.255" to "25.255.255.255" in order to broadcast. Then follow the localhost guide or the following steps: 
Run Chunk_Announcer.py 
Secondly, run Chunk_Discovery.py and discover the chunks. 
Thirdly, run Chunk_Uploader, 
Finally, run Chunk_Downloader.py.
