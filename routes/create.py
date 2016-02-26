import os
import json

from additional.signals import signal_err, signal_ok, signal_done


def create(args):
    if len(args) < 3:
        signal_err('You have not entered a project name!')
        return False

    current_dir = os.getcwd()
    project_name = args[2]

    # creating dirs
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
        return False
    try:
        os.mkdir(current_dir + '/' + project_name + '/' + 'Sanelotto_server')
        os.mkdir(current_dir + '/' + project_name + '/' + 'Sanelotto_local')
        signal_ok('Configs directories was created')
    except:
        signal_err('Directory not been created!')
        return False

    # creating configs
    local_config = {
        'name': project_name,
        'server': '127.0.0.1',
        'ssh_key': False,
        'login': 'root',
        'pass': 'password',
        'before_start_commands': True,
        'before_start_dir': 'app',
        'server_dir': '/root'
    }
    server_config = {
        'name': project_name,
        'github_user': 'username',
        'github_repo': 'repository',
        'branch': 'master',
        'rewrite_configs': True,
        'configs_dir': 'configs',
        'start_commands': True,
        'stop_commands': True,
        'commands_dir': 'app'
    }
    local_config_json = json.dumps(local_config, sort_keys=True, indent=4)
    server_config_json = json.dumps(server_config, sort_keys=True, indent=4)

    # write to main configs
    local_config_file = open(current_dir + '/' + project_name + '/' + 'Sanelotto_local/Sanelotto_local.json', 'w')
    server_config_file = open(current_dir + '/' + project_name + '/' + 'Sanelotto_server/Sanelotto_server.json', 'w')
    try:
        local_config_file.write(local_config_json)
        server_config_file.write(server_config_json)

        local_config_file.close()
        server_config_file.close()

        signal_ok('Configs was created')
    except:
        signal_err('Configs not been created!')
        return False

    # additional directories
    if local_config['before_start_commands']:
        try:
            os.mkdir(current_dir + '/' + project_name + '/' + 'Sanelotto_local/app')
            open(current_dir + '/' + project_name + '/' + 'Sanelotto_local/app/before.slfile', 'w').close()
            signal_ok('Additional local files was created')
        except:
            signal_err('Additional local files not been created!')
            return False

    if server_config['rewrite_configs']:
        try:
            os.mkdir(current_dir + '/' + project_name + '/' + 'Sanelotto_server/configs')
            overwriting_config = open(current_dir + '/' + project_name + '/' + 'Sanelotto_server/configs/__main__.json', 'w')
            overwriting_config.write(json.dumps({}))
            overwriting_config.close()
            signal_ok('Configs files for overwriting was created')
        except:
            signal_err('Configs files for overwriting not been created!')
            return False

    if server_config['start_commands'] or server_config['stop_commands']:
        try:
            os.mkdir(current_dir + '/' + project_name + '/' + 'Sanelotto_server/app')
            signal_ok('Directory for additional commands was created')
        except:
            signal_err('Directory for additional commands not been created!')
            return False

    if server_config['start_commands']:
        try:
            open(current_dir + '/' + project_name + '/' + 'Sanelotto_server/app/start.slfile', 'w').close()
            signal_ok('File for start commands was created')
        except:
            signal_err('File for start commands not been created!')
            return False

    if server_config['stop_commands']:
        try:
            open(current_dir + '/' + project_name + '/' + 'Sanelotto_server/app/stop.slfile', 'w').close()
            signal_ok('File for stop commands was created')
        except:
            signal_err('File for stop commands not been created!')
            return False
    signal_done('Project ' + project_name + ' successfully created!')