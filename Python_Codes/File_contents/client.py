import socket

# Step 1: Create a socket (IPv4 + TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to the server
client_socket.connect(('localhost', 12345))
filename = input("Enter the filename:")
client_socket.send(filename.encode())

# Step 3: Receive data from the server
response = client_socket.recv(4096).decode()  # Buffer size 1024 bytes
print(response)
# print("Message from server:", message.decode())  # Decode bytes to string

# Step 4: Close the socket
client_socket.close()