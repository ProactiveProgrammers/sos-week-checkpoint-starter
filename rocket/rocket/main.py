"""Display and countdown and a launch of a rocket."""

from pathlib import Path

import typer

# create a Typer object to support the command-line interface
cli = typer.Typer()


def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # determine if the file is not None and if it is a file
    if file is not None:
        # the file is valid
        if file.is_file():
            return True
    # the file was either none or not valid
    return False


@cli.command()
def countdown(
    countdown_dir: Path = typer.Option(None), countdown_file: Path = typer.Option(None)
):
    """Display a countdown before the rocket's launch as ASCII art."""
    # add extra space after the command to run the program
    print()
    # display a message to indicate that the rocket's countdown will start
    print("Countdown for the rocket's launch!")
    print()
    countdown_file_fully_qualified = countdown_dir / countdown_file
    if confirm_valid_file(countdown_file_fully_qualified):
        launch_contents_text = countdown_file_fully_qualified.read_text()
        print(launch_contents_text)
    else:
        print(f"{countdown_file_fully_qualified} was not a valid countdown file")


@cli.command()
def launch(
    rocket_dir: Path = typer.Option(None), rocket_file: Path = typer.Option(None)
):
    """Launch the rocket by display it take off as ASCII art."""
    # add extra space after the command to run the program
    print()
    # display a message to indicate that the rocket will launch
    print("Launch the rocket!")
    print()
    rocket_file_fully_qualified = rocket_dir / rocket_file
    if confirm_valid_file(rocket_file_fully_qualified):
        rocket_contents_text = rocket_file_fully_qualified.read_text()
        print(rocket_contents_text)
    else:
        print(f"{rocket_file_fully_qualified} was not a valid rocket file")
