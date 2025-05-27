import socket

bind_ip = "0.0.0.0"
bind_port = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind port))
server.listen(5)
print "[*] Listening on %s:%d" % (bind_ip, bind_port)

#our client-handling thread
def handle_client(client_socket):
  #print out what the client sends
  request = client_socket.recv(1024)
  print :[*] Recieved: %s: % request
