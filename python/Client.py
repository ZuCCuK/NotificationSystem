import socket
from winotify import Notification,audio


c = socket.socket()
port=9899
c.connect(("localhost",port))
while True:
    try:
        msg = c.recv(1024).decode()
        print(msg)
        if len(msg)>=10:
            toast = Notification(app_id="BildirimSisetmi",
                                 title="Bildirim",
                                 msg=msg,
                                 duration="long")
            toast.set_audio(audio.SMS, loop=False)
            toast.show()


    except:
        pass