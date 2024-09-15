import socket
import time

def sigma():
    try:
        ip = "158.101.31.180"
        # ip = "127.0.0.1"
        port = 13452
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            server.connect((ip, port))
            print(server.recv(1024).decode("utf-8"))
            server.close()
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        if not isinstance(e, KeyboardInterrupt):
            try:
                print("Encountered error, retrying")
                server = server.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.connect((ip, port))
                print(server.recv(1024).decode("utf-8"))
            except:
                pass
        else:
            quit()

if __name__ == "__main__":
    while True:
        try:
            sigma()
        except:
            sigma()