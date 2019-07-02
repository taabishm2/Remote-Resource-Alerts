import time
import psutil
import os

global usage
usage = { 'upload':0, 'dwnld':0, 'total':0 }

def bandwidth_monitor(threshold, mode, effect):
    global usage
    
    initup_count = initdwn_count = initbw_count = 0    

    while True:
        upload_count = psutil.net_io_counters().bytes_sent
        downld_count = psutil.net_io_counters().bytes_recv
        bandwd_count = upload_count + downld_count
        
        if initbw_count:    #If any usage has occurred
            meter([ upload_count-initup_count,
                         downld_count-initdwn_count,
                         bandwd_count - initbw_count ]) #Send upload, download & total bytes

        if 

        initbw_count  = bandwd_count
        initdwn_count = downld_count
        initup_count  = upload_count
        time.sleep(1)

def convert_gbit(value):
    '''Return value in gbits'''
    return value/1024./1024./1024.*8
def convert_mbit(value):
    '''Return value in mbits'''
    return value/1024./1024.*8

def meter(value):
    global usage
    usage['upload'] += value[0]
    usage['dwnld']  += value[1]
    usage['total']  += value[2]



