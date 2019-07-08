import time
import fetchcommand

def listen():
    for lim in range(100):  #Try for 5 minutes to get a new command
        try:
            f = fetchcommand.fetchcmd()
        except:
            raise("fetchcommand Exception: Couldn't fetch from server")

        if f == '420':      #Implies no new command, wait for 5 seconds
            time.sleep(5)
        elif f.split()[0] == '421':     #Implies faulty handling on server
            raise("421 Error: Server code fault")
            return
        else:
            return f.lower()
    else:
        raise("Listener timed out.")

if __name__ == '__main__':
    print(listen())
