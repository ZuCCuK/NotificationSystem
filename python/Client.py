import socket
from winotify import Notification,audio


c = socket.socket()
port=9899
c.connect(("localhost",port))
while True:
    try:
        msg = c.recv(1024).decode()
        print(msg)
        if len(msg)>=3:
            toast = Notification(app_id="BildirimSisetmi",
                                 title="Bildirim",
                                 msg=msg,
                                 duration="long")
            toast.set_audio(audio.SMS, loop=False)
            toast.show()


    except IOError as e:
      
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: ',e)
            sys.exit()
        # hiçbir veri almazsak
        
        continue
    except Exception as e:
        
        print('Reading error: ',e)
        sys.exit()
