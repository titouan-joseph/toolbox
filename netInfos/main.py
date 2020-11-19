#!/usr/bin/python3
import requests
import socket
import netifaces
import argparse

TAB = "    "


def displayHostName():
    hostname = socket.gethostname()
    print(f"Hostname : {hostname}")


def displayPublicIP():
    publicIP = requests.get("https://api.ipify.org/").text
    print(f"Public IPv4 : {publicIP}")


def displayInterfaces():
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        print(interface)
        try:
            print(f"{TAB}mac addr : {addrs[netifaces.AF_LINK][0]['addr']}")
        except KeyError:
            pass
        displayIPv4(addrs, 1)
        displayIPv6(addrs, 1)


def displayIPv4(addrs, offset=0):
    try:
        display = f"\n {TAB * offset + ' ' * 11}".join(
            [addrs[netifaces.AF_INET][i]['addr'] for i in range(len(addrs[netifaces.AF_INET]))])
        print(f"{TAB*offset}IPv4 addr : {display}")
    except (ValueError, KeyError):
        pass


def displayIPv6(addrs, offset=0):
    try:
        display = f"\n {TAB * offset + ' ' * 11}".join(
            [addrs[netifaces.AF_INET6][i]['addr'] for i in range(len(addrs[netifaces.AF_INET6]))])
        print(f"{TAB*offset}IPv6 addr : {display}")
    except (ValueError, KeyError):
        pass


def displayAllIPv4():
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        displayIPv4(addrs)


def displayAllIPv6():
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        displayIPv6(addrs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostname", help="Display the hostname", action="store_true")
    parser.add_argument("--publicip", help="Display the public address IPv4", action="store_true")
    parser.add_argument("--interfaces", help="Display MAC/IPv4/IPv6 addresses of all interface", action="store_true")
    parser.add_argument("-4", "--ipv4", help="Display all IPv4 addresses of all interface", action="store_true")
    parser.add_argument("-6", "--ipv6", help="Display all IPv6 addresses of all interface", action="store_true")
    parser.add_argument("-a", "--all", help="Display all information", action="store_true")
    args = parser.parse_args()

    if args.hostname:
        displayHostName()
    if args.publicip:
        displayPublicIP()
    if args.interfaces:
        displayInterfaces()
    if args.ipv4:
        displayAllIPv4()
    if args.ipv6:
        displayAllIPv6()
    if args.all:
        displayHostName()
        displayPublicIP()
        displayInterfaces()
