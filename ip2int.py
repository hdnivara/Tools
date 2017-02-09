#!/usr/bin/python
"""
Convert an IPv4 address from string to integer.
"""

import argparse
import socket
import struct

parser = argparse.ArgumentParser(description="Print integer form of an IPv4 string")
parser.add_argument("IPv4_STRING", help="IPv4 string")
ip_str = vars(parser.parse_args())['IPv4_STRING']

def ip2int(ipv4_str):
    return struct.unpack("!I", socket.inet_aton(ipv4_str))[0]

def ip_display(ipv4_str, ipv4_int):
    print "IPv4 String: %s" % (ipv4_str)
    print "IPv4 Integer: %u, 0x%08X" % (ipv4_int, ipv4_int)

ip_display(ip_str, ip2int(ip_str))
