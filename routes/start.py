import os

from additional.signals import signal_err
from additional.start_local import start_local
from additional.start_server import start_server

def start(args):

    # correct and access check
    if len(args) < 3:
        signal_err('Local or server part?')
        return False

    start_type = args[2]

    if start_type != 'local' and start_type != 'server':
        signal_err('Incorrect part')
        return False

    current_dir = os.getcwd()

    if not os.access(current_dir + '/' + 'Sanelotto_' + start_type, os.F_OK):
        signal_err('Directory "' + start_type + '" not found')
        return False

    if not os.access(current_dir + '/' + 'Sanelotto_' + start_type, os.R_OK):
        signal_err('Permission denied')
        return False

    # launch
    if start_type == 'local':
        start_local(current_dir)

    elif start_type == 'server':
        start_server(current_dir)

    else:
        signal_err('Incorrect command')