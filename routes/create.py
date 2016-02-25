import os
import json

from signals import signal_done, signal_err, signal_ok

def create(args):
    if len(args) < 3:
        print('You have not entered a project name!')
    else:
        current_dir = os.getcwd()
        project_name = args[2]
        if os.access(current_dir, os.W_OK):
            signal_ok('The directory defined')
        else:
            signal_err('Permission denied')
            return False
        try:
            os.mkdir(current_dir + '/' + project_name)
            signal_ok('Project directory created')
        except:
            signal_err('Directory is exist!')
        os.mkdir(current_dir + '/' + project_name + '/' + 'Sanelotto_server')
        local_config = {
            'name': project_name,
            'server': '127.0.0.1',
            'ssh_key': False,
            'login': 'root',
            'pass': 'password',
            'dir': '/root'
        }
        server_config = {
            'name': project_name,
            'github_user': 'username',
            'github_repo': 'repository',
            'branch': 'master',
            'rewrite_configs': True
        }