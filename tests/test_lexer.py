import unittest
from core.lexer import Lexer

class TestLexer(unittest.TestCase):
    def test_tokenize(self):
        lexer = Lexer()
        self.assertEqual(lexer.tokenize("create project node"), ["create", "project", "node"])

if __name__ == '__main__':
    unittest.main()