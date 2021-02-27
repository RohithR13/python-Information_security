import socket

target_host = "127.0.0.1" #the host we need to send or test with our tcp client
target_port = 9999 # port
# client object creation
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connection establishment
client.connect((target_host,target_port))
#data we need to send to the host
client.send("hello server".encode())
 #response from client and save

response = client.recv(1024) #4096 is the size of the recieve data
print(type(response))
print(response)