import socket

if __name__ == "__main__":
    try:
        ip = "127.0.0.1"
        port = 13452
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('', port))
        print(f"Established server on {socket.gethostbyname(socket.gethostname())}")
        server.listen(2)
        print("Server actively listening for incoming connections")
        while True:
            print("Waiting for another incoming connection")
            client, address = server.accept()
            print(f"Connection Established - {address[0]}:{address[1]}")
            client.close()
            print(f"Connection Closed - {address[0]}:{address[1]}")
    except Exception as x:
        if isinstance(x, KeyboardInterrupt):
            server.close()
            client.close()
            quit("Closed connections & quitting")