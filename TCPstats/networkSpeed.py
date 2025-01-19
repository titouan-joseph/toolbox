import time
import psutil
import sys

ul = 0.00
dl = 0.00
t0 = time.time()
upload = psutil.net_io_counters().bytes_sent
download = psutil.net_io_counters().bytes_recv
up_down = (upload, download)


while True:

    last_up_down = up_down
    upload = psutil.net_io_counters().bytes_sent
    download = psutil.net_io_counters().bytes_recv
    t1 = time.time()
    up_down = (upload, download)
    try:
        ul, dl = [
            (now - last) / (t1 - t0) / 1024.0
            for now, last in zip(up_down, last_up_down)
        ]
        t0 = time.time()
    except:
        pass

    # Reset lines for output
    for _ in range(2):
        sys.stdout.write("\x1b[1A\x1b[2K")

    print("UL: {:0.2f} kB/s \n".format(ul) + "DL: {:0.2f} kB/s".format(dl))

    time.sleep(0.5)
