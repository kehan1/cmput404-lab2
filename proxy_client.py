#!/usr/bin/env python3
import socket

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
Host: www.google.com

"""


def connect_socket(addr):
    (family, socketype, proto, cannoname, sockaddr) = addr
    try:
        s = socket.socket(family,socketype, proto)
        s.connect(sockaddr)
        s.sendall(payload.encode())
        #print(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
               break
            full_data += data

        print(full_data)
        
    except:
        print("DID NOT CONNECT")
        pass
    finally:
        s.close()


def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    addr = addr_info[0]
    connect_socket(addr)

if __name__ == "__main__":
    main()

