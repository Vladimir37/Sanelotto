import os
import json
import shutil
import unittest

class LocalTest(unittest.TestCase):
    def test_first_commands(self):
        os.system('sanelotto create testing')
        # configs overwrite
        config_file = open('testing/Sanelotto_server/Sanelotto_server.json', 'r')
        config = json.loads(config_file.read())
        config_file.close()
        config_file = open('testing/Sanelotto_server/Sanelotto_server.json', 'w')
        config['github_user'] = 'Vladimir37'
        config['github_repo'] = 'Sanelotto'
        config_file.write(json.dumps(config))
        config_file.close()
        # commands writing
        commands = open('testing/Sanelotto_server/app/first.slfile', 'w')
        commands.write('mkdir test_first_dir\n')
        commands.write('touch test_first_file.txt')
        commands.close()
        # start
        os.system('cd testing && sanelotto start server')
        # checking
        dir_check = os.path.exists('testing/test_first_dir')
        file_check = os.path.exists('testing/test_first_file.txt')
        # cleaning
        shutil.rmtree('testing')

        self.assertTrue(dir_check and file_check)

    def test_stop_commands(self):
        os.system('sanelotto create testing')
        # configs overwrite
        config_file = open('testing/Sanelotto_server/Sanelotto_server.json', 'r')
        config = json.loads(config_file.read())
        config_file.close()
        config_file = open('testing/Sanelotto_server/Sanelotto_server.json', 'w')
        config['github_user'] = 'Vladimir37'
        config['github_repo'] = 'Sanelotto'
        config_file.write(json.dumps(config))
        config_file.close()
        # commands writing
        commands = open('testing/Sanelotto_server/app/stop.slfile', 'w')
        commands.write('mkdir test_stop_dir\n')
        commands.write('touch test_stop.txt')
        commands.close()
        # start
        os.system('cd testing && sanelotto start server')
        # precheck
        pre_dir_check = not os.path.exists('testing/test_stop_dir')
        pre_file_check = not os.path.exists('testing/test_stop.txt')
        # second start
        os.system('cd testing && sanelotto start server')
        # checking
        dir_check = os.path.exists('testing/test_stop_dir')
        file_check = os.path.exists('testing/test_stop.txt')
        # cleaning
        shutil.rmtree('testing')

        self.assertTrue(dir_check and file_check and pre_dir_check and pre_file_check)

    def test_start_commands(self):
        os.system('sanelotto create testing')
        # configs overwrite
        config_file = open('testing/Sanelotto_server/Sanelotto_server.json', 'r')
        config = json.loads(config_file.read())
        config_file.close()
        config_file = open('testing/Sanelotto_server/Sanelotto_server.json', 'w')
        config['github_user'] = 'Vladimir37'
        config['github_repo'] = 'Sanelotto'
        config['logging'] = False
        config_file.write(json.dumps(config))
        config_file.close()
        # commands writing
        commands = open('testing/Sanelotto_server/app/start.slfile', 'w')
        commands.write('echo TESTING >> testing.txt')
        commands.close()
        # start
        os.system('cd testing && sanelotto start server')
        os.system('cd testing && sanelotto start server')
        # checking
        check_file = open('testing/testing.txt', 'r')
        check = check_file.read()
        check_file.close()
        # cleaning
        shutil.rmtree('testing')

        self.assertTrue(check == 'TESTING\nTESTING\n')

    def test_overwriting(self):
        os.system('sanelotto create testing')
        # configs overwrite
        config_file = open('testing/Sanelotto_server/Sanelotto_server.json', 'r')
        config = json.loads(config_file.read())
        config_file.close()
        config_file = open('testing/Sanelotto_server/Sanelotto_server.json', 'w')
        config['github_user'] = 'Vladimir37'
        config['github_repo'] = 'Sanelotto'
        config_file.write(json.dumps(config))
        config_file.close()
        # overwriting config overwrite
        config_ow = {}
        config_ow_file = open('testing/Sanelotto_server/files/__main__.json', 'w')
        config_ow['test_one'] = os.path.abspath('testing/test_one_copy')
        config_ow['test_two'] = os.path.abspath('testing/test_two_copy')
        config_ow_file.write(json.dumps(config_ow))
        config_ow_file.close()
        # creating files
        os.system('touch testing/Sanelotto_server/files/test_one')
        os.system('touch testing/Sanelotto_server/files/test_two')
        # start
        os.system('cd testing && sanelotto start server')
        # checking
        file_check1 = os.path.exists(os.path.abspath('testing/test_one_copy'))
        file_check2 = os.path.exists(os.path.abspath('testing/test_two_copy'))
        # cleaning
        shutil.rmtree('testing')

        self.assertTrue(file_check1 and file_check2)

suite = unittest.TestLoader().loadTestsFromTestCase(LocalTest)
unittest.TextTestRunner(verbosity=2).run(suite)