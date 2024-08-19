import unittest
from core.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):
    def test_execute(self):
        interpreter = Interpreter()
        interpreter.execute("create project node")

if __name__ == '__main__':
    unittest.main()