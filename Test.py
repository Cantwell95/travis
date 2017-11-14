
#!/usr/bin/python
import time;
import getpass

print getpass.getuser()
localtime = time.localtime(time.time())
print "Local current time :", localtime
