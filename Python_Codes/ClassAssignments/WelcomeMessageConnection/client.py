import socket

# Step 1: Create a socket (IPv4 + TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to the server
client_socket.connect(('localhost', 12345))

# Step 3: Receive data from the server
message = client_socket.recv(1024)  # Buffer size 1024 bytes
print("Message from server:", message.decode())  # Decode bytes to string

# Step 4: Close the socket
client_socket.close()
