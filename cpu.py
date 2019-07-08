import psutil
import time
import responselistener

def monitor_cpu_times(mode,threshold):
    '''Monitor the CPU time in seconds spent in different modes in seconds

    modes is an integer and may be 0 (user), 1 (system) or 2 (idle)
    user & system mode measures CPU time in user and system mode respectively
    idle measures CPU idle time spent on doing nothing

    threshold - max time allowed in mentioned mode in seconds
    '''

    while True:
        val = psutil.cpu_times()[mode]
        if val > threshold:
            msg = f"CPU Time exceeded in {['user','system','idle'][mode]}. Current CPU Time is: {val} seconds. Reply 'execute' to carry out programmed action"
            onewaysend.twilioSend(msg)
            responselistener.listen()
            return
        time.sleep(1)



print(monitor_cpu_times(1,2))
