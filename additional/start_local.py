import os
import json
import datetime

from additional.signals import signal_ok, signal_err
from additional.sshpass import ssh_exec_pass

def start_local(current_dir):
    # current date
    print('---------------------------------------')
    print(datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"))
    print('---------------------------------------')

    try:
        local_file_sys = open(current_dir + '/' + 'Sanelotto_local/Sanelotto_local.json', 'r')
        local_file = local_file_sys.read()
        local_file = json.loads(local_file)
        local_file_sys.close()
    except:
        signal_err('Failed to read Sanelotto_local.json')
        return False

    # prefix and postfix
    prefix = ''
    postfix = ''
    postfix_s = ''
    if local_file['use_sudo']:
        prefix = 'sudo '
    if local_file['logging']:
        postfix = ' >> ' + current_dir + '/' + 'Sanelotto_local/logs/local_start.txt'
        postfix_s = ' >> Sanelotto_server/logs/server_main_start.txt'

    # start before commands
    if local_file['before_start_commands']:
        try:
            before_addr = current_dir + '/' + 'Sanelotto_local/' + str(local_file['before_start_dir']) + '/before.slfile'
            before_commands = open(before_addr, 'r')
            for command in before_commands:
                os.system(prefix + command + postfix)
            signal_ok('Local commands successfully completed')
        except:
            signal_err('Failed to run local commands')
            return False

    # start command making
    start_command = 'cd ' + str(local_file['server_dir']) + ' && ' + prefix + 'sanelotto start server' + postfix_s

    # connect command making
    if local_file['ssh_key']:
        connect_command = 'ssh ' + str(local_file['login']) + '@' + local_file['server'] + ' "' + start_command + '"'
        os.system(connect_command)
    else:
        connect_command = ['ssh', str(local_file['login']) + '@' + local_file['server'], start_command]
        ssh_exec_pass(str(local_file['pass']), connect_command)