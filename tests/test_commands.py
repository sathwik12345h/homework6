"""Tests for individual command implementations and the CommandHandler class."""

from app.plugins.add import AddCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.subtract import SubtractCommand
from app import Command, CommandHandler

def test_add_command(capfd):
    """Test the add command to ensure it correctly adds two numbers."""
    command = AddCommand()
    command.execute('2', '3')
    out, _ = capfd.readouterr()
    assert out == "The result of 2 + 3 is 5\n", \
        "AddCommand should output the correct result."

def test_add_command_invalid_input(capfd):
    """Test the add command with invalid input."""
    command = AddCommand()
    command.execute('two', 'three')
    out, _ = capfd.readouterr()
    assert out == "Invalid input: Please provide valid numbers.\n", \
        "AddCommand should handle invalid input."

def test_add_command_insufficient_arguments(capfd):
    """Test the add command with insufficient arguments."""
    command = AddCommand()
    command.execute('2')
    out, _ = capfd.readouterr()
    assert out == "Error: 'add' command requires exactly 2 arguments.\n", \
        "AddCommand should notify about insufficient arguments."

def test_add_command_too_many_arguments(capfd):
    """Test the add command with too many arguments."""
    command = AddCommand()
    command.execute('1', '2', '3')
    out, _ = capfd.readouterr()
    assert out == "Error: 'add' command requires exactly 2 arguments.\n", \
        "AddCommand should notify about too many arguments."

def test_multiply_command(capfd):
    """Test the multiply command to ensure it correctly multiplies two numbers."""
    command = MultiplyCommand()
    command.execute('2', '3')
    out, _ = capfd.readouterr()
    assert out == "The result of 2 * 3 is 6\n", \
        "MultiplyCommand should output the correct result."

def test_subtract_command(capfd):
    """Test the subtract command to ensure it correctly subtracts two numbers."""
    command = SubtractCommand()
    command.execute('5', '3')
    out, _ = capfd.readouterr()
    assert out == "The result of 5 - 3 is 2\n", \
        "SubtractCommand should output the correct result."

def test_divide_command(capfd):
    """Test the divide command to ensure it correctly divides two numbers."""
    command = DivideCommand()
    command.execute('6', '3')
    out, _ = capfd.readouterr()
    assert out == "The result of 6 / 3 is 2.0\n", \
        "DivideCommand should output the correct result."

def test_divide_by_zero(capfd):
    """Test the divide command to ensure it handles division by zero."""
    command = DivideCommand()
    command.execute('6', '0')
    out, _ = capfd.readouterr()
    assert out == "Error: Division by zero.\n", \
        "DivideCommand should output an error for division by zero."

def test_command_handler_empty_input(capfd):
    """Test that executing with an empty input prints the proper message."""
    handler = CommandHandler()
    handler.execute_command("   ")  # Input with only spaces
    out, _ = capfd.readouterr()
    assert out == "No command entered.\n", \
        "CommandHandler should print a message for empty input."

def test_command_handler_nonexistent_command(capfd):
    """Test that executing a command that hasn't been registered prints the proper error."""
    handler = CommandHandler()
    handler.execute_command("unknown")
    out, _ = capfd.readouterr()
    assert out == "No such command: unknown\n", \
        "CommandHandler should notify about unregistered commands."

def test_command_handler_registered_command(capfd):
    """Test that a registered command is executed correctly via the handler."""
    handler = CommandHandler()

    class DummyCommand(Command):
        """A dummy command for testing."""
        def execute(self, *args):
            print("Dummy command executed with args:", args)

    dummy = DummyCommand()
    handler.register_command("dummy", dummy)
    handler.execute_command("dummy arg1 arg2")
    out, _ = capfd.readouterr()
    assert out == "Dummy command executed with args: ('arg1', 'arg2')\n", \
        "CommandHandler should execute a registered command with the correct arguments."

def test_command_handler_exception(capfd):
    """Test that if a command raises an exception, the handler catches it and prints an error."""
    handler = CommandHandler()

    class FailingCommand(Command):
        """A command that always raises an exception."""
        def execute(self, *args):
            raise ValueError("Test exception")

    failing = FailingCommand()
    handler.register_command("fail", failing)
    handler.execute_command("fail arg")
    out, _ = capfd.readouterr()
    assert out == "An error occurred: Test exception\n", \
        "CommandHandler should catch exceptions and print an error message."

class DummyCommandHandler:
    """A dummy command handler with a 'commands' attribute."""
    def __init__(self):
        self.commands = {"command1": None, "command2": None}
