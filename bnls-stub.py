#!/usr/bin/env python3
#
# bnls-stub
# A stub for BNLS. This will just send a message then disconnect the client.
# 30 July 2020
#

from struct import *
import socket
import socketserver
import threading

message = 'This BNLS server has been sunset. Use jbls.davnit.net instead.'

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print("[{}:{}] established".format(self.client_address[0], self.client_address[1]))
        data = pack('<HB', 3 + len(message), 0xFF) + bytes(message, 'ascii')
        self.request.sendall(data)
        self.request.close()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    server = ThreadedTCPServer(("0.0.0.0", 9367), ThreadedTCPRequestHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    while server_thread.is_alive():
        pass

    server.shutdown()
    server.server_close()

