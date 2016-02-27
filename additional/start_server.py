import os
import json

from additional.signals import signal_ok, signal_err

def start_server(current_dir):
    try:
        server_file_sys = open(current_dir + '/' + 'Sanelotto_server/Sanelotto_server.json', 'r')
        server_file = server_file_sys.read()
        server_file = json.loads(server_file)
        server_file_sys.close()
    except:
        signal_err('Failed to read Sanelotto_server.json')
        return False

    if server_file['use_sudo']:
        prefix = 'sudo '
    else:
        prefix = ''

    # reload project
    if os.path.exists(current_dir + '/' + server_file['name']):
        # stop command
        if server_file['stop_commands']:
            try:
                stop_sys = open(current_dir + '/' + server_file['commands_dir'] + '/stop.slfile')
                for command in stop_sys:
                    os.system(prefix + command)
                stop_sys.close()
            except:
                signal_err('Failed to run stop commands')
        os.system('cd ' + current_dir + '/' + server_file['name'] + ' && ' + prefix + 'git pull')
    # download project
    else:
        dl_addr = server_file['github_user'] + '/' + server_file['github_repo'] + ' -b ' + server_file['branch']
        os.system(prefix + 'git clone https://github.com/' + dl_addr)

    #