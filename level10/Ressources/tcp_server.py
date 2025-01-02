import socket

PORT = 6969
HOST = '0.0.0.0'


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)

        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)


if __name__ == '__main__':
    main()
