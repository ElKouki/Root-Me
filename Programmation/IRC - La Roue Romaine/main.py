  
import socket, sys, time, base64
import math,re
import codecs
server = "irc.root-me.org"
port = 6667
channel = "#root-me_challenge"
botnick = "rajoul"
serverbot = "candy"
 
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("connecting to:"+server)
irc.connect((server, port))
irc.send(b"USER kouki kouki kouki :This is a fun bot!\n")
irc.send(b"NICK kouki\n")
irc.send(b"JOIN #root-me_challenge\n")

 
irc.send(b'PRIVMSG candy :!ep3\r\n')
text = irc.recv(2040)
message=codecs.decode(str(text.strip(b'\r')),'rot_13')
print(message)
irc.send(b'PRIVMSG candy :!ep3 -rep %s\r\n'%message)
text = irc.recv(2040)
print(text)





