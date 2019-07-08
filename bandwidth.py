import time
import psutil
import os
import onewaysend
import responselistener

global usage
usage = { 'upload':0, 'dwnld':0, 'total':0 }

def bandwidth_monitor(threshold, mode):
    '''threshold indicates max Mbs. Mode is to decide 'upload','dwnld','total' usage'''
    global usage
    initup_count = initdwn_count = initbw_count = 0

    while True:
        print(usage)
        upload_count = psutil.net_io_counters().bytes_sent
        downld_count = psutil.net_io_counters().bytes_recv
        bandwd_count = upload_count + downld_count

        if initbw_count:    #If any usage has occurred
            meter([ upload_count-initup_count,
                         downld_count-initdwn_count,
                         bandwd_count-initbw_count ]) #Send upload, download & total bytes

        initbw_count  = bandwd_count
        initdwn_count = downld_count
        initup_count  = upload_count

        if convert_mbit(usage[mode]) >= threshold:

            print("Threshold Exceeded")

            msg = f'''You have exceeded your {mode} usage. Current usage is {convert_mbit(usage[mode])} & threshold is set at {threshold}. To execute programmed function, reply "execute"'''

            onewaysend.twilioSend(msg)
            res = responselistener.listen()
            wifiAction(res)
            return

        time.sleep(1)


def convert_mbit(value):
    '''Return value in mbits'''
    return value/1000000

def meter(value):
    global usage
    usage['upload'] += value[0]
    usage['dwnld']  += value[1]
    usage['total']  += value[2]

def wifiAction(cmd):
    if cmd == 'disablewifi':
        os.system("netsh wlan disconnect")
        onewaysend.twilioSend("Shut Down WiFi Successfully")
        return
    else:
        onewaysend.twilioSend("Invalid Command entered. Try again.")


if __name__ == '__main__':
    bandwidth_monitor(2,'dwnld') #Testing for 2 Mb download limit

