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
        auth_type = input('Are you use ssh-key or login/password authentication? (key/pass): ')
        if auth_type != 'key' and auth_type != 'pass':
            print('Incorrect!')
            continue
        else:
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
        use_sudo_local = input('Do you want use "sudo" on local machine? (y/n): ')
        if use_sudo_local != 'y' and use_sudo_local != 'n':
            print('Incorrect!')
            continue
        else:
            if use_sudo_local == 'y':
                signal_warn('The user on local machine must have the right to use "sudo" without password')
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
        first_comm = input('Do you need special commands for first start project before downloading? (y/n): ')
        if first_comm != 'y' and first_comm != 'n':
            print('Incorrect!')
            continue
        else:
            break

    while True:
        stop_comm = input('Do you need special commands for stopping project before restart? (y/n): ')
        if stop_comm != 'y' and stop_comm != 'n':
            print('Incorrect!')
            continue
        else:
            break

    while True:
        use_sudo = input('Do you want use "sudo" on server? (y/n): ')
        if use_sudo != 'y' and use_sudo != 'n':
            print('Incorrect!')
            continue
        else:
            if use_sudo == 'y':
                signal_warn('The user on server must have the right to use "sudo" without password')
            break

    while True:
        config_ow = input('Will you overwrite configs or other files after downloading project on server? (y/n): ')
        if config_ow != 'y' and config_ow != 'n':
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
        'server_dir': server_dir,
        'use_sudo': use_sudo_local == 'y'
    }
    server_config = {
        'name': project_name,
        'github_user': gt_name,
        'github_repo': gt_repo,
        'branch': gt_branch,
        'rewrite_configs': config_ow == 'y',
        'configs_dir': 'files',
        'first_commands': first_comm == 'y',
        'start_commands': True,
        'stop_commands': stop_comm == 'y',
        'use_sudo': use_sudo == 'y',
        'commands_dir': 'app'
    }

    creating(current_dir, project_name, local_config, server_config)