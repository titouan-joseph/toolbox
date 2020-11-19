# Network Infos

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/) [![Generic badge](https://img.shields.io/badge/netifaces-0.10.9-orange.svg)](https://github.com/al45tair/netifaces) [![Generic badge](https://img.shields.io/badge/requests-2.23.0-orange.svg)](https://github.com/psf/requests)

## Presentation

Tool for display some network informations like : 

- Hostname
- Public IPv4
- MAC addresses
- Local IPv4 and IPv6



## How to use

usage: ``main.py [-h] [--hostname] [--publicip] [--interfaces] [-4] [-6] [-a]``

```bash
 optional arguments:
 -h, --help    show this help message and exit
  --hostname    Display the hostname
  --publicip    Display the public address IPv4
  --interfaces  Display MAC/IPv4/IPv6 addresses of all interface
  -4, --ipv4    Display all IPv4 addresses of all interface
  -6, --ipv6    Display all IPv6 addresses of all interface
  -a, --all     Display all information
```

