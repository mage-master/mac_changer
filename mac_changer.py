#!/usr/bin/env python3

from subprocess import run, check_output
import argparse
import re
import sys


def main():
    try:
        parser = argparse.ArgumentParser(description="Program to change mac address of specified network interface")
        
        parser.add_argument('-i', "--interface", help="Enter the changing interface", type=str)
        parser.add_argument('-m', "--mac", help="Enter the new mac address", type=str)
        args = parser.parse_args()
        
        print("\n\033[1;31m[.] ARGUMENT MODE [.]")
        changer(args.interface, args.mac)
        verify(args.interface, args.mac)
        
    except TypeError:
        try:
            print("\n\033[1;31m[.] MANUAL MODE [.]")
            interface = input("\n\033[32m[-] Enter network interface name : ")
            mac = input("[-] Enter new mac: ")
    
            changer(interface, mac)
            verify(interface, mac)    

        except:
            print("\n\033[1;37;41m[!] Please input valid arguments [!]\033[m\n")
            print("\033[5;34;40m[+] Program by mage-master [+]\033[m\n")
            sys.exit("\033[1;33m[!] Exiting Program [!]\033[m\n")


def verify(interface, mac):        
    ifconfig = check_output(["sudo", "ifconfig", interface])
    result = regex(ifconfig)

    if result == mac:
        print(f"\n\033[1;33m[+] Mac Address successfully changed to {result} [+]\n")
    
    else:
        print("\n\033[5;31m[!] Unexpected Error, unable to append MAC Address n [!]\n")
        sys.exit("\033[1;33m[!] Exiting Program [!]\033[m\n")
        
           
def changer(interface, mac):
    run(["sudo", "ifconfig", interface, "down"])
    run(["sudo", "ifconfig", interface, "hw", "ether", mac])
    run(["sudo", "ifconfig", interface, "up"])
    

def regex(check):
    regex = re.search(r"\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}", str(check))
    result = regex.group(0)
    return result
    
    
if __name__ == "__main__":
    main()
    print("\033[5;34;40m[+] Program by mage-master [+]\033[m\n")
