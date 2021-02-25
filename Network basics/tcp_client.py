import socket

target_host = "www.google.com" #the host we need to send or test with our tcp client
target_port = 80 # port
# client object creation
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connection establishment
client.connect((target_host,target_port))
#data we need to send to the host
client.send("GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n".encode())
 #response from client and save

response = client.recv() #4096 is the size of the recieve data
print(type(response))
print(response)