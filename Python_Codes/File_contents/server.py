import socket



# Step 1: Create a socket (IPv4 + TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind to localhost and port 12345
server_socket.bind(('localhost', 12345))

# Step 3: Put the socket into listening mode
server_socket.listen(1)
print("Server is listening on port 12345...")

# Step 4: Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connected to client at {client_address}")

filename =  client_socket.recv(1024).decode()
print(f"requested file: {filename}")

try:
    with open(filename, 'r') as file:
        content =  file.read()
        response = content
        print(response)
except FileNotFoundError:
    response = "Error:file not found."
except Exception as e:
    response = f"Error :{str(e)}"


# Step 5: Send a welcome message to the client
# welcome_message = "Welcome to the server!"
client_socket.send(filename.encode())  # Encode string to bytes

# Step 6: Close sockets
client_socket.close()
server_socket.close()