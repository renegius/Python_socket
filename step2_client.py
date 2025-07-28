import socket
import threading

HOST = '127.0.0.1'
PORT = 65433


def client_task(i):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = f'Hello from client {i}'
        s.sendall(msg.encode())


threads = []
for i in range(10):
    t = threading.Thread(target=client_task, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('All clients finished')
