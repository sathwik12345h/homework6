import logging
import pytest

# Set up a logger for capturing logs during tests
logging.basicConfig(level=logging.INFO)

def test_exit_command(caplog):
    """Test that the ExitCommand logs the exit message and raises SystemExit."""
    from app.plugins.exit import ExitCommand

    command = ExitCommand(command_handler=None)

    with caplog.at_level(logging.INFO):  # Capture logs at INFO level
        with pytest.raises(SystemExit):
            command.execute()  # Execute the command

    # Verify that the log message was generated as expected
    assert "Exiting the application." in caplog.text
    assert "Exiting..." in caplog.text
