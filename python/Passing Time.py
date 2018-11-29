def speedtest(startm,leng,starthr,startmin,spdlmt):
    time=leng/spdlmt*60
    endm=startm+leng
    if time>=60:
        processhr=time/60//1
        processmin=time-processhr*60
        endhr=starthr+processhr
        endmin=startmin+processmin
        if endmin>=60:
            endhr=endhr+1
            endmin=endmin-60
    else:
        pendmin=startmin+time
        if pendmin>=60:
            endhr=starthr+1
            endmin=pendmin-60
        else:
            endhr=starthr
            endmin=pendmin
    print(time)
    print(processhr)
    print(processmin)
    endhr=endhr//1
    endmin=endmin//1
    print("The speedtest will end at {0} km, the earliest passing time is {1}:{2}".format(endm,endhr,endmin))

def speedtesttemp(startm,leng,spdlmt):
    time=leng/spdlmt*60
    endm=startm+leng
    print("The speedtest will end at {0} km, the minimum passing time is {1}".format(endm,time))
