import os
import json

from additional.signals import signal_done, signal_warn, signal_ok, signal_err
from additional.sshpass import ssh_exec_pass

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
    try:
        local_file_sys = open(current_dir + '/' + 'Sanelotto_' + start_type + '/Sanelotto_' + start_type + '.json', 'r')
        local_file = local_file_sys.read()
        local_file = json.loads(local_file)
        local_file_sys.close()
    except:
        signal_err('Failed to read Sanelotto_' + start_type + '.json')
        return False

    # start before commands
    if local_file['before_start_commands']:
        try:
            before_addr = current_dir + '/' + 'Sanelotto_' + start_type + '/' + local_file['before_start_dir'] + '/before.slfile'
            before_commands = open(current_dir, 'r')
            for command in before_commands:
                os.system(command)
            signal_ok('Local commands successfully completed')
        except:
            signal_err('Failed to run local commands')
            return False

    # start command making
    start_command = 'cd ' + local_file['server_dir'] + ' && sanelotto start server'

    # connect command making
    if local_file['ssh_key']:
        connect_command = 'ssh ' + local_file['login'] + '@' + local_file['server'] + ' "' + start_command + '"'
        os.system(connect_command)
    else:
        connect_command = ['ssh', local_file['login'] + '@' + local_file['server'], start_command]
        ssh_exec_pass(local_file['pass'], connect_command)