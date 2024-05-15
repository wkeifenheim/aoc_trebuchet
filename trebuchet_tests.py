import pytest
from trebuchet import calibration_sum, convert_text_to_number
from cal_input import cal_input


def test_partone_example():
    test_set = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    assert calibration_sum(test_set, False) == 142


def test_partone():
    assert calibration_sum(cal_input, False) == 54450


def test_parttwo_example():
    test_set = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    assert calibration_sum(test_set, True) == 281
