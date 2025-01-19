import icmplib
import argparse
import sys

def MTU_finder(host):
  global MTU
  found = False

  while not found:
    if DEBUG:
      print("[DEBUG] Testing MTU:", MTU)

    result = icmplib.ping(host, payload_size=MTU, count=1, interval=0)
    if result.is_alive:
      found = True
    else:       
      MTU -= 1

  print(f"GOOD, the MTU is {MTU}")

def check_packet_loss(host):
  global MTU

  result = icmplib.ping(host, payload_size=MTU, count=100, interval=0)

  print(f"{result.packet_loss * 100}% packet loss | min: {result.min_rtt} | max: {result.max_rtt} | avg: {result.avg_rtt}")

if __name__ == "__main__":
  # Config

  # Parser
  parser = argparse.ArgumentParser(description="MTU-finder")
  parser.add_argument("host", help="Host to test")
  parser.add_argument("-d", "--debug", help="Debug mode", action="store_true")
  args = parser.parse_args()

  # VARS
  MTU = 1500
  DEBUG = args.debug

  print("[INFO] Starting MTU-finder...")
  MTU_finder(args.host)
  
  print("[INFO] Checking packet loss with 100 requests...")
  check_packet_loss(args.host)

  sys.exit()
