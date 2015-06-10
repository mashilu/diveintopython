import socket

def pbossServer():
    srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srvsock.bind(('192.168.206.50', 18088))
    srvsock.listen(5)
    srvsock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    
    print("good")
    while True:
        clisock, (remoteHost, remotePort) = srvsock.accept()
        print("[%s:%s] connected" % (remoteHost, remotePort))
        while True:
            data = clisock.recv(4096)
            print(data)
            if not data:
                clisock.close()
                break
        

        
if __name__ == "__main__":
    pbossServer()