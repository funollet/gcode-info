from collections import namedtuple
from pathlib import Path
from typing import List, Tuple


def getlines(fname: str) -> List[str]:
    return Path(fname).read_text().splitlines()


def is_time(line: str) -> bool:
    return line.startswith(";TIME:")


def parse_line_time(line: str) -> int:
    return int(line.partition(":")[-1])


HoursMinutes = namedtuple("HoursMinutes", ["hours", "minutes"])


def seconds_to_hm(seconds: int) -> HoursMinutes:
    return HoursMinutes(int(seconds / 3600), int((seconds % 3600) / 60))


class GcodeInfo:
    def __init__(self, fname: str):
        self.fname = fname

    def set_time(self, line: str):
        self.seconds = parse_line_time(line)

    def values(self) -> Tuple:
        duration = seconds_to_hm(self.seconds)
        values = (
            f"{duration.hours}h.{duration.minutes}m",
            self.fname,
        )
        return values


def parse_file(fname: str) -> Tuple:
    data = GcodeInfo(fname)

    for line in getlines(fname):
        if is_time(line):
            data.set_time(line)

    return data.values()
