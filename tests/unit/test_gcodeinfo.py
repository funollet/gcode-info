from gcode_info.gcodeinfo import (
    is_filament_used,
    is_time,
    parse_filament_used,
    parse_line_time,
    seconds_to_hm,
)


def test_seconds_to_hm():
    assert seconds_to_hm(59).hours == 0
    assert seconds_to_hm(59).minutes == 0

    assert seconds_to_hm(60).hours == 0
    assert seconds_to_hm(60).minutes == 1

    assert seconds_to_hm(121).hours == 0
    assert seconds_to_hm(121).minutes == 2

    assert seconds_to_hm(7319).hours == 2
    assert seconds_to_hm(7319).minutes == 1


def test_is_time():
    assert is_time(";TIME:41007") is True
    assert is_time("TIME:41007") is False
    assert is_time(";Time:41007") is False


def test_parse_line_time():
    assert parse_line_time(";TIME:41007") == 41007


def test_is_filament_used():
    assert is_filament_used(";Filament used: 10.0m") is True
    assert is_filament_used(";filament used: 10.0m") is True
    assert is_filament_used(";FILAMENT USED: 10.0m") is True
    assert is_filament_used("Filament used: 10.0m") is False
    assert is_filament_used(";filament used: 10.0m") is True
    assert is_filament_used("A lot of Filament is used: 10.0m") is False


def test_parse_filament_used():
    assert parse_filament_used(";Filament used: 10.0m") == 10.0
