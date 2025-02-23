from enum import Enum

#
#

TimeFormat = Enum('TimeFormat', [('Second', 1), ('Minute', 2), ('Hour', 3)])

#
#

def calculate_duration(entries: list, format : TimeFormat = TimeFormat.Second) -> int:
    match format:
        case TimeFormat.Second:
            return calculate_seconds(entries)
        case TimeFormat.Minute:
            return calculate_seconds(entries) / 60
        case TimeFormat.Hour:
            return calculate_seconds(entries) / 60 / 60

#
#

def calculate_seconds(entries: list) -> int:
    sum_seconds : int = 0
    for row in entries:
        sum_seconds += row[0]
    return sum_seconds