import os
import json
import shutil
import unittest

class LocalTest(unittest.TestCase):
    def test_first_commands(self):
        os.system('sanelotto create testing')
        # configs overwrite
        config_file = open('testing/Sanelotto_server', 'rw')
        config = json.loads(config_file.read())
        config['github_name'] = 'Vladimir37'
        config['github_repo'] = 'Sanelotto'
        config_file.write(json.dumps(config))
        config_file.close()
        # commands writing
        commands = open('testing/Sanelotto_server/app/first.slfile', 'w')
        commands.write('mkdir test_dir\n')
        commands.write('touch test_file.txt')
        commands.close()
        # start
        os.system('cd testing && sanelotto start local')
        # checking
        dir_check = os.path.exists('testing/test_dir')
        file_check = os.path.exists('testing/test_file.txt')
        # cleaning
        shutil.rmtree('testing')

        self.assertTrue(dir_check and file_check)

suite = unittest.TestLoader().loadTestsFromTestCase(LocalTest)
unittest.TextTestRunner(verbosity=2).run(suite)