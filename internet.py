import socket
from subprocess import Popen, PIPE

import logger


def is_internet_connected(host="8.8.8.8", port=53, timeout=30):
    '''
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53
        Service: domain (DNS)
    '''
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        logger.debug('This computer is connected to Internet.')
        return True
    except Exception as ex:
        logger.debug('This computer is not connected to Internet.')
        return False


def __exec(args: list) -> bool:
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    return not process.wait()


def force_connect_vpn(vpn_name: str) -> None:
    cmd = 'nmcli con up'.split(' ')
    cmd.append(vpn_name)
    logger.debug(f'Running {cmd}.')
    return __exec(cmd)
