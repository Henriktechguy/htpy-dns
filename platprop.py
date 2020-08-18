import os
#finds os info
platform = os.uname()
#parses uname components
baseos = platform.sysname
netname = platform.nodename
osrelease = platform.release
osversion = platform.version
architecture = platform.machine
#testprint
#print(platform)