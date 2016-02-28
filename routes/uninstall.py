import os
import shutil

from additional.signals import signal_err, signal_ok, signal_done

def uninstall():
    try:
        home_dir = os.path.expanduser('~' + os.environ["SUDO_USER"])
    except:
        home_dir = os.path.expanduser('~')

    question = input('For uninstall Sanelotto enter "uninstall": ')
    if question != 'uninstall':
        print('Not uninstalled')
        return False

    if not os.access('/usr/local/bin/sanelotto', os.W_OK):
        signal_err('Permission denied')
        return False

    try:
        os.remove('/usr/local/bin/sanelotto')
        signal_ok('Link was deleted')
    except:
        signal_err('Failed to delete link. Permission denied or link not exist.')
        return False

    if os.access(home_dir + '/.sanelotto', os.F_OK):
        try:
            shutil.rmtree(home_dir + '/.sanelotto')
            signal_ok('Sanelotto directory was deleted')
        except:
            signal_err('Failed to delete Sanelotto directory')
            return False

    signal_done('Sanelotto was deleted')