#! /usr/bin/env python
from os import popen
from scapy.all import sendp, IP, UDP, Ether, TCP 
from random import randrange


def sourceIPgen():
	#this function generates random IP addresses 
	# these values are not valid for first octet of IP address 

	not_valid = [10,127,254,255,1,2,169,172,192]
	first = randrange(1,256)
	while first in not_valid: first = randrange(1,256) 
	print first
	ip = ".".join([str(first),str(randrange(1,256)),str(randrange(1,256)), str(randrange(1,256))])
	return ip

def gendest(start, end):
	#this function randomly generates IP addresses of the hosts based on
	#entered start and end values 
	first = 10
	second = 102; 
	third = 20;
	ip = ".".join([str(first),str(second), str(third), str(randrange(start,end))])
	return ip #send the generated IPs

def main(): 
	start = 2 
	end = 30
	# open interface eth0 to send packets 
	interface = popen('ifconfig | awk \'/eth0/ {print $1}\'').read()
	# send normal traffic to the destination hosts 
	for i in xrange(1000):
	# form the packet
		payload = "my name is maryam kia" 
		packets = Ether()/IP(dst=gendest(start, end),src=sourceIPgen())/UDP(dport=80,sport=2)/payload 
		print(repr(packets)) 
		m = 0
	# send packet with the defined interval (seconds) 
	while m <= 8:
		sendp(packets,iface=interface.rstrip(),inter=0.2)
		m +=1
	
	#main
if __name__=="__main__":
	main()