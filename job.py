import time
import sys
import atexit
import signal

def exit_handler():
    print("Exit")

def kill_handler(*args):
    print("Cleaning up")
    sys.exit(0)

atexit.register(exit_handler)
signal.signal(signal.SIGINT, kill_handler)
signal.signal(signal.SIGTERM, kill_handler)

print("Hello world!")
time.sleep(3)
print("Hello again!")
sys.exit(0)
