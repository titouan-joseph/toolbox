import time
import os
import sys
import psutil
import argparse
from operator import xor
import shutil

isWindows = sys.platform.startswith('win')

# Check if netstat is installed
if shutil.which('netstat') is None:
    print('netstat is not installed')
    print('Install netstat for linux using the command: sudo apt-get install net-tools')
    sys.exit(1)

# Parser for command line arguments
parser = argparse.ArgumentParser(description='TCP-stats')
parser.add_argument('-i', '--interval', type=int,
                    default=1, help='Interval in seconds')
parser.add_argument('-l', '--log', type=str,
                    help='Output file', metavar='FILE')
parser.add_argument('-a', '--append', action='store_true',
                    help='Append to output file')
parser.add_argument('-o', '--overwrite', action='store_true',
                    help='overwrite log to output file')
args = parser.parse_args()

# CSV header
file = None
if args.log:
    file = args.log if args.log.endswith('.csv') else args.log + '.csv'

    if os.path.exists(file) and not xor(args.overwrite, args.append):
        print(f'{file} already exists, if you want to append, please use -a option or -w option '
              f'to overwrite. You can not use both at the same time.')
        sys.exit(1)

    if not os.path.exists(file) or args.overwrite:
        with open(file, 'w') as f:
            f.write('time;tcp_received_segments;tcp_sent_ou_segments;tcp_retransmitted_segments;'
                    'retransmission_rate;ul_kBps;dl_kBps\n')

# Network speed vars
ul = 0.00
dl = 0.00
t0 = time.time()
up_down = (psutil.net_io_counters().bytes_sent,
           psutil.net_io_counters().bytes_recv)

# TCP stats vars
netstatCommand = 'netstat -s | find "Segments"' if isWindows else 'netstat -s | grep "segments"'

# Prepare lines for output
for _ in range(5):
    sys.stdout.write("\n")

# Main loop
while True:
    # Get network speed
    last_up_down = up_down
    up_down = (psutil.net_io_counters().bytes_sent,
               psutil.net_io_counters().bytes_recv)
    t1 = time.time()
    try:
        ul, dl = [
            (now - last) / (t1 - t0) / 1024.0
            for now, last in zip(up_down, last_up_down)
        ]
        t0 = time.time()
    except:
        pass

    # Get TCP stats
    tcpSeg = os.popen(netstatCommand).read().split("\n")
    tcprecv = int(tcpSeg[0].split('=')[1]) if isWindows else int(
        tcpSeg[0].split()[0])
    tcpsend = int(tcpSeg[1].split('=')[1]) if isWindows else int(
        tcpSeg[1].split()[0])
    tcpretr = int(tcpSeg[2].split('=')[1]) if isWindows else int(
        tcpSeg[2].split()[0])

    # Print
    # Reset lines for output
    for _ in range(5):
        sys.stdout.write("\x1b[1A\x1b[2K")

    sys.stdout.write(f"Segment received : {tcprecv} \n"
                     f"Segment sent out : {tcpsend} \n"
                     f"Segment retransmitted : {tcpretr} \n"
                     f"Retransmission : {(tcpretr/tcpsend)*100:.4f} %\n"
                     f"UL: {ul:.2f} kB/s | DL: {dl:.2f} kB/s\n")

    # Write to file for logging
    if (file):
        with open(file, 'a') as f:
            f.write(
                f"{t1};{tcprecv};{tcpsend};{tcpretr};{(tcpretr/tcpsend)*100:.4f};{ul:.2f};{dl:.2f}\n")

    time.sleep(args.interval)
