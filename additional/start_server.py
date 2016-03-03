import os
import json
import shutil
import datetime

from additional.signals import signal_ok, signal_err, signal_done

def start_server(current_dir):
    # current date
    print('#####################')
    print('# ' + datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S") + ' #')
    print('#####################')

    try:
        server_file_sys = open(current_dir + '/' + 'Sanelotto_server/Sanelotto_server.json', 'r')
        server_file = server_file_sys.read()
        server_file = json.loads(server_file)
        server_file_sys.close()
    except:
        signal_err('Failed to read Sanelotto_server.json')
        return False

    # prefix and postfix
    prefix = ''
    postfix = ''
    if server_file['use_sudo']:
        prefix = 'sudo '
    if server_file['logging']:
        postfix = ' >> ' + current_dir + '/' + 'Sanelotto_server/logs/server_actions.txt'

    # reload project
    if os.path.exists(current_dir + '/' + str(server_file['github_repo'])):
        # stop command
        if server_file['stop_commands']:
            try:
                stop_sys = open(current_dir + '/Sanelotto_server/' + str(server_file['commands_dir']) + '/stop.slfile', 'r')
                for command in stop_sys:
                    os.system(prefix + command + postfix)
                stop_sys.close()
                signal_ok('Stop commands completed')
            except:
                signal_err('Failed to run stop commands')
                return False
        # reload from GitHub
        os.system('cd ' + current_dir + '/' + str(server_file['github_repo']) + ' && ' + prefix + 'git reset --hard HEAD')
        os.system('cd ' + current_dir + '/' + str(server_file['github_repo']) + ' && ' + prefix + 'git clean -f -d')
        os.system('cd ' + current_dir + '/' + str(server_file['github_repo']) + ' && ' + prefix + 'git pull' + postfix)
        signal_ok('Project was updated from GitHub')
    # download project
    else:
        dl_addr = str(server_file['github_user']) + '/' + server_file['github_repo'] + ' -b ' + server_file['branch']
        os.system(prefix + 'git clone https://github.com/' + dl_addr + postfix)
        os.system('cd ' + current_dir + '/' + str(server_file['github_repo']) + ' && ' + prefix + 'git reset --hard')
        signal_ok('Project was downloaded from GitHub')
        # first commands
        if server_file['first_commands']:
            try:
                first_sys = open(current_dir + '/Sanelotto_server/' + str(server_file['commands_dir']) + '/first.slfile', 'r')
                for command in first_sys:
                    os.system(prefix + command + postfix)
                first_sys.close()
                signal_ok('First commands completed')
            except:
                signal_err('Failed to run first commands')
                return False

    # config overwrite
    if server_file['rewrite_configs']:
        # read __main__
        try:
            config_main_sys = open(current_dir + '/Sanelotto_server/' + str(server_file['configs_dir']) + '/' + '__main__.json', 'r')
            config_main = config_main_sys.read()
            config_main = json.loads(config_main)
            config_main_sys.close()
            signal_ok('__main__.json successfully read')
        except:
            signal_err('Failed to read __main__.json')
            return False

        # overwriting
        for config_name in config_main:
            try:
                shutil.copyfile(current_dir + '/Sanelotto_server/' + str(server_file['configs_dir']) + '/' + config_name,
                                config_main[config_name])
                signal_ok('Copying ' + config_name)
            except:
                signal_err('Failed to copy ' + config_name)
                return False
        signal_ok('Overwriting successfully completed!')

        # launch
        if server_file['start_commands']:
            try:
                stop_sys = open(current_dir + '/Sanelotto_server/' + str(server_file['commands_dir']) + '/start.slfile', 'r')
                for command in stop_sys:
                    os.system(prefix + command + postfix)
                stop_sys.close()
                signal_ok('Start commands completed')
            except:
                signal_err('Failed to run start commands')
                return False

        signal_done('Project successfully started')