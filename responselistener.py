import time
import fetchcommand
import onewaysend
import wifi

def listen():
    for lim in range(100): #Try for 5 minutes
        f = fetchcommand.fetchcmd()
        if f == '420':
            time.sleep(3)
        elif f.split()[0] == '421':
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



