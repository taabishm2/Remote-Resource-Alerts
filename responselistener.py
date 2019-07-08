import time
import fetchcommand
import onewaysend
import wifi

def listen():
    for lim in range(100):  #Try for 5 minutes to get a new command
        f = fetchcommand.fetchcmd()
        if f == '420':      #Implies no new command, wait for 5 seconds
            time.sleep(5)
        elif f.split()[0] == '421':     #Implies faulty handling on server
            raise("421 Error: Server code fault")
            return
        else:
            if f.lower() == "execute":
                onewaysend.twilioSend("Shuting Down WiFi")
                wifi.disable()
                return
            else:
                onewaysend.twilioSend("unrecognized command")
                return



