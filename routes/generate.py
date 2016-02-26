import os

from additional.signals import signal_warn
from additional.creating import creating

def generate():
    current_dir = os.getcwd()

    print('------- LOCAL SETTINGS -------')
    while True:
        project_name = input('Enter project name: ')
        if not project_name:
            print('Incorrect name!')
            continue
        else:
            break

    while True:
        server_addr = input('Enter your server name for deploying (Example: 127.0.0.1): ')
        if not server_addr:
            print('Incorrect server name!')
            continue
        else:
            break

    while True:
        signal_warn('If you will use login and password, then on local machine will be installed "sshpass" ')
        auth_type = input('Are you use ssh-key or login/password authentication? (key/pass): ')
        if auth_type != 'key' and auth_type != 'pass':
            print('Incorrect!')
            continue
        else:
            signal_warn('"sshpass" will be installed when you first start deploy project')
            break

    while True:
        username = input('Enter your username on server? (Example: root): ')
        if not username:
            print('Incorrect!')
            continue
        else:
            break

    if auth_type == 'pass':
        while True:
            password = input('Enter your password for server: ')
            if not password:
                print('Incorrect!')
                continue
            else:
                break
    else:
        password = False

    while True:
        before_commands = input('Will you run commands on local machine before deploying? (y/n): ')
        if before_commands != 'y' and before_commands != 'n':
            print('Incorrect!')
            continue
        else:
            break

    while True:
        server_dir = input('Enter directory on server for your application (Example: /home/username): ')
        if not server_dir:
            print('Incorrect!')
            continue
        else:
            break

    print('------- SERVER SETTINGS -------')
    while True:
        gt_name = input('Enter your username on GitHub: ')
        if not gt_name:
            print('Incorrect!')
            continue
        else:
            break

    while True:
        gt_repo = input('Enter repository name on GitHub: ')
        if not gt_repo:
            print('Incorrect!')
            continue
        else:
            break

    while True:
        gt_branch = input('Enter desired branch name on repository (Example: master): ')
        if not gt_branch:
            print('Incorrect!')
            continue
        else:
            break

    while True:
        stop_comm = input('Do you need special commands for stopping project before restart? (y/n): ')
        if not stop_comm != 'y' and stop_comm != 'n':
            print('Incorrect!')
            continue
        else:
            break

    while True:
        config_ow = input('Will you overwrite JSON configs after downloading project on server? (y/n): ')
        if not config_ow != 'y' and config_ow != 'n':
            print('Incorrect!')
            continue
        else:
            break

    # creating configs
    local_config = {
        'name': project_name,
        'server': server_addr,
        'ssh_key': auth_type == 'key',
        'login': username,
        'pass': password,
        'before_start_commands': before_commands == 'y',
        'before_start_dir': 'app',
        'server_dir': server_dir
    }
    server_config = {
        'name': project_name,
        'github_user': gt_name,
        'github_repo': gt_repo,
        'branch': gt_branch,
        'rewrite_configs': config_ow == 'y',
        'configs_dir': 'configs',
        'start_commands': True,
        'stop_commands': stop_comm == 'y',
        'commands_dir': 'app'
    }

    creating(current_dir, project_name, local_config, server_config)