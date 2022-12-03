import socket

clients={}
adresses={}


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created")
s.bind(("localhost",9899))
s.listen(4)
print("waiting for clients")

class noti:
    def __init__(self, c, addr):
        self.c = c
        self.addr = addr

    def send(self):
        msg=input("mesajı giriniz: ")
        c.send(bytes(msg,"utf8"))
        print(self.addr)

while True:
    c,addr=s.accept()
        #print(addr,"adresine bağlanılıdı")
    obj=noti(c,addr)

    while True:
     obj.send()

if __name__ == "__main__":
    while True:
        pass