"""Test suite to ensure that the rocket has correct countdown and launch."""

from typer.testing import CliRunner

from rocket import main

runner = CliRunner()


def test_rocket_launch():
    """Ensure that the launch function displays correct output."""
    result = runner.invoke(
        main.cli, ["launch", "--rocket-dir", "input", "--rocket-file", "rocket.txt"]
    )
    assert result.exit_code == 0
    assert "Launch the rocket!" in result.stdout
    assert result.stdout.count("\n") == 44


def test_rocket_countdown():
    """Ensure that the countdown function displays correct output."""
    result = runner.invoke(
        main.cli,
        ["countdown", "--countdown-dir", "input", "--countdown-file", "countdown.txt"],
    )
    assert result.exit_code == 0
    assert "Countdown for the rocket's launch!" in result.stdout
    assert result.stdout.count("\n") == 9
