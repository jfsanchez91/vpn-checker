import syslog as _syslog
import notify2 as notify


TITLE = 'VPN Checker'
MESSAGE = 'You are connected to internet without using a valid VPN.'


def syslog(message=''):
    '''
        Message: Text to log in the system syslog file. Should not be empty.
    '''
    if message:
        _syslog.syslog(message)


def show_error_notification():
    '''
        Display a notification message in the $USER desktop and 
        log the same message in the system syslog file.
    '''
    syslog(MESSAGE)
    notify.init('VPN Checker')
    n = notify.Notification(TITLE, MESSAGE)
    n.show()