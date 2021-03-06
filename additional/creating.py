import os
import json

from additional.signals import signal_err, signal_ok, signal_done

def creating(current_dir, project_name, local_config, server_config):
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

    # configs to JSON
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
            os.mkdir(current_dir + '/' + project_name + '/' + 'Sanelotto_server/files')
            overwriting_config = open(current_dir + '/' + project_name + '/' + 'Sanelotto_server/files/__main__.json', 'w')
            overwriting_config.write(json.dumps({}))
            overwriting_config.close()
            signal_ok('Configs files for overwriting was created')
        except:
            signal_err('Configs files for overwriting not been created!')
            return False

    if server_config['logging']:
        try:
            os.mkdir(current_dir + '/' + project_name + '/' + 'Sanelotto_server/logs')
            os.mkdir(current_dir + '/' + project_name + '/' + 'Sanelotto_local/logs')
            signal_ok('Directory for logs was created')
        except:
            signal_err('Directory for logs not been created!')
            return False

    if server_config['start_commands'] or server_config['stop_commands']:
        try:
            os.mkdir(current_dir + '/' + project_name + '/' + 'Sanelotto_server/app')
            signal_ok('Directory for additional commands was created')
        except:
            signal_err('Directory for additional commands not been created!')
            return False

    if server_config['first_commands']:
        try:
            open(current_dir + '/' + project_name + '/' + 'Sanelotto_server/app/first.slfile', 'w').close()
            signal_ok('File for first commands was created')
        except:
            signal_err('File for first commands not been created!')
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