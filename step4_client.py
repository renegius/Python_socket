import socket
import threading

HOST = '127.0.0.1'
PORT = 65435


def client_task(i):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        msg = f'Hello from client {i}'
        s.sendto(msg.encode(), (HOST, PORT))
        data, _ = s.recvfrom(1024)
        print(f'Reply to client {i}: {data.decode()}')


threads = []
for i in range(10):
    t = threading.Thread(target=client_task, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('All UDP clients finished')
