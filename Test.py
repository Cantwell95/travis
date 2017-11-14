
#!/usr/bin/python
import datetime
import getpass



print datetime.datetime.now()
username = getpass.getuser()
print username
print(getpass.getuser())

import socket
hostname = socket.gethostname()
print hostname
