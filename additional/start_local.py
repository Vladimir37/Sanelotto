import os
import json

from additional.signals import signal_ok, signal_err
from additional.sshpass import ssh_exec_pass

def start_local(current_dir):
    try:
        local_file_sys = open(current_dir + '/' + 'Sanelotto_local/Sanelotto_local.json', 'r')
        local_file = local_file_sys.read()
        local_file = json.loads(local_file)
        local_file_sys.close()
    except:
        signal_err('Failed to read Sanelotto_local.json')
        return False

    # start before commands
    if local_file['before_start_commands']:
        try:
            before_addr = current_dir + '/' + 'Sanelotto_local/' + str(local_file['before_start_dir']) + '/before.slfile'
            before_commands = open(before_addr, 'r')
            for command in before_commands:
                os.system(command)
            signal_ok('Local commands successfully completed')
        except:
            signal_err('Failed to run local commands')
            return False

    # start command making
    start_command = 'cd ' + str(local_file['server_dir']) + ' && sanelotto start server > log_sanelotto.txt'

    # connect command making
    if local_file['ssh_key']:
        connect_command = 'ssh ' + str(local_file['login']) + '@' + local_file['server'] + ' "' + start_command + '"'
        os.system(connect_command)
    else:
        connect_command = ['ssh', str(local_file['login']) + '@' + local_file['server'], start_command]
        ssh_exec_pass(str(local_file['pass']), connect_command)