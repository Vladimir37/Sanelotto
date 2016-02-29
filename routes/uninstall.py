import os
import shutil

from additional.signals import signal_err, signal_ok, signal_done

def uninstall():
    sl_dir = '/usr/share/'

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

    try:
        shutil.rmtree(sl_dir + '/.sanelotto')
        signal_ok('Sanelotto directory was deleted')
    except:
        signal_err('Failed to delete Sanelotto directory')
        return False

    signal_done('Sanelotto was deleted')