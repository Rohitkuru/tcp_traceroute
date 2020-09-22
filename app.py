#!/usr/bin/python3


from scapy.all import *
import sys

host=sys.argv[1]
port=int(sys.argv[2])
ttl=1

while True:
   p=sr1(IP(dst=host,ttl=ttl)/TCP(dport=port,flags="S"),timeout=1,verbose=False)
   try:
      if p[ICMP].type == 11 and p[ICMP].code == 0:
         print(p[IP].src,p[ICMP].flags)
         ttl += 1
      elif p[ICMP].type == 0:
         print(p[IP].src)
         break
   except TypeError as e:
      print("No response")
      if ttl == 30:
         break
      ttl += 1
   except IndexError as e:
      print(p[IP].src,p[TCP].flags)
      print("No of hops " + str(ttl))
      break

