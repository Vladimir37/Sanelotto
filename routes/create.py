import os

from additional.signals import signal_err
from additional.creating import creating


def create(args):
    if len(args) < 3:
        signal_err('You have not entered a project name!')
        return False

    current_dir = os.getcwd()
    project_name = args[2]

    # creating configs
    local_config = {
        'name': project_name,
        'server': '127.0.0.1',
        'ssh_key': False,
        'login': 'root',
        'pass': 'password',
        'before_start_commands': True,
        'before_start_dir': 'app',
        'use_sudo': False,
        'logging': True,
        'server_dir': '/root'
    }
    server_config = {
        'name': project_name,
        'github_user': 'username',
        'github_repo': 'repository',
        'branch': 'master',
        'rewrite_configs': True,
        'configs_dir': 'files',
        'first_commands': True,
        'start_commands': True,
        'stop_commands': True,
        'use_sudo': False,
        'logging': True,
        'commands_dir': 'app'
    }

    creating(current_dir, project_name, local_config, server_config)