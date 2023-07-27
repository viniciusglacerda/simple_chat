import socket
import sys
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# if len(sys.argv) != 3 or len(sys.argv) != 1:
#     print("command: python main.py HOST PORT")
#     exit()

# SERVER_ADDRESS = str(sys.argv[1])
# PORT = int(sys.argv[2])
MAX_CONNECTIONS = 9
DATA_LENGTH = 2048

SERVER_ADDRESS = "localhost"
PORT = 8082
DATA_LENGTH = 2048

server.bind((SERVER_ADDRESS, PORT))

server.listen(MAX_CONNECTIONS)

clients_list = []

def client(conn, addr):
    conn.send(bytes("Welcome to this chat!", "utf-8"))

    while True:
        try:
            msg = conn.recv(DATA_LENGTH)
            if msg:
                formatted_msg = f"<{addr[0]}> {msg}"

                print(formatted_msg)

                # Broadcasting
                broadcast(formatted_msg, conn)
            
            else:
                # msg have no content, connection is broken
                remove(conn)
        except:
            continue

def broadcast(msg, conn):
    for client in clients_list:
        if client != conn:
            try:
                client.send(bytes(msg, "utf-8"))
            except:
                client.close()
                remove(client)

def remove(client):
    if client in clients_list:
        clients_list.remove(client)

def main():
    while True:
        conn, addr = server.accept()

        clients_list.append(conn)

        print(f"User: {addr[0]} connected")

        # A new Thread for each user connection
        user_thread = threading.Thread(target=client, args=(conn, addr))
        user_thread.start()
    conn.close()
    server.close()

# if __name__ == "__main__":
#     main()