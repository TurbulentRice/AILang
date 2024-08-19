from core.constants import ALLOWED_SUBJECTS, ALLOWED_TYPES, ALLOWED_ARGS, ARG_PROMPT, NAMED_ARGS

class Parser:
    def parse(self, tokens):
        if not tokens:
            return None

        command = {
            'action': None,
            'subject': None,
            'type': None,
            'output_type': None,
            'args': {},
            'prompt': None,
            'path': None
        }

        # Parsing the action
        command['action'] = tokens.pop(0)
        if command['action'] not in ALLOWED_SUBJECTS:
            raise ValueError(f"Invalid action: {command['action']}")

        # Parsing the subject
        if tokens:
            command['subject'] = tokens.pop(0)
            if command['subject'] not in ALLOWED_SUBJECTS[command['action']]:
                raise ValueError(f"Invalid subject: {command['subject']}")

        # Parsing the input type
        if tokens and command['subject'] in ALLOWED_TYPES:
            command['type'] = tokens.pop(0)
            if command['type'] not in ALLOWED_TYPES[command['subject']]:
                raise ValueError(f"Invalid type: {command['type']}")
            
        # Parsing the output type (specific to the convert command)
        if command['action'] == 'convert' and tokens:
            command['output_type'] = tokens.pop(0)
            if command['output_type'] not in ALLOWED_TYPES[command['subject']]:
                raise ValueError(f"Invalid output type: {command['output_type']}")

        # Parsing the rest of the arguments
        while tokens:
            arg = tokens.pop(0)
            if arg in ALLOWED_ARGS[command['action']]:
                if tokens:
                    command['args'][NAMED_ARGS[arg]] = tokens.pop(0)
            elif arg == ARG_PROMPT:
                if tokens:
                    command['prompt'] = tokens.pop(0).strip('"')
            else:
                if not arg.startswith('-'):
                    command['path'] = arg

        return command

# Example usage
if __name__ == '__main__':
    parser = Parser()
    command_str = 'convert file json yaml -p "convert the configuration format" ./config/settings.json'
    tokens = command_str.split()
    parsed_command = parser.parse(tokens)
    print(parsed_command)
