#!/usr/bin/env python

import netifaces
import time
import sys

from internet import is_internet_connected
from error import show_error_notification, syslog


AVAILABLE_GATEWAYS = ('172.18.1.53', '10.10.1.100')
SLEEP_TIME = 10   # seconds


def main():
    sys.argv[0] = 'VPN Checker'
    syslog('Starting the service.')
    while True:
        gateways = netifaces.gateways()
        defaults = gateways['default']
        for gateway in defaults:
            ip,_ = defaults[gateway]
            if ip not in AVAILABLE_GATEWAYS and is_internet_connected():
                show_error_notification()
        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    main()
