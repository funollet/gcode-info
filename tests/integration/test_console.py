import click.testing

from gcode_info import console
from gcode_info.gcodeinfo import parse_file


def test_main_succeeds():
    runner = click.testing.CliRunner()
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_parse_file():
    result = parse_file("tests/fixtures/files/Holder_Bosch_GSR_10p8V.gcode")
    assert "11h 23m" in result[0]
    assert "tests/fixtures/files/Holder_Bosch_GSR_10p8V.gcode" in result[1]
