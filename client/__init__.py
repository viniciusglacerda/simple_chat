import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# if len(sys.argv) != 3 or len(sys.argv) != 1:
#     print("command: python main.py HOST PORT")
#     exit()

# SERVER_ADDRESS = str(sys.argv[1])
# PORT = int(sys.argv[2])
# DATA_LENGTH = 2048

SERVER_ADDRESS = "localhost"
PORT = 8082
DATA_LENGTH = 2048

server.connect((SERVER_ADDRESS, PORT))

def main():
    while True:
        sockets_list = [sys.stdin, server]
        
        read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

        for socks in read_sockets:
            if socks == server:
                msg = socks.recv(DATA_LENGTH)
                print(msg.decode() if type(msg) == bytes else msg)
            
            else:
                msg = sys.stdin.readline()
                server.send(bytes(msg, "utf-8"))
                print(f"<YOU> ")
                sys.stdout.flush()
    server.close()

# if __name__ == "__main__":
#     main()