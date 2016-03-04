import os
import shutil
import unittest

class CreateTest(unittest.TestCase):
    def test_generate_all(self):
        test_commands = open('test_commands', 'w')
        test_commands.write('testing\nlocalhost\nkey\nroot\ny\nn\n/home\nusername\nrepo\nmaser\ny\ny\nn\ny')
        test_commands.close()
        files = []
        os.system('sanelotto generate < test_commands')
        files.append(os.path.exists('testing/Sanelotto_local/Sanelotto_local.json'))
        files.append(os.path.exists('testing/Sanelotto_local/app/before.slfile'))
        files.append(os.path.exists('testing/Sanelotto_server/Sanelotto_server.json'))
        files.append(os.path.exists('testing/Sanelotto_server/app/first.slfile'))
        files.append(os.path.exists('testing/Sanelotto_server/app/start.slfile'))
        files.append(os.path.exists('testing/Sanelotto_server/app/stop.slfile'))
        files.append(os.path.exists('testing/Sanelotto_server/files/__main__.json'))
        files_exists = True
        for file in files:
            files_exists = files_exists and file
        # cleaning
        shutil.rmtree('testing')
        os.remove('test_commands')
        self.assertTrue(files_exists)

    def test_generate_min(self):
        test_commands = open('test_commands', 'w')
        test_commands.write('testing\nlocalhost\nkey\nroot\nn\nn\n/home\nusername\nrepo\nmaser\nn\nn\nn\nn')
        test_commands.close()
        files = []
        os.system('sanelotto generate < test_commands')
        files.append(os.path.exists('testing/Sanelotto_local/Sanelotto_local.json'))
        files.append(not os.path.exists('testing/Sanelotto_local/app/before.slfile'))
        files.append(os.path.exists('testing/Sanelotto_server/Sanelotto_server.json'))
        files.append(not os.path.exists('testing/Sanelotto_server/app/first.slfile'))
        files.append(os.path.exists('testing/Sanelotto_server/app/start.slfile'))
        files.append(not os.path.exists('testing/Sanelotto_server/app/stop.slfile'))
        files.append(not os.path.exists('testing/Sanelotto_server/files/__main__.json'))
        files_exists = True
        for file in files:
            files_exists = files_exists and file
        # cleaning
        shutil.rmtree('testing')
        os.remove('test_commands')
        self.assertTrue(files_exists)

    def test_create(self):
        os.system('sanelotto create testing')
        local_file = os.path.exists('testing/Sanelotto_local/Sanelotto_local.json')
        server_file = os.path.exists('testing/Sanelotto_server/Sanelotto_server.json')
        shutil.rmtree('testing')
        self.assertTrue(local_file and server_file)

suite = unittest.TestLoader().loadTestsFromTestCase(CreateTest)
unittest.TextTestRunner(verbosity=2).run(suite)