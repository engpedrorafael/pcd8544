#!/bin/bash

echo "Installing LCDd.py to /usr/local/sbin ..."
cp ./LCDd.py /usr/local/sbin/
chmod 755 /usr/local/sbin/LCDd.py

echo "Installing lcdd to /etc/init.d ..."
cp ./lcdd /etc/init.d/
chmod 755 /etc/init.d/lcdd

echo "Installing Service..."
update-rc.d lcdd defaults
