import os
os.system("netsh interface show interface")

def disable():
    os.system("netsh wlan disconnect")

