# Creating TCP servers in Python is just as easy as creating a client. You might
# want to use your own TCP server when writing command shells or crafting
# a proxy (both of which we’ll do later). Let’s start by creating a standard
# multi-threaded TCP server. Crank out the code below

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9992

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#To start off, we pass in the IP address and port we want the server to
#listen on
server.bind((bind_ip,bind_port))

#the server to start listening
server.listen(5)

print ("[*] Listening on %s:%d" % (bind_ip,bind_port))

# this is our client-handling thread
def handle_client(client_socket):
    try:
        # print out what the client sends
        request = client_socket.recv(1024)
        print ('[*] Received: %s' % request)

        # send back a packet
        client_socket.send(b'ACK!')

        client_socket.close()

    except Exception as e:
        print (f'Error:  {e}')

while True:
    client,addr = server.accept()
    print ('[*] Accepted connection from: %s:%d' % (addr[0],addr[1]))

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
