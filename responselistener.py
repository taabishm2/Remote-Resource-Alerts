import time
import fetchcommand
import requests

def listen():
    for lim in range(100):  #Try for 5 minutes to get a new command
        try:
            f = fetchcommand.fetchcmd()
        except:
            raise Exception("fetchcommand Exception: Couldn't fetch from server")

        if f == '420':      #Implies no new command, wait for 5 seconds
            print("Waiting")
            time.sleep(5)
        elif f.split()[0] == '421':     #Implies faulty handling on server
            raise Exception("421 Error: Server code fault")
            requests.get("http://taabishm2.pythonanywhere.com/resetcmd")
            return
        else:
            requests.get("http://taabishm2.pythonanywhere.com/resetcmd")
            return f.lower()
    else:
        requests.get("http://taabishm2.pythonanywhere.com/resetcmd")
        raise Exception("Listener timed out.")

if __name__ == '__main__':
    print(listen())
