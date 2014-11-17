#!/usr/bin/env python

import os
import sys
import time
from commands import getstatusoutput

N_COLS=14
N_LINES=5

if os.name != 'posix':
    sys.exit('platform not supported')

from datetime import datetime
import pcd8544.lcd as lcd

hb=0
def ifInfo():
    global hb

    lcd.locate(0, 5)
    st,out = getstatusoutput('ifconfig | grep "inet addr" | grep -v "127.0.0.1"')
    lineN=2
    if out:
        for line in [x for x in out.split(" ") if ":" in x and "cast" not in x and "addr" in x]:
            IP=(line.split(':')[1])
        if hb:
            IP=IP.replace(".",",")

        lcd.text(IP+" "*(N_COLS-len(IP)))


    else:
        if hb:
            lcd.text(""*N_COLS)
        else:
            lcd.text("  No network  ")
    if hb:
        hb= 0
    else:
        hb= 1

class LCD:
    vPos=0
    hPos=0

    def __init__(self):
        lcd.init()
        lcd.backlight(1)
        lcd.cls()

    def write(self, line):
        ifInfo()
        lcd.locate(self.hPos, self.vPos)
        lcd.text(line[0:N_COLS])


def main():
    myLCD=LCD()

    ifInfo()

    f=open('/dev/lcd')
    while True:
        ifInfo()

        fifo=f.readline()
        if fifo != "":
            myLCD.write(fifo.strip())
        else:
            time.sleep(2)



if __name__ == "__main__":
    main()
