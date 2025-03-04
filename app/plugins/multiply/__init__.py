import logging
from app.commands import Command

class MultiplyCommand(Command):
    def execute(self, *args):
        """Multiplies two numbers."""
        if len(args) != 2:
            print("Error: 'multiply' command requires exactly 2 arguments.")
            return

        try:
            a, b = map(int, args)
        except ValueError:
            logging.error("Invalid input: Please provide valid numbers.")
            print("Invalid input: Please provide valid numbers.")
            return

        result = a * b
        logging.info(f"The result of {a} * {b} is {result}")
        print(f"The result of {a} * {b} is {result}")
        