# Server.py
# Handles a custom server
from threading import Thread
import socket

class Server(Thread):
    def __init__(self, ip=None, port=None):
        Thread.__init__(self)
        
        # Thanks to Alexander on Stack Exchange for this algorithm
        # It gets the IP address of the current device
        # Can be ignored if an IP is passed to the application
        self.ip = ip or [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        
        # Set the port by either the port passed as an argument
        # or default to 2000
        self.port = port or 2000
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(1)
        
    def run(self):
        while True:
            conn, addr = self.sock.accept()
            data = conn.recv(2048) # Receive
            if not data: break
            
            if data == b'ping!':
                conn.send(b'pong!')
            else:
                print(data)
    
    def stop(self):
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()