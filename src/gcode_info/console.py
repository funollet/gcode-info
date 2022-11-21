import click
from rich.console import Console
from rich.table import Table

from . import __version__
from .gcodeinfo import parse_file


@click.command()
@click.version_option(version=__version__)
@click.argument("files", type=click.Path(exists=True), nargs=-1)
def main(files):
    """Extract information from GCode files."""

    results = [parse_file(f) for f in files]

    table = Table(box=None)
    table.add_column("Duration", justify="right")
    table.add_column("Filament used", justify="right")
    table.add_column("Filename")

    for row in results:
        table.add_row(*row)

    console = Console()
    console.print(table)


if __name__ == "__main__":
    main()
