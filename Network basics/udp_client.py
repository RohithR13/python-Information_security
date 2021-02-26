import  socket
#for working this program there should be sever running on the  target host and port 
target_host = "127.0.0.1" #host address of udp server which we need to test
target_port = 80 #port

#create udp client socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "data to send"

#in udp there is no connection establishment step it is a connectionless protocol
#send data 
client.sendto(message.encode(),(target_host,target_port))
data, addr = client.recvfrom(4096)#4096is buffer size
print(data)
print(addr)


