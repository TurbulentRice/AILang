import unittest
from core.commands import create_project, run_script

class TestCommands(unittest.TestCase):
    def test_create_project(self):
        # Test creating a project
        create_project('node', 'my_project', './', 'basic api with jwt token authentication')
        # Add assertions as needed

    def test_run_script(self):
        # Test running a script
        run_script('python', './script.py', 'run the script')
        # Add assertions as needed

if __name__ == '__main__':
    unittest.main()