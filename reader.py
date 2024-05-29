import socket

class Reader:
    def __init__(self, address):
        self.client_address = address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.client_address)

    def receive_time(self):
        data, address = self.sock.recvfrom(4096)
        return data.decode('utf-8')

    def close(self):
        self.sock.close()

def main():
    reader = Reader(('localhost', 12345))
    try:
        while True:
            received_time = reader.receive_time()
            print(f"Received: {received_time}")
    finally:
        reader.close()

if __name__ == "__main__":
    main()
