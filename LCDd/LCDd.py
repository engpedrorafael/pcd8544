#!/usr/bin/env python

import os
import sys
import time
from commands import getstatusoutput

N_COLS=14
N_LINES=5
CURSOR="_"
PERIOD=1

if os.name != 'posix':
    sys.exit('platform not supported')

from datetime import datetime
import pcd8544.lcd as lcd

hb=False

def ifInfo():
    global hb

    lcd.locate(0, 5)
    st,out = getstatusoutput('ifconfig | grep "inet addr" | grep -v "127.0.0.1"')
    lineN=2
    if out:
        for line in [x for x in out.split(" ") if ":" in x and "cast" not in x and "addr" in x]:
            IP=(line.split(':')[1])
        lcd.text(IP+" "*(N_COLS-len(IP)))
    else:
        if hb:
            lcd.text(" "*N_COLS)
        else:
            lcd.text("  No network  ")

class LCD:
    vPos=0
    hPos=0
    lines=[]

    def __init__(self):
        lcd.init()
        lcd.backlight(1)
        lcd.cls()

    def write(self, line):
        ifInfo()
        self.lines.insert(0,line[0:N_COLS])
        if len(self.lines) == 6:
            self.lines.pop()
            for i,l in enumerate(self.lines):
                lcd.locate(0, i)
                lcd.text(self.lines[4-i]+" "*(N_COLS-len(self.lines[4-i])))
            self.hPos = min(len(self.lines[0]), N_COLS-1)
        else:
            lcd.locate(self.hPos, self.vPos)
            lcd.text(self.lines[0])
            self.vPos +=1
            if self.vPos == 5:
                self.vPos =4
                self.hPos = min(len(self.lines[0]), N_COLS-1)

    def blinkCursor(self, hb):
        lcd.locate(self.hPos, self.vPos)
        if hb:
            lcd.text(CURSOR)
        else:
            lcd.text(" ")


def main():
    global hb
    myLCD=LCD()

    ifInfo()

    f=open('/dev/lcd')
    while True:
        ifInfo()

        hb = not hb
        myLCD.blinkCursor(hb)


        fifo=f.readline()
        if fifo != "":
            myLCD.write(fifo.split('\n')[0])
        else:
            time.sleep(PERIOD)



if __name__ == "__main__":
    main()
