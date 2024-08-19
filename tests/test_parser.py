import unittest
from core.parser import Parser
from core.constants import ACTION_CREATE, SUBJECT_PROJECT, TYPE_NODE, ARG_PROMPT, ARG_VERSION, ARG_NAME

class TestParser(unittest.TestCase):
    def test_parse(self):
        parser = Parser()
        command_str = f'{ACTION_CREATE} {SUBJECT_PROJECT} {TYPE_NODE} {ARG_VERSION} latest {ARG_NAME} my_project {ARG_PROMPT} "basic api with jwt token authentication" ./'
        tokens = command_str.split()
        parsed_command = parser.parse(tokens)
        expected = {
            'action': ACTION_CREATE,
            'subject': SUBJECT_PROJECT,
            'type': TYPE_NODE,
            'args': {
                ARG_VERSION: 'latest',
                ARG_NAME: 'my_project'
            },
            'prompt': 'basic api with jwt token authentication',
            'path': './'
        }
        self.assertEqual(parsed_command, expected)

if __name__ == '__main__':
    unittest.main()
