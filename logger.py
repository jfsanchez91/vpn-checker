import logging

import env

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)

def debug(msg):
    if not msg.endswith('.'):
        msg += '.'
    if env.get_boolean('DEBUG'):
        logging.warning('[DEBUG]: %s', msg)



