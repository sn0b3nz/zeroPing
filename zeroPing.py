import os
import sys
import colorama


class ping:
   def __init__(self):
       print ("nombre del sitio : \r")
       pings=input("")
       self.ping_os=os.system("ping "+pings)
       print (ping)
if __name__=="__main__":
	ping()