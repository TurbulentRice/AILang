from functools import wraps

def command_handler(*required_args):
    def decorator(func):
        @wraps(func)
        def wrapper(command):
            kwargs = {arg: command[arg] for arg in required_args if arg in command}
            kwargs.update({k: v for k, v in command.get('args', {}).items() if k in required_args})
            return func(**kwargs)
        return wrapper
    return decorator
