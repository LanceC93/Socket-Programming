import socket
import sys

number = input("Pick a number between 1-100: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connects and sends message to server
name = "John"
message = name + "#" + number  #combines the name and given int with a # to seperate them
message = message.encode()    #converts to bytes
s.connect(("localhost", 5260))
print("Connected.")
s.sendall(message)
print("Message Sent.")

#receives message from server
data = s.recv(1024) #receives return number
if not data:
    print("Received no return message.")
    s.close()
    sys.exit()
message = data.decode()

# extracts the name from the message
server_name = ""
i = 0
while message[i] != "#":
    server_name += message[i]
    i += 1

server_number = int(message[i+1:])  #extracts the number from the message

#prints necessary text and closes
print("Message received.")
print(f"Client Name: {name}, Client Number: {number} | Server Name: {server_name}, Server Number: {server_number}")
print(f"Sum = {int(number) + server_number}")
s.close()