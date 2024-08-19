from core.interpreter import Interpreter

if __name__ == "__main__":
    interpreter = Interpreter()
    while True:
        try:
            command = input("AILang> ")
            interpreter.execute(command)
        except (ValueError, TypeError, KeyError) as e:
            print(e)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting AILang...")
            break
