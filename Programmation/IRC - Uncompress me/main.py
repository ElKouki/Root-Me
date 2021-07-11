import socket, base64, zlib

#On crée un socket et on se connecte au serveur
host="irc.root-me.org" # host du chall
port=6667 # port IRC

bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Création du socket utilisé par le bot
bot.connect((host,port)) # on se connecte au host:port

#On s'identifie
bot.send(b"NICK kouki\r\n")
print(bot.recv(1024000))
bot.send(b"USER kouki 0 * :Real Name\r\n")
print(bot.recv(1024000))

#On rejoint le channel
bot.send(b"JOIN #root-me_challenge\r\n")
print(bot.recv(20140000))

#On envoie un 1er message
message = bot.send(b"PRIVMSG Candy !ep4\r\n")
txt = bot.recv(128)
print(txt)
txt = txt.split(b" :")[1].replace(b' ',b'')
txt = str(txt)
print(txt)
rep = txt.split('\'')[1].split('\\')[0]
print(rep)
#zlib.decompress(bytes(rep, encoding='utf-8'))
#On décode le message envoyé par le bot
result = zlib.decompress(base64.b64decode(rep))
print(result)
message = bot.send(b"PRIVMSG Candy !ep4 -rep " + result + b'\r\n')
#On récupère le flag
print(bot.recv(1024000))