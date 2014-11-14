#!/bin/bash

echo "Installing LCDd.sh to /usr/local/sbin ..."
cp ./LCDd.sh /usr/local/sbin/
chmod 755 /usr/local/sbin/LCDd.sh

echo "Installing shutdownd to /etc/init.d ..."
cp ./lcdd /etc/init.d/
chmod 755 /etc/init.d/lcdd

echo "Installing Service..."
update-rc.d lcdd defaults
