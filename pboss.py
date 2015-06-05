import socket

def pbossServer():
    srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srvsock.bind(('192.168.206.50', 8088))
    srvsock.listen(5)
    
    while True:
        clisock, (remoteHost, remotePort) = srvsock.accept()
        print("[%s:%s] connected" % (remoteHost, remotePort))
        clisock.close()
        
if __name__ == "__main__":
    pbossServer()