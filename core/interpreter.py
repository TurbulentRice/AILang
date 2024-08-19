from core.lexer import Lexer
from core.parser import Parser
from core.dispatch import DISPATCH_TABLE

class Interpreter:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
    
    def execute(self, command_str):
        tokens = self.lexer.tokenize(command_str)
        command = self.parser.parse(tokens)
        
        action = command['action']
        subject = command['subject']
        handler = DISPATCH_TABLE.get(action, {}).get(subject)
        
        if handler:
            handler(command)
        else:
            print(f"No handler found for action: {action} with subject: {subject}")
