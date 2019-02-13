#!/usr/bin/env python

import netifaces
import time
import sys
import re

import env
import logger
from internet import is_internet_connected, force_connect_vpn
from error import show_error_notification, syslog


_DEFAULT_GATEWAYS = ('172.18.1.[\d]+', '10.10.1.100')
_DEFAULT_VPN_NAME = 'SyrconVPN'
SLEEP_TIME = 10   # seconds

AVAILABLE_GATEWAYS = env.get_list('AVAILABLE_GATEWAYS') or _DEFAULT_GATEWAYS
FORCE_CONNECT = env.get_boolean('FORCE_CONNECT')
VPN_NAME = env.get_str('VPN_NAME') or _DEFAULT_VPN_NAME

logger.debug(f'AVAILABLE_GATEWAYS = {AVAILABLE_GATEWAYS}')
logger.debug(f'FORCE_CONNECT = {FORCE_CONNECT}')
logger.debug(f'VPN_NAME = {VPN_NAME}')


_gateways = list(map(re.compile, map(lambda x: x + '$' if not x.endswith('$') else x, map(lambda x: x.replace('.', '\.'), _DEFAULT_GATEWAYS))))

def match(ip: str):
    return any(map(lambda x: x.match(ip), _gateways))

def check_vpn_status():
    gateways = netifaces.gateways()
    defaults = gateways['default']
    for gateway in defaults:
        ip,_ = defaults[gateway]
        if not match(ip) and is_internet_connected():
            if FORCE_CONNECT:
                force_connect_vpn(VPN_NAME)
            else:
                show_error_notification()
    time.sleep(SLEEP_TIME)


def main():
    sys.argv[0] = 'VPN Checker'
    msg = 'Starting the service.'
    syslog(msg)
    logger.debug(msg)
    while True:
        check_vpn_status()


if __name__ == "__main__":
    main()
