import socket

cim=input("Add meg a szerver cimet!: ")
foglalat=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
foglalat.connect((cim, 80))
foglalat.send(b"GET / HTTP/1.1\r\nHost:  " +
	bytes(cim, "utf8")  +
	b"\r\nConnection: close\r\n\r\n")
valasz=foglalat.recv(10000)
foglalat.shutdown(socket.SHUT_RDWR)
foglalat.close()
print(repr(valasz))
