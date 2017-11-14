
#!/usr/bin/python
import datetime
import getpass
import socket


print datetime.datetime.now()
username = getpass.getuser()
print username
print(getpass.getuser())


hostname = socket.gethostname()
print hostname
