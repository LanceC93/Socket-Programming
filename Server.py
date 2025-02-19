import socket

#server initialization
server_name = "Bob"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 5260))
s.listen(5)
print("Now Listening.")

#accepts clients as long as one doesnt give it an invalid number.
while True:

    #receives the data from the client
    (client, address) = s.accept()
    data = client.recv(1024)
    if not data:
        break
    print("Message received.")
    message = data.decode()

    # extracts the name from the message
    name = ""
    i = 0
    while message[i] != "#":
        name += message[i]
        i += 1
    
    #extracts the number from the message
    number = int(message[i+1:])
    if number > 100 or number < 1:    #ends connnection if given a bad number
        print(f"Invalid Number.({number}) Ending Connection.")
        client.close()
        break

    #prints the necessary messages
    server_number = 34
    print(f"Client Name: {name}, Client Number: {number} | Server Name: {server_name}, Server Number: {server_number}")
    print(f"Sum = {number + server_number}")

    #return message
    message = (server_name + "#" + f"{server_number}")
    message = message.encode()
    client.sendall(message)
    print("Message Sent.")
    client.close()