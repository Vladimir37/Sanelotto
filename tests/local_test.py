import os
import shutil
import unittest

class LocalTest(unittest.TestCase):
    def test_before_commands(self):
        os.system('sanelotto create testing')
        commands = open('testing/Sanelotto_local/app/before.slfile', 'w')
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

def local_testing():
    suite = unittest.TestLoader().loadTestsFromTestCase(LocalTest)
    unittest.TextTestRunner(verbosity=2).run(suite)