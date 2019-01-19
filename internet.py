import socket


def is_internet_connected(host="8.8.8.8", port=53, timeout=30):
    '''
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53
        Service: domain (DNS)
    '''
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        return False
