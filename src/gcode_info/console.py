from typing import Iterable

import click

from . import __version__
from .gcodeinfo import parse_file

MatrixOfStr = Iterable[Iterable[str]]


def as_columns(iter: MatrixOfStr) -> str:
    lines = ["\t".join(row) for row in iter]
    return "\n".join(lines)


@click.command()
@click.version_option(version=__version__)
@click.argument("files", type=click.Path(exists=True), nargs=-1)
def main(files):
    """Extract information from GCode files."""

    results = [parse_file(f) for f in files]
    print(as_columns(results))


if __name__ == "__main__":
    main()
