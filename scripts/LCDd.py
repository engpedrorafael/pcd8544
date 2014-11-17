#!/usr/bin/env python

import os
import sys
import time
from commands import getstatusoutput

if os.name != 'posix':
    sys.exit('platform not supported')

from datetime import datetime
import pcd8544.lcd as lcd

hb=0
def ifInfo():
    global hb

    st,out = getstatusoutput('ifconfig | grep "inet addr" | grep -v "127.0.0.1"')
    lineN=2
    if out:
        for line in [x for x in out.split(" ") if ":" in x and "cast" not in x]:
            lcd.locate(0, lineN)
            lcd.text(line.split(':')[1])
            lineN += 1

        st,out = getstatusoutput("/sbin/ip route | awk '/default/ { print $3 }'")
        lcd.locate(0, lineN)
        lcd.text(out)
    else:
        lcd.cls()
        lcd.locate(0, lineN)
        if hb:
            lcd.text("            ")
        else:
            lcd.text("  No network")

    lcd.locate(0,0)
    st,hostName=getstatusoutput("cat /etc/hostname")
    lcd.text(hostName)


    lcd.locate(0, 5)
    if hb:
        lcd.text(".")
        hb=0
    else:
        lcd.text(" ")
        hb=1


def stats():
    lcd.cls()
    while 1:
        ifInfo()
        time.sleep(2)

def main():
    lcd.init()
    lcd.backlight(1)
    stats()


if __name__ == "__main__":
    main()
