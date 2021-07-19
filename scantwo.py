#!/usr/bin/env python3

# This Is A Progtam To Scan All Hosts In Network
# Just Give sudo Permision
# Arguments : Network Gateway, Network Interface

import scapy.all as sc
import sys

def scan(ip,interf):
    arp = sc.ARP(pdst=ip)
    ether = sc.Ether(dst='ff:ff:ff:ff:ff:ff')
    frame = ether / arp
    answer = sc.srp(frame,timeout=5,verbose=False,iface=interf)[0]
    res_list = []
    for i in range(0,len(answer)):
        client_dict = {"ip" : answer[i][1].psrc, "mac" : answer[i][1].hwsrc}
        res_list.append(client_dict)
    return res_list

def result_print(reslist):
    print("-----------------------------------\nIP Address\tMAC Address\n-----------------------------------")
    for element in reslist:
        print("{}\t{}".format(element["ip"], element["mac"]))

ip_range = sys.argv[1] + '/24'
interface = sys.argv[2]
output = scan(ip_range,interface)
result_print(output)