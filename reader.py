import socket

def main():
    client_address = ('localhost', 12345)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(client_address)

    try:
        while True:
            data, address = sock.recvfrom(4096)
            print(f"Received: {data.decode('utf-8')}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
