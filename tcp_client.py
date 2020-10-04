import socket
import sys

target_host = str(input('Taget host: '))
target_port = int(input('Taget port: '))


#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((str(target_host),int(target_port)))

#send some data
#client.send(b'GET /HTTP/1.1\r\nHost: google.com\r\n\r\n')
message = str.encode((input('Enter your message: ')))
client.send(message)

# receive some data
response = client.recv(4096)

print (response)
