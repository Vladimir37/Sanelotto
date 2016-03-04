import os
import shutil
import unittest

class LocalTest(unittest.TestCase):
    def test_before_commands(self):
        # os.system('sanelotto create testing')
        self.assertEqual(1, 2)

suite = unittest.TestLoader().loadTestsFromTestCase(LocalTest)
unittest.TextTestRunner(verbosity=2).run(suite)