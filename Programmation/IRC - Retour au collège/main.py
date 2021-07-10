import socket
import math

#On crée un socket et on se connecte au serveur
host="irc.root-me.org" # host du chall
port=6667 # port IRC

bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Création du socket utilisé par le bot
bot.connect((host,port)) # on se connecte au host:port

bot.send(b"NICK kouki\r\n")
print(bot.recv(1024000))

bot.send(b"USER kouki 0 * :Real Name\r\n")
print(bot.recv(1024000))

bot.send(b"JOIN #root-me_challenge\r\n")
print(bot.recv(20140000))

message = bot.send(b"PRIVMSG Candy !ep1\r\n")
rep = bot.recv(128).split(b" :")[1].replace(b' ',b'')
print(rep)

prem = math.sqrt(float(rep.split(b"/")[0]))
print("Premier = ",prem)
second = rep.split(b"/")[1].strip(b'\n')
print("Second = ",second)
res = prem * int(second)
res=str(round(res,2))
print(res)

bot.send(b'PRIVMSG Candy !ep1 -rep ' + bytes(res,encoding='utf-8') + b'\r\n')
print(bot.recv(1024000))
bot.send(b"QUIT")
print("DECONNECTE")