import logging
from app.commands import Command

class DivideCommand(Command):
    def execute(self, a: str, b: str):
        """Divides two numbers."""
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            logging.error("Invalid input: Please provide valid numbers.")
            print("Invalid input: Please provide valid numbers.")
            return

        if b == 0:
            logging.error("Error: Division by zero.")
            print("Error: Division by zero.")
            return

        result = a / b
        logging.info(f"The result of {a} / {b} is {result}")
        print(f"The result of {a} / {b} is {result}")
        