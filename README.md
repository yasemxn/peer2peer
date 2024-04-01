<h1> Peer-to-Peer File Sharing App - Computer Networks </h1>

_Run all the codes in python3._

<h2>Running Guide</h2>

_Before running, 
Create a downloadLog.txt & uploadLog.txt files_

<b> In local host: </b>

1. Run Chunk_Announcer.py, <br/>
   Then specify the filename to announce the chunks via broadcast. 
2. Run Chunk_Discovery.py,<br/>
   By listening the broadcast of Chunk_Announcer.py discover the chunks and the IP addresses to request them from. The discovering loop is forever so you can stop running after any repetitions occurred. A txt file will be created during the process, and show the content dictionary which includes chunknames and IP addresses. 
3. Run Chunk_Uploader.py, <br/>
This will help you to start a TCP connection and get the requested contents before sending them. 
Meanwhile sending a chunk, take a look at uploadLog.txt you've created to see the chunk names, timestamps and destination IP address in more detailed way. 
4. Make sure Chunk_Discovery process is over to run Chunk_Downloader.py <br/>
After requesting the content you want to download, a TCP connection will start and your request will be sent to Chunk_Uploader. 
5. Finally your request will be downloaded both as chunks and as a merged file. <br/>

<b> In Hamachi: </b> <br/>
Change your IP = gethostbyname() to your personal Hamachi IP Address. <br/>
   Then in line 47 and 48, change "255.255.255.255" to "25.255.255.255" in order to broadcast. Then follow the localhost guide or the following steps: <br/>
  1._Run Chunk_Announcer.py <br/>_
  2._Run Chunk_Discovery.py and discover the chunks. <br/>_
  3._Run Chunk_Uploader, <br/>_
  4._Run Chunk_Downloader.py._
