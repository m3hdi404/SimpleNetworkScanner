#!/usr/bin/env python3

import subprocess as sb
import os
import threading

def scan(hostname):
    res = sb.call("ping -c 3 " + hostname, shell=True, stdout=open(os.devnull, 'wb'), stderr=sb.STDOUT)
    return res

def results(host):
    resu = scan(host)
    if resu == 0:
        print(host)
        print('*' * 20)

def main():
    print("Hosts Up : ")
    print('*' * 20)
    for i in range(0,256):
        ip = '192.168.43.' + str(i)
        x = threading.Thread(target = results, args = (ip,))
        x.start()


if __name__ == "__main__":
    main()
